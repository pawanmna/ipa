import cv2
import matplotlib.pyplot as plt
import os

from Run_LowLight_Image_Enhancement_Pixel_Adaptive import enhance_image, f2i


def compute_histogram(image):
    hist_b = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([image], [2], None, [256], [0, 256])
    return hist_b, hist_g, hist_r


def demo_enhancement(image_path, output_dir="demo_output"):
    os.makedirs(output_dir, exist_ok=True)

    InputImg = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if InputImg is None:
        print(f"Error: Could not load image from {image_path}")
        return

    print("Running enhancement...")
    EnhancedImg, details = enhance_image(InputImg, gamma_max=6.0, return_details=True)

    EnhancedImg_uint8 = f2i(EnhancedImg)
    gamma_map = details["gamma_map"]
    transmap = details["transmission_map"]

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle(
        "Low-Light Image Enhancement Demonstration", fontsize=16, fontweight="bold"
    )

    original_rgb = cv2.cvtColor(InputImg, cv2.COLOR_BGR2RGB)
    enhanced_rgb = cv2.cvtColor(EnhancedImg_uint8, cv2.COLOR_BGR2RGB)

    axes[0, 0].imshow(original_rgb)
    axes[0, 0].set_title("Original Low-Light Image", fontsize=12)
    axes[0, 0].axis("off")

    axes[0, 1].imshow(enhanced_rgb)
    axes[0, 1].set_title("Enhanced Result", fontsize=12)
    axes[0, 1].axis("off")

    gamma_display = gamma_map
    gamma_span = max(gamma_display.max() - gamma_display.min(), 1e-6)
    gamma_normalized = (gamma_display - gamma_display.min()) / gamma_span
    axes[0, 2].imshow(gamma_normalized, cmap="jet")
    axes[0, 2].set_title(
        "Pixel-Adaptive Gamma Map\n(Dark=High Gamma, Bright=Low Gamma)", fontsize=12
    )
    axes[0, 2].axis("off")
    plt.colorbar(axes[0, 2].images[0], ax=axes[0, 2], fraction=0.046, pad=0.04)

    hist_b, hist_g, hist_r = compute_histogram(InputImg)
    axes[1, 0].plot(hist_b, color="b", label="Blue", alpha=0.7)
    axes[1, 0].plot(hist_g, color="g", label="Green", alpha=0.7)
    axes[1, 0].plot(hist_r, color="r", label="Red", alpha=0.7)
    axes[1, 0].set_title("Original Histogram\n(Compressed/Low Contrast)", fontsize=12)
    axes[1, 0].set_xlabel("Pixel Intensity")
    axes[1, 0].set_ylabel("Frequency")
    axes[1, 0].legend()
    axes[1, 0].set_xlim([0, 256])

    hist_b_enh, hist_g_enh, hist_r_enh = compute_histogram(EnhancedImg_uint8)
    axes[1, 1].plot(hist_b_enh, color="b", label="Blue", alpha=0.7)
    axes[1, 1].plot(hist_g_enh, color="g", label="Green", alpha=0.7)
    axes[1, 1].plot(hist_r_enh, color="r", label="Red", alpha=0.7)
    axes[1, 1].set_title("Enhanced Histogram\n(Spread/Improved Contrast)", fontsize=12)
    axes[1, 1].set_xlabel("Pixel Intensity")
    axes[1, 1].set_ylabel("Frequency")
    axes[1, 1].legend()
    axes[1, 1].set_xlim([0, 256])

    axes[1, 2].imshow(transmap, cmap="viridis")
    axes[1, 2].set_title("Transmission Map", fontsize=12)
    axes[1, 2].axis("off")
    plt.colorbar(axes[1, 2].images[0], ax=axes[1, 2], fraction=0.046, pad=0.04)

    plt.tight_layout()

    output_path = os.path.join(output_dir, "demo_result.png")
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"Demo saved to: {output_path}")

    plt.show()

    print(
        "Auto-tuned gamma_max=%.2f, denoise_h=%d, scale=%.2f"
        % (
            details["gamma_max"],
            details["denoise_h"],
            details["processing_scale"],
        )
    )

    return EnhancedImg_uint8, gamma_map


if __name__ == "__main__":
    input_dir = os.path.join("inputi", "input")
    image_files = [f for f in os.listdir(input_dir) if f.endswith(".png")]

    if image_files:

        #sample_image = os.path.join(input_dir, image_files[0])
        sample_image = "inputi\input\demo.png"
        print(f"Processing: {sample_image}")
        enhanced_img, gamma_map = demo_enhancement(sample_image)

        print("\n=== Enhancement Complete ===")
        print("Key observations:")
        print(
            "1. Original: Low contrast, compressed histogram, loss of details in dark regions"
        )
        print(
            "2. Enhanced: Expanded dynamic range, improved brightness, restored details"
        )
        print(
            "3. Gamma Map: Darker regions have higher gamma values (brighter after correction)"
        )
        print("4. Histogram: Shows spreading indicating improved contrast")
    else:
        print("No images found in input directory")
