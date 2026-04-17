# IEEE-Style Project Report

## Low-Light Image Enhancement Using Pixel-Adaptive Gamma Correction with Practical Denoising, Auto-Tuning, and Acceleration

### Abstract
Low-light image enhancement remains important for surveillance, mobile photography, and downstream vision tasks because underexposed scenes typically suffer from poor contrast, limited detail visibility, and amplified sensor noise. This project implements a low-light enhancement pipeline derived from pixel-adaptive gamma correction and a dehazing-inspired recovery model. The implementation was further improved with three practical enhancements: stronger denoising, automatic per-image parameter tuning, and a faster processing path for larger images. Evaluation on the 49 low-light images bundled with the repository shows consistent visual improvement and strong gains in no-reference image quality indicators. Mean grayscale brightness increased from `15.468` to `109.333`, mean contrast increased from `10.791` to `53.721`, and mean entropy increased from `4.904` to `7.405`. The average runtime of the upgraded implementation on the local dataset was `0.625 s` per image. Qualitative examples and dataset-level plots indicate that the modified pipeline substantially improves visibility while preserving more detail by recovering the final image from the original input rather than from the denoised guide image.

### Keywords
Low-light enhancement, gamma correction, transmission map, denoising, adaptive parameter tuning, image restoration, dehazing prior

## I. Introduction
Low-light images often exhibit low brightness, compressed dynamic range, color distortion, and visible noise. A practical enhancement method must brighten dark regions without washing out highlights or destroying fine texture. The base project in this repository approaches the problem by transforming low-light enhancement into a dehazing-style recovery task. It estimates atmospheric light from the inverted image, applies pixel-adaptive gamma correction, computes a transmission map, and reconstructs the enhanced result.

The original code was functional, but three implementation-level opportunities were clear.

1. Noise removal could be improved because dark scenes frequently contain strong chroma and luminance noise.
2. Fixed parameters such as `gamma_max` are not ideal across images with different exposure and contrast characteristics.
3. The runtime path could be simplified and partially downscaled for better throughput on larger datasets.

This report documents the upgraded implementation and summarizes both qualitative and quantitative results on the repository input set.

## II. Project Overview
The core enhancement pipeline is implemented in `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py`. The visualization wrapper in `demo_enhancement.py` now imports the same core `enhance_image(...)` function instead of duplicating the algorithm. This creates a single source of truth for batch execution, demonstrations, and analysis.

The upgraded pipeline has the following stages.

1. Estimate image brightness, contrast, and noise level.
2. Auto-tune denoising strength and the effective upper bound for gamma correction.
3. Denoise the image only for illumination and transmission estimation.
4. Invert and normalize the guide image, then estimate atmospheric light.
5. Apply pixel-adaptive gamma correction and estimate the transmission map.
6. Recover the final enhanced image from the original input to preserve detail.
7. Apply percentile-based range adjustment for final contrast stretching.

## III. Methodology
### A. Baseline Formulation
The project follows a dehazing-inspired view of low-light enhancement. Let `I` be the low-light input, `A` the estimated atmospheric light, and `t` the transmission map. The recovered image is computed channel-wise by reversing the scattering-style model after applying pixel-adaptive gamma correction to the normalized inverted image.

### B. Stronger Noise Removal
The denoising stage was upgraded to better stabilize atmospheric light and transmission estimation.

1. Noise level is estimated from the median absolute Laplacian response on the grayscale input.
2. `fastNlMeansDenoisingColored` is auto-tuned based on the estimated noise and scene darkness.
3. A bilateral filtering stage is added when the scene is especially noisy or dark.
4. For large images, the denoising prior can be estimated at reduced resolution and blended with an edge-preserving result.

An important final correction was also applied after visual review: the recovered image is produced from the original input, not the denoised image. This avoids the overly smooth appearance that can occur when denoising is carried into the final reconstruction.

### C. Automatic Parameter Tuning
The implementation no longer treats `gamma_max` as a fixed global constant. Instead, it uses the user-provided value as an upper bound and computes an image-specific effective gamma limit from the following cues.

1. Mean brightness, which captures overall darkness.
2. Contrast, which indicates how compressed the dynamic range is.
3. Estimated noise level, which acts as a penalty against overly aggressive enhancement.

The tuning logic increases gamma for darker, flatter images and reduces it for relatively brighter inputs. Across the repository dataset, the tuned gamma ranged from `5.279` to `6.000`, with a mean of `5.749`.

### D. Faster Processing Path
Three direct runtime improvements were integrated.

1. Python channel loops were replaced with vectorized NumPy expressions.
2. `skimage.morphology.erosion` was replaced with `cv2.erode` in the dark-channel step.
3. Only the expensive estimation branch is downscaled for large images, after which the transmission and gamma maps are resized back to full resolution.

These changes keep the implementation simple while improving scalability.

## IV. Experimental Setup
### A. Data
The repository input folder `input/` contains `49` low-light images used for this report.

### B. Software Environment
The implementation uses Python with OpenCV, NumPy, and Matplotlib. The analysis assets for this report were generated by `generate_ieee_report_assets.py`.

### C. Evaluation Protocol
Because no paired ground-truth bright images are included in the repository, evaluation was performed with no-reference indicators and visual inspection.

1. Brightness: mean grayscale intensity.
2. Contrast: grayscale standard deviation.
3. Entropy: information content from the grayscale histogram.
4. Sharpness: variance of the Laplacian.
5. Runtime: wall-clock runtime reported by the enhancement function.

The per-image measurements are available in `report_assets/tables/dataset_metrics.csv`.

## V. Qualitative Results
Figure 1 shows the demo visualization generated from the project demo script. It includes the original image, enhanced result, adaptive gamma map, histograms, and the transmission map.

![Figure 1. Demo visualization generated by the project demo.](report_assets/figures/demo_result.png)

Figure 2 presents representative sample comparisons from the dataset. The selected images span darker and relatively brighter low-light cases in order to show how the auto-tuned enhancement adapts across the set.

![Figure 2. Representative original and enhanced image comparisons.](report_assets/figures/sample_comparisons.png)

The visual results show the following trends.

1. Dark regions become significantly more readable after enhancement.
2. Contrast expansion is visible both locally and globally.
3. The adaptive gamma map assigns stronger correction to darker areas.
4. Recovering the final image from the original input preserves detail better than reconstructing from the denoised guide image.

## VI. Quantitative Results
Figure 3 summarizes average dataset-level quality metrics before and after enhancement.

![Figure 3. Dataset-level metric comparison for original and enhanced images.](report_assets/figures/dataset_metrics.png)

Figure 4 shows how the auto-tuned gamma changes with input brightness and how runtime scales with image size.

![Figure 4. Adaptive gamma and runtime behavior across the dataset.](report_assets/figures/runtime_and_gamma.png)

Table I reports the average no-reference metrics over all 49 images.

| Metric | Original Mean | Enhanced Mean | Delta |
| --- | --- | --- | --- |
| Brightness | 15.468 | 109.333 | 93.865 |
| Contrast | 10.791 | 53.721 | 42.930 |
| Entropy | 4.904 | 7.405 | 2.501 |
| Sharpness | 58.974 | 5706.727 | 5647.752 |

Table II reports representative per-image results for four selected samples.

| Image | Brightness Gain | Contrast Gain | Entropy Gain | Tuned Gamma | Runtime (s) |
| --- | --- | --- | --- | --- | --- |
| 2.png | 71.42 | 38.04 | 1.97 | 5.28 | 0.604 |
| 28.png | 75.42 | 44.69 | 3.65 | 6.00 | 0.529 |
| 63.png | 93.63 | 40.31 | 2.67 | 5.89 | 0.679 |
| 13.png | 133.27 | 40.83 | 2.28 | 5.77 | 0.638 |

The average runtime was `0.625 s` per image, with a minimum of `0.529 s` and a maximum of `0.682 s` on the evaluation set.

## VII. Discussion
The results confirm that the project enhancements improved both practicality and output quality.

1. The stronger denoising stage stabilizes light estimation in dark scenes.
2. Automatic gamma tuning removes the need to manually select a single `gamma_max` for every image.
3. Vectorization and reduced-resolution estimation improve efficiency without changing the overall algorithm design.
4. Reconstructing the final result from the original input avoids unnecessary smoothing and yields a more natural result.

There are also limits to the present evaluation.

1. The metrics are no-reference and do not directly measure perceptual fidelity against ground truth.
2. The sharpness increase partly reflects stronger edges and contrast, so it should be interpreted together with visual inspection.
3. The repository dataset is relatively small and appears to contain similarly sized images, which constrains runtime variation.

## VIII. Conclusion
This project demonstrates a practical low-light enhancement system built on pixel-adaptive gamma correction and dehazing-inspired recovery. Three targeted implementation upgrades were added: stronger denoising, automatic parameter tuning, and faster processing. Evaluation on the repository dataset shows strong improvements in brightness, contrast, and entropy while maintaining visually stronger detail by recovering the final image from the original low-light input. The resulting codebase is more consistent, easier to analyze, and better suited for both demo use and batch processing.

## References
[1] J. J. Jeon, J. Y. Park, and I. K. Eom, "Low-Light Image Enhancement Using Gamma Correction Prior in Mixed Color Spaces," *Pattern Recognition*, 2023. doi: `10.1016/j.patcog.2023.110001`.

[2] Project implementation files: `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py`, `demo_enhancement.py`, and generated analysis assets under `report_assets/`.
