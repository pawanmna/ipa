---

# 📄 Low-Light Image Enhancement using Gamma Correction Prior in Mixed Color Spaces

*(Detailed Technical Markdown for Implementation)*

**Paper Source:** 

---

# 1. 📌 Problem Definition

Low-light images suffer from:

* Low contrast
* Poor visibility
* Narrow dynamic range
* Color distortion

Goal:

> Enhance brightness, contrast, and details **without amplifying noise** and while keeping computation efficient.

---

# 2. 🧠 Core Idea

The paper proposes:

* Use **Atmospheric Scattering Model (ASM)** (borrowed from dehazing)
* Apply it on **inverted low-light images**
* Estimate **transmission map** using:

  * Mixed color spaces (**HSI + HSV**)
  * **Gamma Correction Prior (GCP)**
* Introduce **pixel-adaptive gamma**

---

# 3. 🌫️ Atmospheric Scattering Model (ASM)

## 3.1 Model Formulation

For inverted image:

[
1 - I(x) = (1 - J(x)) t(x) + A (1 - t(x))
]

Where:

* ( I(x) ): input (low-pass filtered)
* ( J(x) ): desired enhanced image
* ( A ): atmospheric light
* ( t(x) ): transmission map

---

## 3.2 Recovering Image

[
J(x) = \frac{O(x) - 1 + A}{t(x)} + 1 - A
]

👉 Key problem: **estimate ( t(x) )** accurately.

---

# 4. 🔍 Transmission Map Estimation

## 4.1 Normalize ASM

[
L(x) = \frac{1 - I(x)}{A}, \quad R(x) = \frac{1 - J(x)}{A}
]

[
L(x) = R(x) t(x) + 1 - t(x)
]

---

## 4.2 Using Max Channel

[
t(x) = 1 - \frac{M_L(x)}{1 - M_R(x)}
]

Where:

* ( M_L(x) = \max_c L(x) )
* ( M_R(x) = \max_c R(x) )

---

# 5. 🎨 Saturation-Based Modeling

## 5.1 HSI Saturation

[
S^{HSI}_R(x) = 1 - \frac{m_R(x)}{\mu_R(x)}
]

## 5.2 HSV Saturation

[
S^{HSV}_R(x) = 1 - \frac{m_R(x)}{M_R(x)}
]

---

## 5.3 Combine Relations

[
M_R(x) = \mu_R(x) \cdot \frac{1 - S^{HSI}_R(x)}{1 - S^{HSV}_R(x)}
]

Similarly:

[
M_L(x) = \mu_L(x) \cdot \frac{1 - S^{HSI}_L(x)}{1 - S^{HSV}_L(x)}
]

---

## 5.4 Final Transmission (Closed Form)

[
t(x) =
\frac{
1 - \mu_L(x) \cdot \frac{1 - S^{HSI}_L(x)}{1 - S^{HSV}_L(x)}
}{
1 - \mu_R(x) \cdot \frac{1 - S^{HSI}_R(x)}{1 - S^{HSV}_R(x)}
}
]

---

## ⚠️ Problem:

Estimating saturation terms directly is difficult.

---

# 6. ⚡ Gamma Correction Prior (GCP)

## 6.1 Idea

Use **gamma correction on inverted image**:

[
V(x) = L(x)^{\Gamma}
]

Where:

* ( \Gamma ): gamma value
* ( V(x) ): virtual image

---

## 6.2 Approximation

[
\mu_R(x) \approx \mu_V(x)
]
[
M_R(x) \approx M_V(x)
]

---

## 6.3 Final Transmission Estimate

[
t(x) \approx
\frac{
1 - \mu_L(x)
}{
M_L(x)\mu_V(x) - \mu_L(x)M_V(x)
}
]

---

# 7. 🔧 Image Reconstruction

[
\tilde{J}(x) =
\frac{
O(x) - 1 + A
}{
\max(t(x), t_0)
}

* 1 - A
  ]

Where:

* ( t_0 = 0.1 ) (avoid division by zero)

---

# 8. 🎯 Pixel-Adaptive Gamma

## 8.1 Motivation

* Fixed ( \Gamma ) causes:

  * Over-enhancement
  * Under-enhancement

---

## 8.2 Adaptive Gamma

[
\Gamma(x) = a e^{-M_O(x)} + b
]

Where:

* ( M_O(x) = \max_c O(x) )

---

## 8.3 Coefficients

[
a = \frac{\Gamma_{max} - 1}{1 - e^{-1}}
]

[
b = \Gamma_{max} - a
]

Typical:
[
\Gamma_{max} = 6
]

---

# 9. 🧩 Complete Algorithm Pipeline

## Step-by-step

### 1. Input

* Low-light image ( O(x) )

---

### 2. Denoising

* Apply Gaussian blur (7×7)

---

### 3. Inversion

[
L(x) = 1 - I(x)
]

---

### 4. Estimate Atmospheric Light ( A )

---

### 5. Compute Gamma Map

* Use adaptive formula

---

### 6. Virtual Image

[
V(x) = L(x)^{\Gamma(x)}
]

---

### 7. Compute Statistics

* ( \mu_L(x), M_L(x) )
* ( \mu_V(x), M_V(x) )

---

### 8. Estimate Transmission

[
t(x)
]

---

### 9. Recover Image

[
J(x)
]

---

### 10. Clip Values

* Ensure valid pixel range

---

# 10. ⚙️ Computational Complexity

* No training required
* No iterative refinement
* Closed-form solution

➡️ Very fast compared to:

* Retinex methods
* Deep learning models

---

# 11. 📊 Evaluation Metrics

## Full-reference:

* **PSNR**
* **SSIM**
* **CIEDE2000**

## No-reference:

* **NIQE**
* **BRISQUE**
* **NIQMC**

---

