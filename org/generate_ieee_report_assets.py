import contextlib
import csv
import io
import os
import shutil

import cv2
import matplotlib
import numpy as np

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from Run_LowLight_Image_Enhancement_Pixel_Adaptive import enhance_image, f2i
from demo_enhancement import demo_enhancement


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(ROOT_DIR, "input")
OUTPUT_DIR = os.path.join(ROOT_DIR, "newOutput", "Output", "input")
ASSET_DIR = os.path.join(ROOT_DIR, "report_assets")
FIGURE_DIR = os.path.join(ASSET_DIR, "figures")
TABLE_DIR = os.path.join(ASSET_DIR, "tables")


def ensure_dirs():
    os.makedirs(FIGURE_DIR, exist_ok=True)
    os.makedirs(TABLE_DIR, exist_ok=True)


def compute_entropy(gray_image):
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256]).ravel()
    probs = hist / max(np.sum(hist), 1.0)
    probs = probs[probs > 0]
    return float(-np.sum(probs * np.log2(probs)))


def compute_metrics(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lap_var = cv2.Laplacian(gray, cv2.CV_32F).var()
    return {
        "brightness": float(gray.mean()),
        "contrast": float(gray.std()),
        "entropy": compute_entropy(gray),
        "sharpness": float(lap_var),
    }


def get_image_list():
    return sorted(
        [
            file
            for file in os.listdir(INPUT_DIR)
            if file.lower().endswith((".png", ".jpg", ".jpeg"))
        ]
    )


def load_image(path):
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(path)
    return image


def generate_demo_figure():
    demo_input = os.path.join(INPUT_DIR, "2.png")
    demo_output_dir = os.path.join(FIGURE_DIR, "demo")
    with contextlib.redirect_stdout(io.StringIO()):
        demo_enhancement(demo_input, output_dir=demo_output_dir)
    generated = os.path.join(demo_output_dir, "demo_result.png")
    target = os.path.join(FIGURE_DIR, "demo_result.png")
    shutil.copyfile(generated, target)
    return demo_input, target


def collect_dataset_rows(image_files):
    rows = []
    for file_name in image_files:
        input_path = os.path.join(INPUT_DIR, file_name)
        output_path = os.path.join(OUTPUT_DIR, file_name)

        original = load_image(input_path)
        enhanced = load_image(output_path)

        with contextlib.redirect_stdout(io.StringIO()):
            _, details = enhance_image(original, 6.0, return_details=True)

        original_metrics = compute_metrics(original)
        enhanced_metrics = compute_metrics(enhanced)
        area = int(original.shape[0] * original.shape[1])

        row = {
            "file": file_name,
            "width": int(original.shape[1]),
            "height": int(original.shape[0]),
            "pixels": area,
            "gamma_max": float(details["gamma_max"]),
            "denoise_h": int(details["denoise_h"]),
            "processing_scale": float(details["processing_scale"]),
            "runtime_s": float(details["runtime"]),
        }
        for key, value in original_metrics.items():
            row[f"original_{key}"] = value
        for key, value in enhanced_metrics.items():
            row[f"enhanced_{key}"] = value
            row[f"delta_{key}"] = value - original_metrics[key]

        rows.append(row)

    return rows


def write_csv(rows, path):
    fieldnames = list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def aggregate_rows(rows):
    numeric_keys = [key for key in rows[0].keys() if key != "file"]
    summary = {"count": len(rows)}
    for key in numeric_keys:
        values = np.array([row[key] for row in rows], dtype=np.float64)
        summary[f"mean_{key}"] = float(values.mean())
        summary[f"min_{key}"] = float(values.min())
        summary[f"max_{key}"] = float(values.max())
    return summary


def select_samples(rows):
    preferred = ["2.png"]
    sorted_rows = sorted(rows, key=lambda row: row["original_brightness"])
    quantile_indices = [
        0,
        len(sorted_rows) // 3,
        (2 * len(sorted_rows)) // 3,
        len(sorted_rows) - 1,
    ]

    samples = []
    seen = set()
    for file_name in preferred:
        if any(row["file"] == file_name for row in sorted_rows):
            seen.add(file_name)
            samples.append(file_name)

    for index in quantile_indices:
        file_name = sorted_rows[index]["file"]
        if file_name not in seen:
            seen.add(file_name)
            samples.append(file_name)

    return samples[:4]


def save_sample_comparison(rows, sample_files):
    fig, axes = plt.subplots(
        len(sample_files), 2, figsize=(10, 3.6 * len(sample_files))
    )
    if len(sample_files) == 1:
        axes = np.array([axes])

    row_lookup = {row["file"]: row for row in rows}

    for axis_row, file_name in zip(axes, sample_files):
        original = cv2.cvtColor(
            load_image(os.path.join(INPUT_DIR, file_name)), cv2.COLOR_BGR2RGB
        )
        enhanced = cv2.cvtColor(
            load_image(os.path.join(OUTPUT_DIR, file_name)), cv2.COLOR_BGR2RGB
        )
        row = row_lookup[file_name]

        axis_row[0].imshow(original)
        axis_row[0].set_title(
            f"Original {file_name}\nBrightness {row['original_brightness']:.1f}, Contrast {row['original_contrast']:.1f}",
            fontsize=10,
        )
        axis_row[0].axis("off")

        axis_row[1].imshow(enhanced)
        axis_row[1].set_title(
            f"Enhanced {file_name}\nBrightness {row['enhanced_brightness']:.1f}, Contrast {row['enhanced_contrast']:.1f}",
            fontsize=10,
        )
        axis_row[1].axis("off")

    fig.suptitle(
        "Representative Low-Light Enhancement Results", fontsize=16, fontweight="bold"
    )
    plt.tight_layout()
    output_path = os.path.join(FIGURE_DIR, "sample_comparisons.png")
    plt.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return output_path


def save_metric_plot(rows):
    metrics = ["brightness", "contrast", "entropy", "sharpness"]
    titles = ["Mean Brightness", "Global Contrast", "Entropy", "Laplacian Sharpness"]
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    axes = axes.ravel()

    for axis, metric, title in zip(axes, metrics, titles):
        original_values = [row[f"original_{metric}"] for row in rows]
        enhanced_values = [row[f"enhanced_{metric}"] for row in rows]
        axis.bar(
            [0, 1],
            [np.mean(original_values), np.mean(enhanced_values)],
            color=["#4C78A8", "#F58518"],
        )
        axis.set_xticks([0, 1], ["Original", "Enhanced"])
        axis.set_title(title)
        axis.grid(axis="y", alpha=0.25)

    fig.suptitle("Dataset-Level Quality Metrics", fontsize=16, fontweight="bold")
    plt.tight_layout()
    output_path = os.path.join(FIGURE_DIR, "dataset_metrics.png")
    plt.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return output_path


def save_runtime_gamma_plot(rows):
    brightness = np.array([row["original_brightness"] for row in rows])
    gamma = np.array([row["gamma_max"] for row in rows])
    runtime = np.array([row["runtime_s"] for row in rows])
    pixels = np.array([row["pixels"] for row in rows]) / 1e6

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    axes[0].scatter(brightness, gamma, color="#54A24B", alpha=0.8)
    axes[0].set_title("Auto-Tuned Gamma vs. Input Brightness")
    axes[0].set_xlabel("Original Brightness")
    axes[0].set_ylabel("Tuned Gamma Max")
    axes[0].grid(alpha=0.25)

    axes[1].scatter(pixels, runtime, color="#E45756", alpha=0.8)
    axes[1].set_title("Runtime vs. Image Size")
    axes[1].set_xlabel("Image Size (megapixels)")
    axes[1].set_ylabel("Runtime (s)")
    axes[1].grid(alpha=0.25)

    fig.suptitle(
        "Adaptive Parameter and Runtime Behavior", fontsize=16, fontweight="bold"
    )
    plt.tight_layout()
    output_path = os.path.join(FIGURE_DIR, "runtime_and_gamma.png")
    plt.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return output_path


def format_markdown_table(headers, rows):
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n"


def write_markdown_tables(rows, summary, sample_files):
    aggregate_headers = ["Metric", "Original Mean", "Enhanced Mean", "Delta"]
    aggregate_rows = []
    for metric in ["brightness", "contrast", "entropy", "sharpness"]:
        aggregate_rows.append(
            [
                metric.title(),
                f"{summary[f'mean_original_{metric}']:.3f}",
                f"{summary[f'mean_enhanced_{metric}']:.3f}",
                f"{summary[f'mean_delta_{metric}']:.3f}",
            ]
        )

    sample_headers = [
        "Image",
        "Brightness Gain",
        "Contrast Gain",
        "Entropy Gain",
        "Tuned Gamma",
        "Runtime (s)",
    ]
    lookup = {row["file"]: row for row in rows}
    sample_rows = []
    for file_name in sample_files:
        row = lookup[file_name]
        sample_rows.append(
            [
                file_name,
                f"{row['delta_brightness']:.2f}",
                f"{row['delta_contrast']:.2f}",
                f"{row['delta_entropy']:.2f}",
                f"{row['gamma_max']:.2f}",
                f"{row['runtime_s']:.3f}",
            ]
        )

    with open(
        os.path.join(TABLE_DIR, "aggregate_summary.md"), "w", encoding="utf-8"
    ) as file:
        file.write(format_markdown_table(aggregate_headers, aggregate_rows))

    with open(
        os.path.join(TABLE_DIR, "sample_summary.md"), "w", encoding="utf-8"
    ) as file:
        file.write(format_markdown_table(sample_headers, sample_rows))


def write_report_numbers(summary, sample_files):
    lines = [
        f"dataset_count={summary['count']}",
        f"mean_original_brightness={summary['mean_original_brightness']:.6f}",
        f"mean_enhanced_brightness={summary['mean_enhanced_brightness']:.6f}",
        f"mean_delta_brightness={summary['mean_delta_brightness']:.6f}",
        f"mean_original_contrast={summary['mean_original_contrast']:.6f}",
        f"mean_enhanced_contrast={summary['mean_enhanced_contrast']:.6f}",
        f"mean_delta_contrast={summary['mean_delta_contrast']:.6f}",
        f"mean_original_entropy={summary['mean_original_entropy']:.6f}",
        f"mean_enhanced_entropy={summary['mean_enhanced_entropy']:.6f}",
        f"mean_delta_entropy={summary['mean_delta_entropy']:.6f}",
        f"mean_original_sharpness={summary['mean_original_sharpness']:.6f}",
        f"mean_enhanced_sharpness={summary['mean_enhanced_sharpness']:.6f}",
        f"mean_delta_sharpness={summary['mean_delta_sharpness']:.6f}",
        f"mean_runtime_s={summary['mean_runtime_s']:.6f}",
        f"min_runtime_s={summary['min_runtime_s']:.6f}",
        f"max_runtime_s={summary['max_runtime_s']:.6f}",
        f"mean_gamma_max={summary['mean_gamma_max']:.6f}",
        f"min_gamma_max={summary['min_gamma_max']:.6f}",
        f"max_gamma_max={summary['max_gamma_max']:.6f}",
        f"sample_files={','.join(sample_files)}",
    ]
    with open(
        os.path.join(TABLE_DIR, "report_numbers.txt"), "w", encoding="utf-8"
    ) as file:
        file.write("\n".join(lines) + "\n")


def main():
    ensure_dirs()
    image_files = get_image_list()
    generate_demo_figure()
    rows = collect_dataset_rows(image_files)
    summary = aggregate_rows(rows)
    sample_files = select_samples(rows)

    write_csv(rows, os.path.join(TABLE_DIR, "dataset_metrics.csv"))
    save_sample_comparison(rows, sample_files)
    save_metric_plot(rows)
    save_runtime_gamma_plot(rows)
    write_markdown_tables(rows, summary, sample_files)
    write_report_numbers(summary, sample_files)

    print(f"Generated report assets for {len(rows)} images in {ASSET_DIR}")


if __name__ == "__main__":
    main()
