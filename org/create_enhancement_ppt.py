from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)


def add_title_slide(title, subtitle):
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(2.5), Inches(12.333), Inches(1.5)
    )
    title_frame = title_box.text_frame
    title_para = title_frame.paragraphs[0]
    title_para.text = title
    title_para.font.size = Pt(44)
    title_para.font.bold = True
    title_para.alignment = PP_ALIGN.CENTER

    subtitle_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(4), Inches(12.333), Inches(1)
    )
    subtitle_frame = subtitle_box.text_frame
    subtitle_para = subtitle_frame.paragraphs[0]
    subtitle_para.text = subtitle
    subtitle_para.font.size = Pt(24)
    subtitle_para.alignment = PP_ALIGN.CENTER


def add_content_slide(title, bullets):
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.3), Inches(12.333), Inches(1)
    )
    title_frame = title_box.text_frame
    title_para = title_frame.paragraphs[0]
    title_para.text = title
    title_para.font.size = Pt(36)
    title_para.font.bold = True

    content_box = slide.shapes.add_textbox(
        Inches(0.7), Inches(1.3), Inches(12), Inches(5.5)
    )
    content_frame = content_box.text_frame
    content_frame.word_wrap = True

    for bullet in bullets:
        p = (
            content_frame.paragraphs[0]
            if not content_frame.paragraphs
            else content_frame.add_paragraph()
        )
        p.text = bullet
        p.font.size = Pt(22)
        p.space_after = Pt(12)


add_title_slide(
    "Low-Light Image Enhancement: Enhancements",
    "Improved Denoising, Auto-Tuning, and Performance Optimization",
)

add_content_slide(
    "Original Work Overview",
    [
        "Published in Pattern Recognition journal (2023)",
        "Transforms low-light problem into image dehazing problem",
        "Uses gamma correction prior in mixed color spaces",
        "Pixel-adaptive gamma correction for individual pixel brightness",
        "Based on Dark Channel Prior from dehazing research",
    ],
)

add_content_slide(
    "Original Pipeline Summary",
    [
        "1. Load image and convert to floating point (0-1 range)",
        "2. Apply Gaussian blur for basic denoising",
        "3. Compute atmospheric light using Dark Channel Prior",
        "4. Normalize image by dividing with atmospheric light",
        "5. Apply fixed gamma_max=6.0 for all images",
        "6. Estimate transmission map and recover enhanced image",
    ],
)

add_content_slide(
    "Limitations of Original Approach",
    [
        "Gaussian blur denoising: Too weak for noisy low-light images",
        "Fixed gamma_max=6.0: May over/under-enhance depending on image",
        "No consideration for image-specific noise levels",
        "No brightness-adaptive parameter tuning",
        "Processing speed not optimized for large images",
    ],
)

add_content_slide(
    "Enhancement 1: Improved Noise Removal",
    [
        "Combined Non-Local Means + Edge-Preserving Bilateral Filter",
        "Automatic noise level estimation per image",
        "Adaptive denoising strength based on image characteristics",
        "Parameters: denoise_h auto-tuned (5-22), bilateral filter applied",
        "Reduces noise without flattening image structure",
    ],
)

add_content_slide(
    "Enhancement 2: Automatic Parameter Tuning",
    [
        "gamma_max now acts as upper bound, not fixed value",
        "Per-image brightness and contrast analysis",
        "Darkness factor calculated from histogram analysis",
        "Noise factor from Laplacian variance estimation",
        "Gamma auto-tuned between 1.0 and gamma_max per image",
    ],
)

add_content_slide(
    "Enhancement 3: Faster Processing",
    [
        "Replaced skimage.morphology.erosion with cv2.erode",
        "Removed Python channel loops - vectorized operations",
        "Large image optimization: downsample estimation branch",
        "Target resolution ~960K pixels for speed without quality loss",
        "OpenCV optimizations enabled",
    ],
)

add_content_slide(
    "Technical: Noise Estimation",
    [
        "Uses Laplacian high-pass filter for noise detection",
        "Variance of Laplacian indicates noise level",
        "Formula: sigma = MAD(Laplacian) / 0.6745",
        "Results in noise_factor [0, 1] range",
        "Combined with darkness_factor for adaptive denoising",
    ],
)

add_content_slide(
    "Technical: Auto Gamma Tuning",
    [
        "gamma_max is now a cap, not a fixed value",
        "darkness_factor = 1 - mean_intensity",
        "tuned_gamma = 1.0 + gamma_drive * darkness_factor",
        "gamma_drive = noise_factor + 0.5 * darkness_factor",
        "Always ensures some enhancement (minimum ~1.15)",
    ],
)

add_content_slide(
    "Technical: Speed Optimization",
    [
        "INTER_AREA downsampling for quality preservation",
        "Scale factor = sqrt(960000 / total_pixels) if large",
        "Transmap resized back to full resolution after estimation",
        "Parallel-friendly code structure (ThreadPoolExecutor ready)",
        "cv2.setUseOptimized(True) for faster OpenCV operations",
    ],
)

add_content_slide(
    "Performance Results",
    [
        "Sample image (400x600): ~0.49 seconds processing",
        "Auto-tuned parameters logged per image",
        "gamma_max=5.28 instead of fixed 6.0 (per-image adaptation)",
        "denoise_h=14 (adapted to noise level)",
        "scale=1.0 for small images (no downsampling needed)",
    ],
)

add_content_slide(
    "Backward Compatibility",
    [
        "Default gamma_max=6.0 preserved",
        "Existing CLI commands work unchanged",
        "enhance_image(img, 6.0) behaves as before if desired",
        "return_details=False maintains original interface",
        "All original parameters still configurable",
    ],
)

add_content_slide(
    "Summary of Improvements",
    [
        "Better denoising: Combined NLM + bilateral, auto-tuned strength",
        "Smarter parameters: Per-image gamma adaptation",
        "Faster execution: Vectorization + large image optimization",
        "Maintains compatibility with existing workflows",
        "Prints tuned parameters for transparency",
    ],
)

add_title_slide("Questions?", "Low-Light Image Enhancement Enhancements")

prs.save("Enhancement_Presentation.pptx")
print("Enhancement presentation saved successfully!")
