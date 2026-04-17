import argparse
import os
import time

import cv2
import numpy as np


VALID_EXTENSIONS = (".jpg", ".jpeg", ".webp", ".tiff", ".tif", ".bmp", ".png")


def build_parser():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--input_dir",
        dest="InputPath",
        default="/home/ispl-public/Desktop/Dataset/LIME",
        help="directory for testing inputs",
    )
    parser.add_argument(
        "--output_dir",
        dest="OutputPath",
        default="./",
        help="directory for testing outputs",
    )
    parser.add_argument(
        "--gamma_max",
        dest="gamma_max",
        type=float,
        default=6.0,
        help="maximum gamma value used as an auto-tuning upper bound",
    )
    return parser


""" pixel value: i2f: 0-255 to 0-1, f2i: 0-1 to 0-255 """


def i2f(i_image):
    f_image = np.float32(i_image) / 255.0
    return f_image


def f2i(f_image):
    i_image = np.uint8(np.clip(f_image, 0.0, 1.0) * 255.0)
    return i_image


""" Compute 'A' as described by Tang et al. (CVPR 2014) """


def Compute_A_Tang(im):
    erosion_window = 15
    n_bins = 200

    dark = cv2.erode(
        np.min(im, axis=2), np.ones((erosion_window, erosion_window), dtype=np.uint8)
    )

    [h, edges] = np.histogram(dark, n_bins, [0, 1])
    numpixel = im.shape[0] * im.shape[1]
    thr_frac = numpixel * 0.99
    csum = np.cumsum(h)
    nz_idx = min(np.searchsorted(csum, thr_frac), n_bins - 1)
    dc_thr = edges[nz_idx]
    mask = dark >= dc_thr
    if not np.any(mask):
        mask = dark >= np.percentile(dark, 99)

    A = np.median(im[mask], axis=0, keepdims=True)

    return np.maximum(A, np.finfo(np.float32).eps)


def GetIntensity(fi):
    return np.mean(fi, axis=2)


def GetMax(fi):
    return np.max(fi, axis=2)


def GetMin(fi):
    return np.min(fi, axis=2)


""" Pixel Adaptive Gamma Correction """


def PixelAdaptiveGamma(InputImg, NormImg, amax):
    amin = 1
    xmax = 1
    xmin = 0
    Imax = GetMax(InputImg)

    a = (amax - amin) / (np.exp(-xmin) - np.exp(-xmax))
    b = amax - a * np.exp(-xmin)
    g2 = a * np.exp(-Imax) + b
    g1 = np.where(Imax < xmin, amax, g2)
    gamma = np.where(Imax > xmax, amin, g1)

    GCImg = np.power(NormImg, gamma[:, :, None])

    return GCImg, gamma


""" Estimate Transmission Map """


def EstimateTransmission(InputImg, NormImg, gamma_max=6):
    T_min = 0.1
    me = np.finfo(np.float32).eps
    hi = GetIntensity(NormImg)
    hmax = GetMax(NormImg)

    GCImg, gamma = PixelAdaptiveGamma(InputImg, NormImg, gamma_max)

    ji = GetIntensity(GCImg)
    jmax = GetMax(GCImg)

    tn = np.maximum(jmax * hi - hmax * ji, me)
    td = np.maximum((jmax - ji) * hi, me)

    Tmap = 1.0 - hi * (tn / td)

    return np.clip(Tmap, T_min, 1.0), gamma


""" Recover dehazed image """


def Recover(im, tmap, A):
    res = (im - 1.0 + A.reshape(1, 1, 3)) / tmap[:, :, None] + 1.0 - A.reshape(1, 1, 3)
    return np.clip(res, 0.0, 1.0)


""" Adjust image range """


def Adjust(im, perh, perl):
    im_h = np.percentile(im, perh)
    im_l = np.percentile(im, perl)
    aim = (im - im_l) / max(im_h - im_l, np.finfo(np.float32).eps)
    return np.clip(aim, 0.0, 1.0)


""" Normalize image 0 between 1 """


def Normalize(im):
    im_h = np.max(im, axis=(0, 1), keepdims=True)
    im_l = np.min(im, axis=(0, 1), keepdims=True)
    aim = (im - im_l) / np.maximum(im_h - im_l, np.finfo(np.float32).eps)
    return np.clip(aim, 0.0, 1.0)


def EstimateNoiseLevel(InputImg):
    gray = cv2.cvtColor(InputImg, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
    laplacian = cv2.Laplacian(gray, cv2.CV_32F, ksize=3)
    return float(np.median(np.abs(laplacian)) / 0.6745)


def AutoTuneParameters(InputImg, gamma_limit):
    gray = cv2.cvtColor(InputImg, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
    brightness = float(np.mean(gray))
    contrast = float(np.std(gray))
    noise_level = EstimateNoiseLevel(InputImg)

    darkness = np.clip((0.6 - brightness) / 0.6, 0.0, 1.0)
    contrast_penalty = np.clip((0.25 - contrast) / 0.25, 0.0, 1.0)
    noise_factor = np.clip(noise_level / 0.12, 0.0, 1.0)

    gamma_cap = max(float(gamma_limit), 1.0)
    gamma_drive = np.clip(
        0.7 * darkness + 0.3 * contrast_penalty + 0.2 * noise_factor, 0.15, 1.0
    )
    tuned_gamma_max = 1.0 + (gamma_cap - 1.0) * gamma_drive

    area = InputImg.shape[0] * InputImg.shape[1]
    target_pixels = 1280 * 720
    processing_scale = 1.0
    if area > target_pixels:
        processing_scale = float(np.sqrt(target_pixels / area))

    return {
        "brightness": brightness,
        "contrast": contrast,
        "noise_level": noise_level,
        "noise_factor": float(noise_factor),
        "darkness": float(darkness),
        "gamma_max": float(np.clip(tuned_gamma_max, 1.0, gamma_cap)),
        "denoise_h": int(np.clip(round(5 + 12 * noise_factor + 5 * darkness), 5, 20)),
        "denoise_h_color": int(
            np.clip(round(5 + 8 * noise_factor + 3 * darkness), 5, 16)
        ),
        "bilateral_sigma_color": int(
            np.clip(round(20 + 55 * (0.6 * noise_factor + 0.4 * darkness)), 20, 75)
        ),
        "bilateral_sigma_space": int(np.clip(round(7 + 8 * noise_factor), 7, 15)),
        "processing_scale": processing_scale,
        "adjust_high": 99.7 if darkness > 0.5 else 99.5,
        "adjust_low": 0.3 if contrast_penalty > 0.5 else 0.5,
    }


def ResizeImage(image, scale, interpolation):
    if scale >= 0.999:
        return image

    height, width = image.shape[:2]
    new_size = (
        max(1, int(round(width * scale))),
        max(1, int(round(height * scale))),
    )
    return cv2.resize(image, new_size, interpolation=interpolation)


def DenoiseImage(InputImg, params):
    if params["processing_scale"] < 0.9:
        small = ResizeImage(InputImg, params["processing_scale"], cv2.INTER_AREA)
        small_denoised = cv2.fastNlMeansDenoisingColored(
            small,
            None,
            params["denoise_h"],
            params["denoise_h_color"],
            7,
            21,
        )
        denoise_prior = cv2.resize(
            small_denoised,
            (InputImg.shape[1], InputImg.shape[0]),
            interpolation=cv2.INTER_LINEAR,
        )
        edge_preserved = cv2.bilateralFilter(
            InputImg,
            7,
            params["bilateral_sigma_color"],
            params["bilateral_sigma_space"],
        )
        denoised = cv2.addWeighted(edge_preserved, 0.6, denoise_prior, 0.4, 0)
    else:
        denoised = cv2.fastNlMeansDenoisingColored(
            InputImg,
            None,
            params["denoise_h"],
            params["denoise_h_color"],
            7,
            21,
        )

    if params["noise_factor"] > 0.3 or params["darkness"] > 0.45:
        denoised = cv2.bilateralFilter(
            denoised,
            5,
            params["bilateral_sigma_color"],
            params["bilateral_sigma_space"],
        )

    return denoised


""" Main """


def enhance_image(InputImg, gamma_max, return_details=False):
    start_time = time.time()
    params = AutoTuneParameters(InputImg, gamma_max)
    denoised_input = DenoiseImage(InputImg, params)
    original_float = i2f(InputImg)
    denoised_float = i2f(denoised_input)

    working_float = ResizeImage(
        denoised_float, params["processing_scale"], cv2.INTER_AREA
    )
    DenoiseImg = 1.0 - working_float

    A = Compute_A_Tang(DenoiseImg)
    NormImg = Normalize(DenoiseImg / A.reshape(1, 1, 3))

    Transmap, gamma_map = EstimateTransmission(
        working_float, NormImg, params["gamma_max"]
    )
    if params["processing_scale"] < 0.999:
        target_size = (InputImg.shape[1], InputImg.shape[0])
        Transmap = cv2.resize(Transmap, target_size, interpolation=cv2.INTER_LINEAR)
        gamma_map = cv2.resize(gamma_map, target_size, interpolation=cv2.INTER_LINEAR)

    RecoverImg = Recover(original_float, Transmap, A)
    AdjustImg = Adjust(RecoverImg, params["adjust_high"], params["adjust_low"])

    end_time = time.time()
    details = {
        **params,
        "gamma_map": gamma_map,
        "transmission_map": Transmap,
        "runtime": end_time - start_time,
    }
    print(
        "--- %.3f seconds | gamma_max=%.2f | denoise_h=%d | scale=%.2f ---"
        % (
            details["runtime"],
            details["gamma_max"],
            details["denoise_h"],
            details["processing_scale"],
        )
    )

    if return_details:
        return AdjustImg, details
    return AdjustImg


def run_folder(InputPath, OutputPath, gamma_max):
    FolderTemp = os.path.normpath(InputPath).split(os.sep)
    output_dir = os.path.join(OutputPath, "Output", FolderTemp[-1])
    os.makedirs(output_dir, exist_ok=True, mode=0o777)

    FileList = sorted(
        [
            file
            for file in os.listdir(InputPath)
            if os.path.splitext(file)[1].lower() in VALID_EXTENSIONS
        ]
    )

    for file_name in FileList:
        file_path = os.path.join(InputPath, file_name)
        InputImg = cv2.imread(file_path, cv2.IMREAD_COLOR)
        if InputImg is None:
            continue

        OutputImg = enhance_image(InputImg, gamma_max)

        name, _ = os.path.splitext(file_name)
        cv2.imwrite(os.path.join(output_dir, name + ".png"), f2i(OutputImg))


if __name__ == "__main__":
    cv2.setUseOptimized(True)
    args = build_parser().parse_args()
    run_folder(args.InputPath, args.OutputPath, args.gamma_max)
