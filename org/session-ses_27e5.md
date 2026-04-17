# Project enhancements for denoising and speed

**Session ID:** ses_27e5c7f4effebmqeuQ9jc6JZOf
**Created:** 4/12/2026, 5:51:09 PM
**Updated:** 4/12/2026, 6:23:30 PM

---

## User

do these enhancements to this project 1. Better noise removal
   Low-light images usually contain noise, so adding a stronger denoising step could improve output quality.
2. Automatic parameter tuning
   The algorithm uses fixed values like gamma_max. These could be adjusted automatically based on each image.
3. Faster processing
   The implementation could be optimized for larger datasets or real-time use. do these 

---

## Assistant (Build · GPT-5.4 · 12.2s)

_Thinking:_

**Planning project modifications**

I need to modify the project accordingly, which requires inspecting the codebase. Since this is a complex multi-step process, I should use a to-do list to keep track. Before doing any substantial work, it's important to send a commentary about the changes. I'll need to inspect files using methods like glob, grep, or read, perhaps even in parallel. Let’s get that to-do list together so I can tackle this efficiently!

I’m inspecting the enhancement pipeline to find where denoising, parameter selection, and runtime are implemented before I change anything.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Inspect current low-light enhancement pipeline and identify denoising, parameter, and performance hotspots",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Implement stronger noise removal with minimal disruption to existing pipeline",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Add automatic per-image parameter tuning for enhancement settings",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Optimize processing path for better throughput on larger inputs",
      "status": "pending",
      "priority": "medium"
    },
    {
      "content": "Run available verification commands or sample execution to validate changes",
      "status": "pending",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Inspect current low-light enhancement pipeline and identify denoising, parameter, and performance hotspots",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Implement stronger noise removal with minimal disruption to existing pipeline",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Add automatic per-image parameter tuning for enhancement settings",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Optimize processing path for better throughput on larger inputs",
    "status": "pending",
    "priority": "medium"
  },
  {
    "content": "Run available verification commands or sample execution to validate changes",
    "status": "pending",
    "priority": "high"
  }
]
```

---

## Assistant (Build · GPT-5.4 · 7.8s)

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/*",
  "path": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org"
}
```

**Output:**
```
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\Run_LowLight_Image_Enhancement_Pixel_Adaptive.py
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\demo_enhancement.py
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\Low_Light_Image_Enhancement_Presentation.pptx
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\create_ppt.py
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\README.md
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\52.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\52.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\46.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\46.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\47.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\47.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\53.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\53.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\45.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\45.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\51.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\51.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\50.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\50.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\2.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\2.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\44.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\44.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\40.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\40.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\6.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\6.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\54.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\54.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\68.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\68.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\69.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\69.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\57.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\5.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\5.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\43.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\43.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\42.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\42.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\56.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\56.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\25.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\25.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\24.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\24.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\18.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\18.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\26.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\26.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\33.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\33.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\27.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\27.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\36.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\36.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\21.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\21.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\35.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\35.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\487.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\38.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\38.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\10.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\10.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\39.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\39.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\13.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\13.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\12.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\12.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\16.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\16.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\17.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\17.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\15.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\15.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\28.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\28.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\14.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\14.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\9.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\9.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\67.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\67.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\58.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\64.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\64.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\59.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\59.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\61.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\61.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\48.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\48.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\60.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\60.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\62.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\62.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\input\63.png
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input\63.png

(Results are truncated: showing first 100 results. Consider using a more specific path or pattern.)
```

**Tool: grep**

**Input:**
```json
{
  "pattern": "gamma_max|denois|noise|enhance|low.?light|guided|retinex",
  "path": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org",
  "include": "*.*"
}
```

**Output:**
```
Found 36 matches
D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\Run_LowLight_Image_Enhancement_Pixel_Adaptive.py:
  Line 23:     "--gamma_max", dest="gamma_max", type=float, default=6.0, help="gamma_max value"
  Line 116: def EstimateTransmission(InputImg, NormImg, gamma_max=6):
  Line 122:     GCImg = PixelAdaptiveGamma(InputImg, NormImg, gamma_max)
  Line 176: def main(InputImg, gamma_max):
  Line 181:     denoised = cv2.fastNlMeansDenoisingColored(InputImg, None, 10, 10, 7, 21)
  Line 182:     DenoiseImg = 1.0 - i2f(denoised)
  Line 186:     A = Compute_A_Tang(DenoiseImg)
  Line 188:         NormImg[:, :, ind] = DenoiseImg[:, :, ind] / A[0, ind]
  Line 191:     Transmap = EstimateTransmission(float_image, NormImg, gamma_max)
  Line 223:         OutputImg = main(InputImg, args.gamma_max)

D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\demo_enhancement.py:
  Line 80: def EstimateTransmission(InputImg, NormImg, gamma_max=6):
  Line 86:     GCImg, gamma = PixelAdaptiveGamma(InputImg, NormImg, gamma_max)
  Line 128: def enhance_image(InputImg, gamma_max=6.0):
  Line 131:     DenoiseImg = 1.0 - cv2.GaussianBlur(float_image, (7, 7), 0)
  Line 133:     A = Compute_A_Tang(DenoiseImg)
  Line 135:         NormImg[:, :, ind] = DenoiseImg[:, :, ind] / A[0, ind]
  Line 138:     Transmap, gamma_map = EstimateTransmission(float_image, NormImg, gamma_max)
  Line 153: def demo_enhancement(image_path, output_dir="demo_output"):
  Line 161:     print("Running enhancement...")
  Line 162:     EnhancedImg, gamma_map, transmap = enhance_image(InputImg, gamma_max=6.0)
  Line 172:     enhanced_rgb = cv2.cvtColor(EnhancedImg_uint8, cv2.COLOR_BGR2RGB)
  Line 178:     axes[0, 1].imshow(enhanced_rgb)
  Line 235:         enhanced_img, gamma_map = demo_enhancement(sample_image)

D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\create_ppt.py:
  Line 69:         "This project implements a low-light image enhancement technique",
  Line 71:         "Key idea: Transform low-light problem into image dehazing problem",
  Line 93:         "Gaussian blur applied to create a denoised version",
  Line 94:         "This denoised image helps in accurate light estimation",
  Line 128:         "Gamma ranges from 1 (no change) to gamma_max (maximum adjustment)",
  Line 173:         "6. Recover enhanced image using transmission",
  Line 175:         "8. Save the enhanced output image",
  Line 193:         "gamma_max: Controls maximum gamma correction (default: 6.0)",
  Line 205:         "Optional gamma_max parameter for tuning brightness",
  Line 207:         "Saves enhanced images as PNG files",

D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\README.md:
  Line 22:     --gamma_max=6                               # defaults gamma_max=6
  Line 24: #python Run_LowLight.py --input_dir=/path/to/your/dataset/dir/ --output_dir=/path/to/save/results/ --gamma_max=6
  Line 36: Keywords: Low-light image enhancement; Inverted image; Atmospheric light; Normalization; Transmission map; Retinex model; HSV color space; HSI color space; Gamma correction   
```

---

## Assistant (Build · GPT-5.4 · 11.4s)

_Thinking:_



**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\Run_LowLight_Image_Enhancement_Pixel_Adaptive.py",
  "offset": 1,
  "limit": 260
}
```

**Output:**
```
<path>D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\Run_LowLight_Image_Enhancement_Pixel_Adaptive.py</path>
<type>file</type>
<content>
1: import numpy as np
2: import cv2
3: 
4: from skimage import morphology
5: import time
6: import os
7: import argparse
8: 
9: parser = argparse.ArgumentParser(description="")
10: parser.add_argument(
11:     "--input_dir",
12:     dest="InputPath",
13:     default="/home/ispl-public/Desktop/Dataset/LIME",
14:     help="directory for testing inputs",
15: )
16: parser.add_argument(
17:     "--output_dir",
18:     dest="OutputPath",
19:     default="./",
20:     help="directory for testing outputs",
21: )
22: parser.add_argument(
23:     "--gamma_max", dest="gamma_max", type=float, default=6.0, help="gamma_max value"
24: )
25: args = parser.parse_args()
26: 
27: """ pixel value: i2f: 0-255 to 0-1, f2i: 0-1 to 0-255 """
28: 
29: 
30: def i2f(i_image):
31:     f_image = np.float32(i_image) / 255.0
32:     return f_image
33: 
34: 
35: def f2i(f_image):
36:     i_image = np.uint8(f_image * 255.0)
37:     return i_image
38: 
39: 
40: """ Compute 'A' as described by Tang et al. (CVPR 2014) """
41: 
42: 
43: def Compute_A_Tang(im):
44:     erosion_window = 15
45:     n_bins = 200
46: 
47:     R = im[:, :, 2]
48:     G = im[:, :, 1]
49:     B = im[:, :, 0]
50: 
51:     # compute the dark channel
52:     dark = morphology.erosion(np.min(im, 2), morphology.square(erosion_window))
53: 
54:     [h, edges] = np.histogram(dark, n_bins, [0, 1])
55:     numpixel = im.shape[0] * im.shape[1]
56:     thr_frac = numpixel * 0.99
57:     csum = np.cumsum(h)
58:     nz_idx = np.nonzero(csum > thr_frac)[0][0]
59:     dc_thr = edges[nz_idx]
60:     mask = dark >= dc_thr
61:     # similar to DCP till this step
62:     # next, median of these top 0.1% pixels
63:     # median of the RGB values of the pixels in the mask
64:     rs = R[mask]
65:     gs = G[mask]
66:     bs = B[mask]
67: 
68:     A = np.zeros((1, 3))
69: 
70:     A[0, 2] = np.median(rs)
71:     A[0, 1] = np.median(gs)
72:     A[0, 0] = np.median(bs)
73: 
74:     return A
75: 
76: 
77: def GetIntensity(fi):
78:     return cv2.divide(fi[:, :, 0] + fi[:, :, 1] + fi[:, :, 2], 3)
79: 
80: 
81: def GetMax(fi):
82:     max_rgb = cv2.max(cv2.max(fi[:, :, 0], fi[:, :, 1]), fi[:, :, 2])
83:     return max_rgb
84: 
85: 
86: def GetMin(fi):
87:     min_rgb = cv2.max(cv2.min(fi[:, :, 0], fi[:, :, 1]), fi[:, :, 2])
88:     return min_rgb
89: 
90: 
91: """ Pixel Adaptive Gamma Correction """
92: 
93: 
94: def PixelAdaptiveGamma(InputImg, NormImg, amax):
95:     GCImg = np.empty(InputImg.shape, InputImg.dtype)
96:     amin = 1
97:     xmax = 1
98:     xmin = 0
99:     Imax = GetMax(InputImg)
100: 
101:     a = (amax - amin) / (np.exp(-xmin) - np.exp(-xmax))
102:     b = amax - a * np.exp(-xmin)
103:     g2 = a * np.exp(-Imax) + b
104:     g1 = np.where(Imax < xmin, amax, g2)
105:     gamma = np.where(Imax > xmax, amin, g1)
106: 
107:     for ind in range(0, 3):
108:         GCImg[:, :, ind] = NormImg[:, :, ind] ** gamma
109: 
110:     return GCImg
111: 
112: 
113: """ Estimate Transmission Map """
114: 
115: 
116: def EstimateTransmission(InputImg, NormImg, gamma_max=6):
117:     T_min = 0.1
118:     me = np.finfo(np.float32).eps
119:     hi = GetIntensity(NormImg)
120:     hmax = GetMax(NormImg)
121: 
122:     GCImg = PixelAdaptiveGamma(InputImg, NormImg, gamma_max)
123: 
124:     ji = GetIntensity(GCImg)
125:     jmax = GetMax(GCImg)
126: 
127:     tn = np.maximum(jmax * hi - hmax * ji, me)
128:     td = np.maximum((jmax - ji) * hi, me)
129: 
130:     Tmap = 1.0 - hi * (tn / td)
131: 
132:     return np.clip(Tmap, T_min, 1.0)
133: 
134: 
135: """ Recover dehazed image """
136: 
137: 
138: def Recover(im, tmap, A):
139:     res = np.empty(im.shape, im.dtype)
140:     for ind in range(0, 3):
141:         res[:, :, ind] = (im[:, :, ind] - 1.0 + A[0, ind]) / tmap + 1.0 - A[0, ind]
142: 
143:     return np.clip(res, 0.0, 1.0)
144: 
145: 
146: """ Adjust image range """
147: 
148: 
149: def Adjust(im, perh, perl):
150:     aim = np.empty(im.shape, im.dtype)
151:     im_h = np.percentile(im, perh)
152:     im_l = np.percentile(im, perl)
153:     for ind in range(0, 3):
154:         aim[:, :, ind] = (im[:, :, ind] - im_l) / (im_h - im_l)
155: 
156:     return np.clip(aim, 0.0, 1.0)
157: 
158: 
159: """ Normalize image 0 between 1 """
160: 
161: 
162: def Normalize(im):
163:     aim = np.empty(im.shape, im.dtype)
164:     for ind in range(0, 3):
165:         im_h = np.max(im[:, :, ind])
166:         im_l = np.min(im[:, :, ind])
167:         aim[:, :, ind] = (im[:, :, ind] - im_l) / (im_h - im_l)
168:         aim[:, :, ind] = np.clip(aim[:, :, ind], 0.0, 1.0)
169: 
170:     return aim
171: 
172: 
173: """ Main """
174: 
175: 
176: def main(InputImg, gamma_max):
177:     start_time = time.time()
178:     ######################################################
179:     float_image = i2f(InputImg)
180: 
181:     denoised = cv2.fastNlMeansDenoisingColored(InputImg, None, 10, 10, 7, 21)
182:     DenoiseImg = 1.0 - i2f(denoised)
183: 
184:     NormImg = np.empty(float_image.shape, float_image.dtype)
185: 
186:     A = Compute_A_Tang(DenoiseImg)
187:     for ind in range(0, 3):
188:         NormImg[:, :, ind] = DenoiseImg[:, :, ind] / A[0, ind]
189:     NormImg = Normalize(NormImg)
190: 
191:     Transmap = EstimateTransmission(float_image, NormImg, gamma_max)
192:     RecoverImg = Recover(float_image, Transmap, A)
193: 
194:     AdjustImg = Adjust(RecoverImg, 99.5, 0.5)
195: 
196:     ######################################################
197:     end_time = time.time()
198:     print("--- %s seconds ---" % (end_time - start_time))
199: 
200:     return AdjustImg
201: 
202: 
203: if __name__ == "__main__":
204:     FolderTemp = args.InputPath.split("/")
205:     OutputPath = args.OutputPath + "/Output/" + FolderTemp[-1]
206:     os.makedirs(OutputPath, exist_ok=True, mode=0o777)
207: 
208:     FileList = [
209:         file
210:         for file in os.listdir(args.InputPath)
211:         if (file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".jpeg"))
212:         or file.endswith(".webp")
213:         or file.endswith(".tiff")
214:         or file.endswith(".tif")
215:         or file.endswith(".bmp")
216:         or file.endswith(".png")
217:     ]
218: 
219:     for FileNum in range(0, len(FileList)):
220:         FilePathName = args.InputPath + "/" + FileList[FileNum]
221:         InputImg = cv2.imread(FilePathName, cv2.IMREAD_COLOR)
222: 
223:         OutputImg = main(InputImg, args.gamma_max)
224: 
225:         Name = os.path.splitext(FileList[FileNum])
226:         cv2.imwrite(OutputPath + "/" + Name[0] + ".png", f2i(OutputImg))

(End of file - total 226 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\demo_enhancement.py",
  "offset": 1,
  "limit": 260
}
```

**Output:**
```
<path>D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\demo_enhancement.py</path>
<type>file</type>
<content>
1: import numpy as np
2: import cv2
3: import matplotlib.pyplot as plt
4: from skimage import morphology
5: import os
6: 
7: 
8: def i2f(i_image):
9:     f_image = np.float32(i_image) / 255.0
10:     return f_image
11: 
12: 
13: def f2i(f_image):
14:     i_image = np.uint8(f_image * 255.0)
15:     return i_image
16: 
17: 
18: def Compute_A_Tang(im):
19:     erosion_window = 15
20:     n_bins = 200
21: 
22:     R = im[:, :, 2]
23:     G = im[:, :, 1]
24:     B = im[:, :, 0]
25: 
26:     dark = morphology.erosion(np.min(im, 2), morphology.square(erosion_window))
27: 
28:     [h, edges] = np.histogram(dark, n_bins, [0, 1])
29:     numpixel = im.shape[0] * im.shape[1]
30:     thr_frac = numpixel * 0.99
31:     csum = np.cumsum(h)
32:     nz_idx = np.nonzero(csum > thr_frac)[0][0]
33:     dc_thr = edges[nz_idx]
34:     mask = dark >= dc_thr
35:     rs = R[mask]
36:     gs = G[mask]
37:     bs = B[mask]
38: 
39:     A = np.zeros((1, 3))
40:     A[0, 2] = np.median(rs)
41:     A[0, 1] = np.median(gs)
42:     A[0, 0] = np.median(bs)
43: 
44:     return A
45: 
46: 
47: def GetIntensity(fi):
48:     return cv2.divide(fi[:, :, 0] + fi[:, :, 1] + fi[:, :, 2], 3)
49: 
50: 
51: def GetMax(fi):
52:     max_rgb = cv2.max(cv2.max(fi[:, :, 0], fi[:, :, 1]), fi[:, :, 2])
53:     return max_rgb
54: 
55: 
56: def GetMin(fi):
57:     min_rgb = cv2.max(cv2.min(fi[:, :, 0], fi[:, :, 1]), fi[:, :, 2])
58:     return min_rgb
59: 
60: 
61: def PixelAdaptiveGamma(InputImg, NormImg, amax):
62:     GCImg = np.empty(InputImg.shape, InputImg.dtype)
63:     amin = 1
64:     xmax = 1
65:     xmin = 0
66:     Imax = GetMax(InputImg)
67: 
68:     a = (amax - amin) / (np.exp(-xmin) - np.exp(-xmax))
69:     b = amax - a * np.exp(-xmin)
70:     g2 = a * np.exp(-Imax) + b
71:     g1 = np.where(Imax < xmin, amax, g2)
72:     gamma = np.where(Imax > xmax, amin, g1)
73: 
74:     for ind in range(0, 3):
75:         GCImg[:, :, ind] = NormImg[:, :, ind] ** gamma
76: 
77:     return GCImg, gamma
78: 
79: 
80: def EstimateTransmission(InputImg, NormImg, gamma_max=6):
81:     T_min = 0.1
82:     me = np.finfo(np.float32).eps
83:     hi = GetIntensity(NormImg)
84:     hmax = GetMax(NormImg)
85: 
86:     GCImg, gamma = PixelAdaptiveGamma(InputImg, NormImg, gamma_max)
87: 
88:     ji = GetIntensity(GCImg)
89:     jmax = GetMax(GCImg)
90: 
91:     tn = np.maximum(jmax * hi - hmax * ji, me)
92:     td = np.maximum((jmax - ji) * hi, me)
93: 
94:     Tmap = 1.0 - hi * (tn / td)
95: 
96:     return np.clip(Tmap, T_min, 1.0), gamma
97: 
98: 
99: def Recover(im, tmap, A):
100:     res = np.empty(im.shape, im.dtype)
101:     for ind in range(0, 3):
102:         res[:, :, ind] = (im[:, :, ind] - 1.0 + A[0, ind]) / tmap + 1.0 - A[0, ind]
103: 
104:     return np.clip(res, 0.0, 1.0)
105: 
106: 
107: def Adjust(im, perh, perl):
108:     aim = np.empty(im.shape, im.dtype)
109:     im_h = np.percentile(im, perh)
110:     im_l = np.percentile(im, perl)
111:     for ind in range(0, 3):
112:         aim[:, :, ind] = (im[:, :, ind] - im_l) / (im_h - im_l)
113: 
114:     return np.clip(aim, 0.0, 1.0)
115: 
116: 
117: def Normalize(im):
118:     aim = np.empty(im.shape, im.dtype)
119:     for ind in range(0, 3):
120:         im_h = np.max(im[:, :, ind])
121:         im_l = np.min(im[:, :, ind])
122:         aim[:, :, ind] = (im[:, :, ind] - im_l) / (im_h - im_l)
123:         aim[:, :, ind] = np.clip(aim[:, :, ind], 0.0, 1.0)
124: 
125:     return aim
126: 
127: 
128: def enhance_image(InputImg, gamma_max=6.0):
129:     float_image = i2f(InputImg)
130:     NormImg = np.empty(float_image.shape, float_image.dtype)
131:     DenoiseImg = 1.0 - cv2.GaussianBlur(float_image, (7, 7), 0)
132: 
133:     A = Compute_A_Tang(DenoiseImg)
134:     for ind in range(0, 3):
135:         NormImg[:, :, ind] = DenoiseImg[:, :, ind] / A[0, ind]
136:     NormImg = Normalize(NormImg)
137: 
138:     Transmap, gamma_map = EstimateTransmission(float_image, NormImg, gamma_max)
139:     RecoverImg = Recover(float_image, Transmap, A)
140: 
141:     AdjustImg = Adjust(RecoverImg, 99.5, 0.5)
142: 
143:     return AdjustImg, gamma_map, Transmap
144: 
145: 
146: def compute_histogram(image):
147:     hist_b = cv2.calcHist([image], [0], None, [256], [0, 256])
148:     hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
149:     hist_r = cv2.calcHist([image], [2], None, [256], [0, 256])
150:     return hist_b, hist_g, hist_r
151: 
152: 
153: def demo_enhancement(image_path, output_dir="demo_output"):
154:     os.makedirs(output_dir, exist_ok=True)
155: 
156:     InputImg = cv2.imread(image_path, cv2.IMREAD_COLOR)
157:     if InputImg is None:
158:         print(f"Error: Could not load image from {image_path}")
159:         return
160: 
161:     print("Running enhancement...")
162:     EnhancedImg, gamma_map, transmap = enhance_image(InputImg, gamma_max=6.0)
163: 
164:     EnhancedImg_uint8 = f2i(EnhancedImg)
165: 
166:     fig, axes = plt.subplots(2, 3, figsize=(15, 10))
167:     fig.suptitle(
168:         "Low-Light Image Enhancement Demonstration", fontsize=16, fontweight="bold"
169:     )
170: 
171:     original_rgb = cv2.cvtColor(InputImg, cv2.COLOR_BGR2RGB)
172:     enhanced_rgb = cv2.cvtColor(EnhancedImg_uint8, cv2.COLOR_BGR2RGB)
173: 
174:     axes[0, 0].imshow(original_rgb)
175:     axes[0, 0].set_title("Original Low-Light Image", fontsize=12)
176:     axes[0, 0].axis("off")
177: 
178:     axes[0, 1].imshow(enhanced_rgb)
179:     axes[0, 1].set_title("Enhanced Result", fontsize=12)
180:     axes[0, 1].axis("off")
181: 
182:     gamma_display = gamma_map
183:     gamma_normalized = (gamma_display - gamma_display.min()) / (
184:         gamma_display.max() - gamma_display.min()
185:     )
186:     axes[0, 2].imshow(gamma_normalized, cmap="jet")
187:     axes[0, 2].set_title(
188:         "Pixel-Adaptive Gamma Map\n(Dark=High Gamma, Bright=Low Gamma)", fontsize=12
189:     )
190:     axes[0, 2].axis("off")
191:     plt.colorbar(axes[0, 2].images[0], ax=axes[0, 2], fraction=0.046, pad=0.04)
192: 
193:     hist_b, hist_g, hist_r = compute_histogram(InputImg)
194:     axes[1, 0].plot(hist_b, color="b", label="Blue", alpha=0.7)
195:     axes[1, 0].plot(hist_g, color="g", label="Green", alpha=0.7)
196:     axes[1, 0].plot(hist_r, color="r", label="Red", alpha=0.7)
197:     axes[1, 0].set_title("Original Histogram\n(Compressed/Low Contrast)", fontsize=12)
198:     axes[1, 0].set_xlabel("Pixel Intensity")
199:     axes[1, 0].set_ylabel("Frequency")
200:     axes[1, 0].legend()
201:     axes[1, 0].set_xlim([0, 256])
202: 
203:     hist_b_enh, hist_g_enh, hist_r_enh = compute_histogram(EnhancedImg_uint8)
204:     axes[1, 1].plot(hist_b_enh, color="b", label="Blue", alpha=0.7)
205:     axes[1, 1].plot(hist_g_enh, color="g", label="Green", alpha=0.7)
206:     axes[1, 1].plot(hist_r_enh, color="r", label="Red", alpha=0.7)
207:     axes[1, 1].set_title("Enhanced Histogram\n(Spread/Improved Contrast)", fontsize=12)
208:     axes[1, 1].set_xlabel("Pixel Intensity")
209:     axes[1, 1].set_ylabel("Frequency")
210:     axes[1, 1].legend()
211:     axes[1, 1].set_xlim([0, 256])
212: 
213:     axes[1, 2].imshow(cv2.cvtColor(transmap, cv2.COLOR_BGR2RGB))
214:     axes[1, 2].set_title("Transmission Map", fontsize=12)
215:     axes[1, 2].axis("off")
216: 
217:     plt.tight_layout()
218: 
219:     output_path = os.path.join(output_dir, "demo_result.png")
220:     plt.savefig(output_path, dpi=150, bbox_inches="tight")
221:     print(f"Demo saved to: {output_path}")
222: 
223:     plt.show()
224: 
225:     return EnhancedImg_uint8, gamma_map
226: 
227: 
228: if __name__ == "__main__":
229:     input_dir = "inputi"
230:     image_files = [f for f in os.listdir(input_dir) if f.endswith(".png")]
231: 
232:     if image_files:
233:         sample_image = os.path.join(input_dir, image_files[0])
234:         print(f"Processing: {sample_image}")
235:         enhanced_img, gamma_map = demo_enhancement(sample_image)
236: 
237:         print("\n=== Enhancement Complete ===")
238:         print("Key observations:")
239:         print(
240:             "1. Original: Low contrast, compressed histogram, loss of details in dark regions"
241:         )
242:         print(
243:             "2. Enhanced: Expanded dynamic range, improved brightness, restored details"
244:         )
245:         print(
246:             "3. Gamma Map: Darker regions have higher gamma values (brighter after correction)"
247:         )
248:         print("4. Histogram: Shows spreading indicating improved contrast")
249:     else:
250:         print("No images found in input directory")

(End of file - total 250 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\README.md",
  "offset": 1,
  "limit": 200
}
```

**Output:**
```
<path>D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\README.md</path>
<type>file</type>
<content>
1: # Low_Light_Pattern_Recognition
2: 
3: "[Low-Light Image Enhancement Using Gamma Correction Prior in Mixed Color Spaces](https://doi.org/10.1016/j.patcog.2023.110001)," Pattern Recognition
4: [Jong Ju Jeon](https://github.com/TripleJ2543)(triplej@pusan.ac.kr), Jun Young Park(jyp9917140@pusan.ac.kr), Il Kyu Eom*(ikeom@pusan.ac.kr)(https://sites.google.com/view/ispl-pnu)   
5: 
6: [Site](https://sites.google.com/view/ispl-pnu), [Paper](https://doi.org/10.1016/j.patcog.2023.110001)
7: 
8: 
9: ### Requirements ###
10: 1. Linux
11: 2. Python (3.11.4)
12: 3. scikit-image (0.20.0)
13: 4. opencv (4.6.0)
14: 
15: 
16: ### Usage ###
17: you can just run through
18: ```shell
19: python Run_LowLight_Image_Enhancement_Pixel_Adaptive.py 
20:     --input_dir=/path/to/your/dataset/dir/ \
21:     --output_dir=/path/to/save/results/ \
22:     --gamma_max=6                               # defaults gamma_max=6
23: 
24: #python Run_LowLight.py --input_dir=/path/to/your/dataset/dir/ --output_dir=/path/to/save/results/ --gamma_max=6
25: 
26: ```
27: 
28: ### Citation ###
29: Jong Ju Jeon, Jun Young Park, Il Kyu Eom,   
30: Low-Light Image Enhancement Using Gamma Correction Prior in Mixed Color Spaces,   
31: Pattern Recognition,   
32: 2023,   
33: https://doi.org/10.1016/j.patcog.2023.110001.
34: (https://www.sciencedirect.com/science/article/pii/S0031320323006994)
35: 
36: Keywords: Low-light image enhancement; Inverted image; Atmospheric light; Normalization; Transmission map; Retinex model; HSV color space; HSI color space; Gamma correction   

(End of file - total 36 lines)
</content>
```

---

## Assistant (Build · GPT-5.4 · 961.8s)

_Thinking:_

**Considering enhancements for denoising**

I need to implement enhancements for both the main and demo versions. I might inspect any test infrastructure we have in place. Using bash to run a Python script could be a possibility. I want to design minimal changes while reasoning through the algorithm.

I see that the current methods for noise removal could be improved by combining bilateral filtering with Non-Local Means based on estimated noise. Implementing automatic parameter tuning could help adjust for different images. I'm also thinking about optimizing processing speed by vectorizing operations or downscaling images for transmission estimation. Lastly, I want to ensure we don't degrade output quality as we make these changes.

_Thinking:_

**Exploring transmission scaling and noise removal**

I’m thinking of using a transmission scale of about 0.5 for larger images. For stronger noise removal, I want to tune the denoise strength with fastNlMeansDenoisingColored after applying CLAHE. However, I need it to be effective without slowing down processing too much.

Using `cv2.bilateralFilter` after Non-Local Means might help. I should consider applying bilateral filtering on downsampled inputs for better efficiency. To improve processing speed, I’ll look into vectorizing functions like Recover, Normalize, and Adjust to avoid looping. Downsampling might only be necessary for certain branches, keeping overall recovery at full size.

_Thinking:_

**Formalizing processing steps**

I'm formalizing my processing approach. First, I want to set the `processing_scale` to be the minimum of 1.0 or the square root of the ratio of target pixels to total pixels, targeting around 900k pixels. If the image is larger, I’ll resize the float_image for the denoise and estimate branch. 

Next, I’ll perform denoising on the resized working image and compute A, NormImg, and Transmap there. Finally, I plan to upsample the Transmap back to the original size and use the same A for the full-size recovery.

_Thinking:_

**Refining noise removal methods**

I'm considering whether to denoise the full image first before recovery or just focus on the inverted image. It seems better to denoise the original image to avoid amplifying noise during enhancement. However, the recovery process expects the original input. I might get better results by creating a denoised float image for recovery while blending with the original input. I'll explore simpler steps like auto-tuning noise parameters and applying filters as necessary.

_Thinking:_

**Considering image processing options**

I plan to use a denoised float image as the base for further processing, while keeping the original image reserved. It seems like estimating transmission could benefit from this base float image, potentially improving noise reduction and overall quality. I need to address a bug in the GetMin function that seems incorrect. Also, I’m contemplating whether to update the command-line interface (CLI) to include an auto mode while balancing backwards compatibility. Adding flags for gamma tuning could be useful, but I need to be cautious about changing behaviors.

_Thinking:_

**Updating files and documentation**

I need to focus on editing the files using the apply_patch method only. I’m also considering updating the README to reflect any changes made. Additionally, I might need to edit both the main and demo files to ensure everything is consistent. It’s important to keep the documentation accurate, so users know what to expect. Let's make sure all necessary updates are done efficiently!

_Thinking:_

**Refactoring thoughts**

I’m considering whether to restructure the script or duplicate code. It might be easier to refactor the main script by placing the parser under the main guard to make the functions importable. Moving the parser into a function called `build_parser` sounds good. I should rename the enhancement function from `main` to `enhance_image` and add a CLI function for running. Even though the user didn't ask for a refactor, keeping the main script changes in sync manually seems safer than duplicating maintenance. I'll inspect if other scripts reference the main function.

_Thinking:_

**Considering noise estimation functions**

I'm thinking about creating a helper function called `estimate_noise_level`. It would take a float image, convert it to grayscale, and potentially make it easier by working with an input in uint8 format. I might use the Laplacian standard deviation on the luminance high pass for noise estimation. The standard formula with the median absolute deviation of the Laplacian is `sigma = median(|laplacian|)/0.6745`, and I’ll ensure it’s normalized in the range of [0, 1].

_Thinking:_

**Evaluating image processing techniques**

I’m working through how to manage image resizing and processing. For any image under the targeted size, I need to resize using `INTER_AREA` to maintain quality. Denoising smaller images is faster but might compromise accuracy, so maybe I should denoise the full-sized image in some cases. I wonder if using a bilateral filter for larger images could speed things up. I’ll need to carefully choose methods to balance speed and detail retention.

_Thinking:_

**Exploring improvements in processing**

I’m considering whether to keep the command line interface (CLI) the same or introduce an internal constant, which might simplify things. It could help to print tuned parameters for the user, like `gamma=5.23` or `denoise_h=`. However, during batch processing, I want to keep it moderate. I also need to fix a demo bug related to the `transmap` display, which is likely broken. I could adjust it to `imshow(transmap, cmap="viridis")`. Also, I’m thinking about adding functions for estimating image statistics and auto-tuning parameters.

_Thinking:_

**Optimizing performance**

I'm considering performance hotspots from loops, particularly with scikit-image morphology. I think replacing `skimage.morphology.erosion` with `cv2.erode` could speed things up. Since I'm working with a float image dark channel, using a kernel like `np.ones((15,15), np.uint8)` might be faster. This shift could eliminate the need for the scikit dependency while maintaining performance. I should also explore using `np.max` and `np.mean` for intensity calculations instead of relying entirely on cv2 operations, aiming for clarity and efficiency.

_Thinking:_

**Refactoring image enhancement**

I’m thinking about implementing a `enhance_image(InputImg, gamma_max=6.0, auto_tune=True)` function, with auto tuning set to True by default. This might return metadata and be used in the main CLI. I want to update the README to include information about auto tuning and performance paths. There’s a potential for duplicated code in the demo, so I’m considering refactoring the parser. I'll create a `build_parser()` function and organize the helpers, improving structure and reducing duplication. It should work smoothly.

_Thinking:_

**Reviewing script updates**

I'm considering running `python -m compileall` or a script on a sample image to check if dependencies are in place. I might need to use bash and apply patches for editing multiple files. I think patching the main script with extensive updates, demos, and README files is essential. I should be cautious about potential import cycles in the demo imports, and I need to handle possible division by zero in the `Normalize` function. Creating a helper function for resizing images also seems like a good idea.

_Thinking:_

**Considering gamma tuning**

I'm looking at using `cv2.addWeighted`, which returns `uint8`, and I think I need to set a `processing_scale` for target pixels around 960k. I'll use a formula involving the square root of the ratio between target and total pixels. There’s a large image threshold at 1600x900 pixels, and if the scale is less than 1, it counts as large. Additionally, I need to tune gamma automatically with a user-supplied max cap, but I have to be careful not to let it break if the user sets it below 2. Using dynamic limits for gamma sounds like a solid idea!

_Thinking:_

**Adjusting gamma calculations**

I’m evaluating my gamma calculations, and I think `gamma_base` might be set at 1.8 for cap=6, yielding 2.25. But this might be too high for brighter images. A simpler approach could be `tuned_gamma = 1.0 + (gamma_cap - 1.0) * drive`, and I’m considering setting `drive` to at least 0.35. For dark images, using the cap seems good, and I want some enhancement to always occur, possibly with a floor of 0.15. So, gamma might hit around 1.75 for cap 6.

_Thinking:_

**Refining denoise strength formula**

I'm working on my denoise strength formula. For `InputImg uint8`, I'm calculating `denoise_h` as `int(round(5 + 12 * noise_factor + 5 * darkness))`, but it might range from 5 to 22. For color, I have `denoise_h_color` set at `int(round(5 + 8 * noise_factor + 3 * darkness))`, and maybe I should clamp it. I’m considering a `processing_scale` of 1 for resolutions below 1280x720 and using the square root for larger areas. I'm also refining parameters like `bilateral_sigma_color` and `adjust_high/low`, ensuring I retune for each image with the `denoised_input` path.

_Thinking:_

**Considering processing optimizations**

I'm thinking about whether parallel dataset processing could help, maybe using ThreadPoolExecutor. Real-time processing sounds nice, but multithreading complicates things because of the GIL, although OpenCV does release it. It could be better to keep things simpler, perhaps just set some optimization flags for OpenCV. Using `cv2.setUseOptimized(True)` and configuring thread management might speed things up, but I need to think about the overall complexity. Let's focus on a straightforward approach and patch the main script accordingly.

I found the core pipeline in `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py`. I’m updating that script to add auto-tuned denoising and gamma selection, plus a faster large-image processing path, then I’ll wire the demo and docs to the same behavior.

**Tool: apply_patch**

**Input:**
```json
{
  "patchText": "*** Begin Patch\n*** Update File: D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\Run_LowLight_Image_Enhancement_Pixel_Adaptive.py\n@@\n-import numpy as np\n-import cv2\n-\n-from skimage import morphology\n-import time\n-import os\n-import argparse\n-\n-parser = argparse.ArgumentParser(description=\"\")\n-parser.add_argument(\n-    \"--input_dir\",\n-    dest=\"InputPath\",\n-    default=\"/home/ispl-public/Desktop/Dataset/LIME\",\n-    help=\"directory for testing inputs\",\n-)\n-parser.add_argument(\n-    \"--output_dir\",\n-    dest=\"OutputPath\",\n-    default=\"./\",\n-    help=\"directory for testing outputs\",\n-)\n-parser.add_argument(\n-    \"--gamma_max\", dest=\"gamma_max\", type=float, default=6.0, help=\"gamma_max value\"\n-)\n-args = parser.parse_args()\n+import argparse\n+import os\n+import time\n+\n+import cv2\n+import numpy as np\n+\n+\n+VALID_EXTENSIONS = (\".jpg\", \".jpeg\", \".webp\", \".tiff\", \".tif\", \".bmp\", \".png\")\n+\n+\n+def build_parser():\n+    parser = argparse.ArgumentParser(description=\"\")\n+    parser.add_argument(\n+        \"--input_dir\",\n+        dest=\"InputPath\",\n+        default=\"/home/ispl-public/Desktop/Dataset/LIME\",\n+        help=\"directory for testing inputs\",\n+    )\n+    parser.add_argument(\n+        \"--output_dir\",\n+        dest=\"OutputPath\",\n+        default=\"./\",\n+        help=\"directory for testing outputs\",\n+    )\n+    parser.add_argument(\n+        \"--gamma_max\",\n+        dest=\"gamma_max\",\n+        type=float,\n+        default=6.0,\n+        help=\"maximum gamma value used as an auto-tuning upper bound\",\n+    )\n+    return parser\n@@\n def f2i(f_image):\n-    i_image = np.uint8(f_image * 255.0)\n+    i_image = np.uint8(np.clip(f_image, 0.0, 1.0) * 255.0)\n     return i_image\n@@\n def Compute_A_Tang(im):\n     erosion_window = 15\n     n_bins = 200\n-\n-    R = im[:, :, 2]\n-    G = im[:, :, 1]\n-    B = im[:, :, 0]\n-\n-    # compute the dark channel\n-    dark = morphology.erosion(np.min(im, 2), morphology.square(erosion_window))\n-\n-    [h, edges] = np.histogram(dark, n_bins, [0, 1])\n+\n+    dark = cv2.erode(\n+        np.min(im, axis=2), np.ones((erosion_window, erosion_window), dtype=np.uint8)\n+    )\n+\n+    [h, edges] = np.histogram(dark, n_bins, [0, 1])\n     numpixel = im.shape[0] * im.shape[1]\n     thr_frac = numpixel * 0.99\n     csum = np.cumsum(h)\n-    nz_idx = np.nonzero(csum > thr_frac)[0][0]\n-    dc_thr = edges[nz_idx]\n+    nz_idx = min(np.searchsorted(csum, thr_frac), n_bins - 1)\n+    dc_thr = edges[nz_idx]\n     mask = dark >= dc_thr\n-    # similar to DCP till this step\n-    # next, median of these top 0.1% pixels\n-    # median of the RGB values of the pixels in the mask\n-    rs = R[mask]\n-    gs = G[mask]\n-    bs = B[mask]\n-\n-    A = np.zeros((1, 3))\n-\n-    A[0, 2] = np.median(rs)\n-    A[0, 1] = np.median(gs)\n-    A[0, 0] = np.median(bs)\n-\n-    return A\n+    if not np.any(mask):\n+        mask = dark >= np.percentile(dark, 99)\n+\n+    A = np.median(im[mask], axis=0, keepdims=True)\n+\n+    return np.maximum(A, np.finfo(np.float32).eps)\n@@\n def GetIntensity(fi):\n-    return cv2.divide(fi[:, :, 0] + fi[:, :, 1] + fi[:, :, 2], 3)\n+    return np.mean(fi, axis=2)\n@@\n def GetMax(fi):\n-    max_rgb = cv2.max(cv2.max(fi[:, :, 0], fi[:, :, 1]), fi[:, :, 2])\n-    return max_rgb\n+    return np.max(fi, axis=2)\n@@\n def GetMin(fi):\n-    min_rgb = cv2.max(cv2.min(fi[:, :, 0], fi[:, :, 1]), fi[:, :, 2])\n-    return min_rgb\n+    return np.min(fi, axis=2)\n@@\n def PixelAdaptiveGamma(InputImg, NormImg, amax):\n-    GCImg = np.empty(InputImg.shape, InputImg.dtype)\n     amin = 1\n     xmax = 1\n     xmin = 0\n     Imax = GetMax(InputImg)\n@@\n     g2 = a * np.exp(-Imax) + b\n     g1 = np.where(Imax < xmin, amax, g2)\n     gamma = np.where(Imax > xmax, amin, g1)\n-\n-    for ind in range(0, 3):\n-        GCImg[:, :, ind] = NormImg[:, :, ind] ** gamma\n-\n-    return GCImg\n+\n+    GCImg = np.power(NormImg, gamma[:, :, None])\n+\n+    return GCImg, gamma\n@@\n def EstimateTransmission(InputImg, NormImg, gamma_max=6):\n     T_min = 0.1\n     me = np.finfo(np.float32).eps\n     hi = GetIntensity(NormImg)\n     hmax = GetMax(NormImg)\n \n-    GCImg = PixelAdaptiveGamma(InputImg, NormImg, gamma_max)\n+    GCImg, gamma = PixelAdaptiveGamma(InputImg, NormImg, gamma_max)\n@@\n     td = np.maximum((jmax - ji) * hi, me)\n \n     Tmap = 1.0 - hi * (tn / td)\n \n-    return np.clip(Tmap, T_min, 1.0)\n+    return np.clip(Tmap, T_min, 1.0), gamma\n@@\n def Recover(im, tmap, A):\n-    res = np.empty(im.shape, im.dtype)\n-    for ind in range(0, 3):\n-        res[:, :, ind] = (im[:, :, ind] - 1.0 + A[0, ind]) / tmap + 1.0 - A[0, ind]\n-\n+    res = (im - 1.0 + A.reshape(1, 1, 3)) / tmap[:, :, None] + 1.0 - A.reshape(1, 1, 3)\n     return np.clip(res, 0.0, 1.0)\n@@\n def Adjust(im, perh, perl):\n-    aim = np.empty(im.shape, im.dtype)\n     im_h = np.percentile(im, perh)\n     im_l = np.percentile(im, perl)\n-    for ind in range(0, 3):\n-        aim[:, :, ind] = (im[:, :, ind] - im_l) / (im_h - im_l)\n-\n+    aim = (im - im_l) / max(im_h - im_l, np.finfo(np.float32).eps)\n     return np.clip(aim, 0.0, 1.0)\n@@\n def Normalize(im):\n-    aim = np.empty(im.shape, im.dtype)\n-    for ind in range(0, 3):\n-        im_h = np.max(im[:, :, ind])\n-        im_l = np.min(im[:, :, ind])\n-        aim[:, :, ind] = (im[:, :, ind] - im_l) / (im_h - im_l)\n-        aim[:, :, ind] = np.clip(aim[:, :, ind], 0.0, 1.0)\n-\n-    return aim\n+    im_h = np.max(im, axis=(0, 1), keepdims=True)\n+    im_l = np.min(im, axis=(0, 1), keepdims=True)\n+    aim = (im - im_l) / np.maximum(im_h - im_l, np.finfo(np.float32).eps)\n+    return np.clip(aim, 0.0, 1.0)\n+\n+\n+def EstimateNoiseLevel(InputImg):\n+    gray = cv2.cvtColor(InputImg, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0\n+    laplacian = cv2.Laplacian(gray, cv2.CV_32F, ksize=3)\n+    return float(np.median(np.abs(laplacian)) / 0.6745)\n+\n+\n+def AutoTuneParameters(InputImg, gamma_limit):\n+    gray = cv2.cvtColor(InputImg, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0\n+    brightness = float(np.mean(gray))\n+    contrast = float(np.std(gray))\n+    noise_level = EstimateNoiseLevel(InputImg)\n+\n+    darkness = np.clip((0.6 - brightness) / 0.6, 0.0, 1.0)\n+    contrast_penalty = np.clip((0.25 - contrast) / 0.25, 0.0, 1.0)\n+    noise_factor = np.clip(noise_level / 0.12, 0.0, 1.0)\n+\n+    gamma_cap = max(float(gamma_limit), 1.0)\n+    gamma_drive = np.clip(\n+        0.7 * darkness + 0.3 * contrast_penalty + 0.2 * noise_factor, 0.15, 1.0\n+    )\n+    tuned_gamma_max = 1.0 + (gamma_cap - 1.0) * gamma_drive\n+\n+    area = InputImg.shape[0] * InputImg.shape[1]\n+    target_pixels = 1280 * 720\n+    processing_scale = 1.0\n+    if area > target_pixels:\n+        processing_scale = float(np.sqrt(target_pixels / area))\n+\n+    return {\n+        \"brightness\": brightness,\n+        \"contrast\": contrast,\n+        \"noise_level\": noise_level,\n+        \"noise_factor\": float(noise_factor),\n+        \"darkness\": float(darkness),\n+        \"gamma_max\": float(np.clip(tuned_gamma_max, 1.0, gamma_cap)),\n+        \"denoise_h\": int(np.clip(round(5 + 12 * noise_factor + 5 * darkness), 5, 20)),\n+        \"denoise_h_color\": int(\n+            np.clip(round(5 + 8 * noise_factor + 3 * darkness), 5, 16)\n+        ),\n+        \"bilateral_sigma_color\": int(\n+            np.clip(round(20 + 55 * (0.6 * noise_factor + 0.4 * darkness)), 20, 75)\n+        ),\n+        \"bilateral_sigma_space\": int(np.clip(round(7 + 8 * noise_factor), 7, 15)),\n+        \"processing_scale\": processing_scale,\n+        \"adjust_high\": 99.7 if darkness > 0.5 else 99.5,\n+        \"adjust_low\": 0.3 if contrast_penalty > 0.5 else 0.5,\n+    }\n+\n+\n+def ResizeImage(image, scale, interpolation):\n+    if scale >= 0.999:\n+        return image\n+\n+    height, width = image.shape[:2]\n+    new_size = (\n+        max(1, int(round(width * scale))),\n+        max(1, int(round(height * scale))),\n+    )\n+    return cv2.resize(image, new_size, interpolation=interpolation)\n+\n+\n+def DenoiseImage(InputImg, params):\n+    if params[\"processing_scale\"] < 0.9:\n+        small = ResizeImage(InputImg, params[\"processing_scale\"], cv2.INTER_AREA)\n+        small_denoised = cv2.fastNlMeansDenoisingColored(\n+            small,\n+            None,\n+            params[\"denoise_h\"],\n+            params[\"denoise_h_color\"],\n+            7,\n+            21,\n+        )\n+        denoise_prior = cv2.resize(\n+            small_denoised,\n+            (InputImg.shape[1], InputImg.shape[0]),\n+            interpolation=cv2.INTER_LINEAR,\n+        )\n+        edge_preserved = cv2.bilateralFilter(\n+            InputImg,\n+            7,\n+            params[\"bilateral_sigma_color\"],\n+            params[\"bilateral_sigma_space\"],\n+        )\n+        denoised = cv2.addWeighted(edge_preserved, 0.6, denoise_prior, 0.4, 0)\n+    else:\n+        denoised = cv2.fastNlMeansDenoisingColored(\n+            InputImg,\n+            None,\n+            params[\"denoise_h\"],\n+            params[\"denoise_h_color\"],\n+            7,\n+            21,\n+        )\n+\n+    if params[\"noise_factor\"] > 0.3 or params[\"darkness\"] > 0.45:\n+        denoised = cv2.bilateralFilter(\n+            denoised,\n+            5,\n+            params[\"bilateral_sigma_color\"],\n+            params[\"bilateral_sigma_space\"],\n+        )\n+\n+    return denoised\n@@\n-\"\"\" Main \"\"\"\n-\n-\n-def main(InputImg, gamma_max):\n+\"\"\" Main \"\"\"\n+\n+\n+def enhance_image(InputImg, gamma_max, return_details=False):\n     start_time = time.time()\n-    ######################################################\n-    float_image = i2f(InputImg)\n-\n-    denoised = cv2.fastNlMeansDenoisingColored(InputImg, None, 10, 10, 7, 21)\n-    DenoiseImg = 1.0 - i2f(denoised)\n-\n-    NormImg = np.empty(float_image.shape, float_image.dtype)\n-\n+    params = AutoTuneParameters(InputImg, gamma_max)\n+    denoised_input = DenoiseImage(InputImg, params)\n+    base_float = i2f(denoised_input)\n+\n+    working_float = ResizeImage(base_float, params[\"processing_scale\"], cv2.INTER_AREA)\n+    DenoiseImg = 1.0 - working_float\n+\n     A = Compute_A_Tang(DenoiseImg)\n-    for ind in range(0, 3):\n-        NormImg[:, :, ind] = DenoiseImg[:, :, ind] / A[0, ind]\n-    NormImg = Normalize(NormImg)\n-\n-    Transmap = EstimateTransmission(float_image, NormImg, gamma_max)\n-    RecoverImg = Recover(float_image, Transmap, A)\n-\n-    AdjustImg = Adjust(RecoverImg, 99.5, 0.5)\n-\n-    ######################################################\n+    NormImg = Normalize(DenoiseImg / A.reshape(1, 1, 3))\n+\n+    Transmap, gamma_map = EstimateTransmission(working_float, NormImg, params[\"gamma_max\"])\n+    if params[\"processing_scale\"] < 0.999:\n+        target_size = (InputImg.shape[1], InputImg.shape[0])\n+        Transmap = cv2.resize(Transmap, target_size, interpolation=cv2.INTER_LINEAR)\n+        gamma_map = cv2.resize(gamma_map, target_size, interpolation=cv2.INTER_LINEAR)\n+\n+    RecoverImg = Recover(base_float, Transmap, A)\n+    AdjustImg = Adjust(RecoverImg, params[\"adjust_high\"], params[\"adjust_low\"])\n+\n     end_time = time.time()\n-    print(\"--- %s seconds ---\" % (end_time - start_time))\n+    details = {\n+        **params,\n+        \"gamma_map\": gamma_map,\n+        \"transmission_map\": Transmap,\n+        \"runtime\": end_time - start_time,\n+    }\n+    print(\n+        \"--- %.3f seconds | gamma_max=%.2f | denoise_h=%d | scale=%.2f ---\"\n+        % (\n+            details[\"runtime\"],\n+            details[\"gamma_max\"],\n+            details[\"denoise_h\"],\n+            details[\"processing_scale\"],\n+        )\n+    )\n \n-    return AdjustImg\n+    if return_details:\n+        return AdjustImg, details\n+    return AdjustImg\n+\n+\n+def run_folder(InputPath, OutputPath, gamma_max):\n+    FolderTemp = os.path.normpath(InputPath).split(os.sep)\n+    output_dir = os.path.join(OutputPath, \"Output\", FolderTemp[-1])\n+    os.makedirs(output_dir, exist_ok=True, mode=0o777)\n+\n+    FileList = sorted(\n+        [\n+            file\n+            for file in os.listdir(InputPath)\n+            if os.path.splitext(file)[1].lower() in VALID_EXTENSIONS\n+        ]\n+    )\n+\n+    for file_name in FileList:\n+        file_path = os.path.join(InputPath, file_name)\n+        InputImg = cv2.imread(file_path, cv2.IMREAD_COLOR)\n+        if InputImg is None:\n+            continue\n+\n+        OutputImg = enhance_image(InputImg, gamma_max)\n+\n+        name, _ = os.path.splitext(file_name)\n+        cv2.imwrite(os.path.join(output_dir, name + \".png\"), f2i(OutputImg))\n \n \n if __name__ == \"__main__\":\n-    FolderTemp = args.InputPath.split(\"/\")\n-    OutputPath = args.OutputPath + \"/Output/\" + FolderTemp[-1]\n-    os.makedirs(OutputPath, exist_ok=True, mode=0o777)\n-\n-    FileList = [\n-        file\n-        for file in os.listdir(args.InputPath)\n-        if (file.endswith(\".jpg\") or file.endswith(\".JPG\") or file.endswith(\".jpeg\"))\n-        or file.endswith(\".webp\")\n-        or file.endswith(\".tiff\")\n-        or file.endswith(\".tif\")\n-        or file.endswith(\".bmp\")\n-        or file.endswith(\".png\")\n-    ]\n-\n-    for FileNum in range(0, len(FileList)):\n-        FilePathName = args.InputPath + \"/\" + FileList[FileNum]\n-        InputImg = cv2.imread(FilePathName, cv2.IMREAD_COLOR)\n-\n-        OutputImg = main(InputImg, args.gamma_max)\n-\n-        Name = os.path.splitext(FileList[FileNum])\n-        cv2.imwrite(OutputPath + \"/\" + Name[0] + \".png\", f2i(OutputImg))\n+    cv2.setUseOptimized(True)\n+    args = build_parser().parse_args()\n+    run_folder(args.InputPath, args.OutputPath, args.gamma_max)\n*** End Patch"
}
```

**Output:**
```
Success. Updated the following files:
M org/Run_LowLight_Image_Enhancement_Pixel_Adaptive.py
```

---

## Assistant (Build · GPT-5.4 · 96.6s)

_Thinking:_

**Updating demo functionality**

I need to focus on updating the demo. First, I should import the shared functions. Then, there’s the part where I have to fix the display issue. It’s important to ensure everything is lined up correctly in the presentation. I wonder if there are any particular problems that might crop up once I start patching things. The goal is to make everything run smoothly! Let's tackle this step by step.

**Tool: apply_patch**

**Input:**
```json
{
  "patchText": "*** Begin Patch\n*** Update File: D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\demo_enhancement.py\n@@\n-import numpy as np\n import cv2\n import matplotlib.pyplot as plt\n-from skimage import morphology\n import os\n-\n-\n-def i2f(i_image):\n-    f_image = np.float32(i_image) / 255.0\n-    return f_image\n-\n-\n-def f2i(f_image):\n-    i_image = np.uint8(f_image * 255.0)\n-    return i_image\n-\n-\n-def Compute_A_Tang(im):\n-    erosion_window = 15\n-    n_bins = 200\n-\n-    R = im[:, :, 2]\n-    G = im[:, :, 1]\n-    B = im[:, :, 0]\n-\n-    dark = morphology.erosion(np.min(im, 2), morphology.square(erosion_window))\n-\n-    [h, edges] = np.histogram(dark, n_bins, [0, 1])\n-    numpixel = im.shape[0] * im.shape[1]\n-    thr_frac = numpixel * 0.99\n-    csum = np.cumsum(h)\n-    nz_idx = np.nonzero(csum > thr_frac)[0][0]\n-    dc_thr = edges[nz_idx]\n-    mask = dark >= dc_thr\n-    rs = R[mask]\n-    gs = G[mask]\n-    bs = B[mask]\n-\n-    A = np.zeros((1, 3))\n-    A[0, 2] = np.median(rs)\n-    A[0, 1] = np.median(gs)\n-    A[0, 0] = np.median(bs)\n-\n-    return A\n-\n-\n-def GetIntensity(fi):\n-    return cv2.divide(fi[:, :, 0] + fi[:, :, 1] + fi[:, :, 2], 3)\n-\n-\n-def GetMax(fi):\n-    max_rgb = cv2.max(cv2.max(fi[:, :, 0], fi[:, :, 1]), fi[:, :, 2])\n-    return max_rgb\n-\n-\n-def GetMin(fi):\n-    min_rgb = cv2.max(cv2.min(fi[:, :, 0], fi[:, :, 1]), fi[:, :, 2])\n-    return min_rgb\n-\n-\n-def PixelAdaptiveGamma(InputImg, NormImg, amax):\n-    GCImg = np.empty(InputImg.shape, InputImg.dtype)\n-    amin = 1\n-    xmax = 1\n-    xmin = 0\n-    Imax = GetMax(InputImg)\n-\n-    a = (amax - amin) / (np.exp(-xmin) - np.exp(-xmax))\n-    b = amax - a * np.exp(-xmin)\n-    g2 = a * np.exp(-Imax) + b\n-    g1 = np.where(Imax < xmin, amax, g2)\n-    gamma = np.where(Imax > xmax, amin, g1)\n-\n-    for ind in range(0, 3):\n-        GCImg[:, :, ind] = NormImg[:, :, ind] ** gamma\n-\n-    return GCImg, gamma\n-\n-\n-def EstimateTransmission(InputImg, NormImg, gamma_max=6):\n-    T_min = 0.1\n-    me = np.finfo(np.float32).eps\n-    hi = GetIntensity(NormImg)\n-    hmax = GetMax(NormImg)\n-\n-    GCImg, gamma = PixelAdaptiveGamma(InputImg, NormImg, gamma_max)\n-\n-    ji = GetIntensity(GCImg)\n-    jmax = GetMax(GCImg)\n-\n-    tn = np.maximum(jmax * hi - hmax * ji, me)\n-    td = np.maximum((jmax - ji) * hi, me)\n-\n-    Tmap = 1.0 - hi * (tn / td)\n-\n-    return np.clip(Tmap, T_min, 1.0), gamma\n-\n-\n-def Recover(im, tmap, A):\n-    res = np.empty(im.shape, im.dtype)\n-    for ind in range(0, 3):\n-        res[:, :, ind] = (im[:, :, ind] - 1.0 + A[0, ind]) / tmap + 1.0 - A[0, ind]\n-\n-    return np.clip(res, 0.0, 1.0)\n-\n-\n-def Adjust(im, perh, perl):\n-    aim = np.empty(im.shape, im.dtype)\n-    im_h = np.percentile(im, perh)\n-    im_l = np.percentile(im, perl)\n-    for ind in range(0, 3):\n-        aim[:, :, ind] = (im[:, :, ind] - im_l) / (im_h - im_l)\n-\n-    return np.clip(aim, 0.0, 1.0)\n-\n-\n-def Normalize(im):\n-    aim = np.empty(im.shape, im.dtype)\n-    for ind in range(0, 3):\n-        im_h = np.max(im[:, :, ind])\n-        im_l = np.min(im[:, :, ind])\n-        aim[:, :, ind] = (im[:, :, ind] - im_l) / (im_h - im_l)\n-        aim[:, :, ind] = np.clip(aim[:, :, ind], 0.0, 1.0)\n-\n-    return aim\n-\n-\n-def enhance_image(InputImg, gamma_max=6.0):\n-    float_image = i2f(InputImg)\n-    NormImg = np.empty(float_image.shape, float_image.dtype)\n-    DenoiseImg = 1.0 - cv2.GaussianBlur(float_image, (7, 7), 0)\n-\n-    A = Compute_A_Tang(DenoiseImg)\n-    for ind in range(0, 3):\n-        NormImg[:, :, ind] = DenoiseImg[:, :, ind] / A[0, ind]\n-    NormImg = Normalize(NormImg)\n-\n-    Transmap, gamma_map = EstimateTransmission(float_image, NormImg, gamma_max)\n-    RecoverImg = Recover(float_image, Transmap, A)\n-\n-    AdjustImg = Adjust(RecoverImg, 99.5, 0.5)\n-\n-    return AdjustImg, gamma_map, Transmap\n+\n+from Run_LowLight_Image_Enhancement_Pixel_Adaptive import enhance_image, f2i\n@@\n     if InputImg is None:\n         print(f\"Error: Could not load image from {image_path}\")\n         return\n \n     print(\"Running enhancement...\")\n-    EnhancedImg, gamma_map, transmap = enhance_image(InputImg, gamma_max=6.0)\n+    EnhancedImg, details = enhance_image(InputImg, gamma_max=6.0, return_details=True)\n \n     EnhancedImg_uint8 = f2i(EnhancedImg)\n+    gamma_map = details[\"gamma_map\"]\n+    transmap = details[\"transmission_map\"]\n@@\n-    axes[1, 2].imshow(cv2.cvtColor(transmap, cv2.COLOR_BGR2RGB))\n+    axes[1, 2].imshow(transmap, cmap=\"viridis\")\n     axes[1, 2].set_title(\"Transmission Map\", fontsize=12)\n     axes[1, 2].axis(\"off\")\n+    plt.colorbar(axes[1, 2].images[0], ax=axes[1, 2], fraction=0.046, pad=0.04)\n@@\n-    return EnhancedImg_uint8, gamma_map\n+    print(\n+        \"Auto-tuned gamma_max=%.2f, denoise_h=%d, scale=%.2f\"\n+        % (\n+            details[\"gamma_max\"],\n+            details[\"denoise_h\"],\n+            details[\"processing_scale\"],\n+        )\n+    )\n+\n+    return EnhancedImg_uint8, gamma_map\n*** End Patch"
}
```

**Output:**
```
Success. Updated the following files:
M org/demo_enhancement.py
```

---

## Assistant (Build · GPT-5.4 · 23.6s)

_Thinking:_



The core script is updated. I’m documenting the new behavior in `README.md` and then I’ll run the code on the bundled sample images to catch integration issues.

**Tool: apply_patch**

**Input:**
```json
{
  "patchText": "*** Begin Patch\n*** Update File: D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\README.md\n@@\n-### Usage ###\n-you can just run through\n+### Usage ###\n+you can just run through\n ```shell\n python Run_LowLight_Image_Enhancement_Pixel_Adaptive.py \n     --input_dir=/path/to/your/dataset/dir/ \\\n     --output_dir=/path/to/save/results/ \\\n-    --gamma_max=6                               # defaults gamma_max=6\n+    --gamma_max=6                               # auto-tuning upper bound, defaults to 6\n \n #python Run_LowLight.py --input_dir=/path/to/your/dataset/dir/ --output_dir=/path/to/save/results/ --gamma_max=6\n \n ```\n+\n+### Enhancements ###\n+1. Stronger noise removal\n+   The pipeline now applies an auto-tuned denoising stage before enhancement. It combines Non-Local Means with an edge-preserving bilateral pass so noise is reduced without flattening image structure.\n+2. Automatic parameter tuning\n+   `gamma_max` is no longer used as a single fixed value for every image. It is treated as the upper bound for a per-image tuning step based on estimated brightness, contrast, and noise.\n+3. Faster processing\n+   The implementation now removes several Python channel loops, uses OpenCV erosion for dark-channel estimation, and downsamples only the expensive estimation branch for large images before resizing the transmission map back to full resolution.\n*** End Patch"
}
```

**Output:**
```
Success. Updated the following files:
M org/README.md
```

---

## Assistant (Build · GPT-5.4 · 23.6s)

_Thinking:_

**Running validation tasks**

I need to validate my files, which might mean reading the updated file — though maybe it's not necessary, just helpful to check the syntax. I could run a compile and sample on two Python files. I want to ensure the directory exists, so using bash for commands is a good idea. Running compile and demo in parallel might be efficient too, especially if I can execute the main script on the input directory. Let’s explore those options!

**Tool: bash**

**Input:**
```json
{
  "command": "python -m compileall \"Run_LowLight_Image_Enhancement_Pixel_Adaptive.py\" \"demo_enhancement.py\"",
  "timeout": 120000,
  "workdir": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org",
  "description": "Compiles updated Python scripts"
}
```

**Output:**
```
Compiling 'Run_LowLight_Image_Enhancement_Pixel_Adaptive.py'...
Compiling 'demo_enhancement.py'...

```

**Tool: bash**

**Input:**
```json
{
  "command": "python -c \"import cv2; from Run_LowLight_Image_Enhancement_Pixel_Adaptive import enhance_image; img=cv2.imread(r'input\\\\2.png', cv2.IMREAD_COLOR); out, details = enhance_image(img, 6.0, return_details=True); print(out.shape, round(details['gamma_max'], 3), round(details['runtime'], 3))\"",
  "timeout": 120000,
  "workdir": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org",
  "description": "Runs enhancement on sample image"
}
```

**Output:**
```
--- 0.493 seconds | gamma_max=5.28 | denoise_h=14 | scale=1.00 ---
(400, 600, 3) 5.279 0.493

```

---

## Assistant (Build · GPT-5.4 · 31.4s)

_Thinking:_

**Updating requirements and imports**

I’m considering the use of `cv2.erode` with a uint8 kernel and how that fits into the overall process. It looks like I don’t need `GetMin`, and for `Adjust`, using Python's max with numpy floats seems fine. I might need to handle the case if `InputImg` is None. The `build_parser` description could be blank, and even though there are platform-specific details for input/output paths, it’s manageable. 

I’ll also update the README to reflect that scikit-image is no longer needed and consider adding numpy and matplotlib. Re-checking the sample script's import order is on my list too.

_Thinking:_

**Patching README and requirements**

I’m planning to update the README. It might be a good idea to remove scikit-image from the main compilation as well. I'm thinking of updating the requirements list to include numpy and matplotlib instead. There’s also the possibility of opening an issue in the sample for further clarity. I’ll make sure to patch everything accordingly, so it’s accurate and reflects what’s actually being used. Keeping everything current is important!

I removed the `scikit-image` dependency from the core path, so I’m correcting the requirements list as well before I wrap up.

**Tool: apply_patch**

**Input:**
```json
{
  "patchText": "*** Begin Patch\n*** Update File: D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\README.md\n@@\n ### Requirements ###\n 1. Linux\n 2. Python (3.11.4)\n-3. scikit-image (0.20.0)\n-4. opencv (4.6.0)\n+3. numpy\n+4. opencv (4.6.0)\n+5. matplotlib (for `demo_enhancement.py`)\n*** End Patch"
}
```

**Output:**
```
Success. Updated the following files:
M org/README.md
```

---

## Assistant (Build · GPT-5.4 · 9.4s)

_Thinking:_

**Updating task statuses**

I think I need to update the statuses of my to-do list. It’s important to keep things organized and ensure I'm on track. I could start by reviewing what still needs to be done and marking off completed tasks. This way, I’ll have a clearer view of what’s left. Let’s see how I can efficiently tackle this, so everything is up to date! It should help me feel more accomplished.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Inspect current low-light enhancement pipeline and identify denoising, parameter, and performance hotspots",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Implement stronger noise removal with minimal disruption to existing pipeline",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Add automatic per-image parameter tuning for enhancement settings",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Optimize processing path for better throughput on larger inputs",
      "status": "completed",
      "priority": "medium"
    },
    {
      "content": "Run available verification commands or sample execution to validate changes",
      "status": "completed",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Inspect current low-light enhancement pipeline and identify denoising, parameter, and performance hotspots",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Implement stronger noise removal with minimal disruption to existing pipeline",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Add automatic per-image parameter tuning for enhancement settings",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Optimize processing path for better throughput on larger inputs",
    "status": "completed",
    "priority": "medium"
  },
  {
    "content": "Run available verification commands or sample execution to validate changes",
    "status": "completed",
    "priority": "high"
  }
]
```

---

## Assistant (Build · GPT-5.4 · 13.9s)

_Thinking:_

**Inspecting git changes**

I need to inspect the git diff and read around the changed sections for reference in the final output. I think it makes sense to start by reading around the first 260 lines of the main file, checking if the line numbers have been updated. I might also look at the demo files and maybe even include the README to gather more context. This should help in constructing a thorough response!

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\Run_LowLight_Image_Enhancement_Pixel_Adaptive.py",
  "offset": 1,
  "limit": 320
}
```

**Output:**
```
<path>D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\Run_LowLight_Image_Enhancement_Pixel_Adaptive.py</path>
<type>file</type>
<content>
1: import argparse
2: import os
3: import time
4: 
5: import cv2
6: import numpy as np
7: 
8: 
9: VALID_EXTENSIONS = (".jpg", ".jpeg", ".webp", ".tiff", ".tif", ".bmp", ".png")
10: 
11: 
12: def build_parser():
13:     parser = argparse.ArgumentParser(description="")
14:     parser.add_argument(
15:         "--input_dir",
16:         dest="InputPath",
17:         default="/home/ispl-public/Desktop/Dataset/LIME",
18:         help="directory for testing inputs",
19:     )
20:     parser.add_argument(
21:         "--output_dir",
22:         dest="OutputPath",
23:         default="./",
24:         help="directory for testing outputs",
25:     )
26:     parser.add_argument(
27:         "--gamma_max",
28:         dest="gamma_max",
29:         type=float,
30:         default=6.0,
31:         help="maximum gamma value used as an auto-tuning upper bound",
32:     )
33:     return parser
34: 
35: 
36: """ pixel value: i2f: 0-255 to 0-1, f2i: 0-1 to 0-255 """
37: 
38: 
39: def i2f(i_image):
40:     f_image = np.float32(i_image) / 255.0
41:     return f_image
42: 
43: 
44: def f2i(f_image):
45:     i_image = np.uint8(np.clip(f_image, 0.0, 1.0) * 255.0)
46:     return i_image
47: 
48: 
49: """ Compute 'A' as described by Tang et al. (CVPR 2014) """
50: 
51: 
52: def Compute_A_Tang(im):
53:     erosion_window = 15
54:     n_bins = 200
55: 
56:     dark = cv2.erode(
57:         np.min(im, axis=2), np.ones((erosion_window, erosion_window), dtype=np.uint8)
58:     )
59: 
60:     [h, edges] = np.histogram(dark, n_bins, [0, 1])
61:     numpixel = im.shape[0] * im.shape[1]
62:     thr_frac = numpixel * 0.99
63:     csum = np.cumsum(h)
64:     nz_idx = min(np.searchsorted(csum, thr_frac), n_bins - 1)
65:     dc_thr = edges[nz_idx]
66:     mask = dark >= dc_thr
67:     if not np.any(mask):
68:         mask = dark >= np.percentile(dark, 99)
69: 
70:     A = np.median(im[mask], axis=0, keepdims=True)
71: 
72:     return np.maximum(A, np.finfo(np.float32).eps)
73: 
74: 
75: def GetIntensity(fi):
76:     return np.mean(fi, axis=2)
77: 
78: 
79: def GetMax(fi):
80:     return np.max(fi, axis=2)
81: 
82: 
83: def GetMin(fi):
84:     return np.min(fi, axis=2)
85: 
86: 
87: """ Pixel Adaptive Gamma Correction """
88: 
89: 
90: def PixelAdaptiveGamma(InputImg, NormImg, amax):
91:     amin = 1
92:     xmax = 1
93:     xmin = 0
94:     Imax = GetMax(InputImg)
95: 
96:     a = (amax - amin) / (np.exp(-xmin) - np.exp(-xmax))
97:     b = amax - a * np.exp(-xmin)
98:     g2 = a * np.exp(-Imax) + b
99:     g1 = np.where(Imax < xmin, amax, g2)
100:     gamma = np.where(Imax > xmax, amin, g1)
101: 
102:     GCImg = np.power(NormImg, gamma[:, :, None])
103: 
104:     return GCImg, gamma
105: 
106: 
107: """ Estimate Transmission Map """
108: 
109: 
110: def EstimateTransmission(InputImg, NormImg, gamma_max=6):
111:     T_min = 0.1
112:     me = np.finfo(np.float32).eps
113:     hi = GetIntensity(NormImg)
114:     hmax = GetMax(NormImg)
115: 
116:     GCImg, gamma = PixelAdaptiveGamma(InputImg, NormImg, gamma_max)
117: 
118:     ji = GetIntensity(GCImg)
119:     jmax = GetMax(GCImg)
120: 
121:     tn = np.maximum(jmax * hi - hmax * ji, me)
122:     td = np.maximum((jmax - ji) * hi, me)
123: 
124:     Tmap = 1.0 - hi * (tn / td)
125: 
126:     return np.clip(Tmap, T_min, 1.0), gamma
127: 
128: 
129: """ Recover dehazed image """
130: 
131: 
132: def Recover(im, tmap, A):
133:     res = (im - 1.0 + A.reshape(1, 1, 3)) / tmap[:, :, None] + 1.0 - A.reshape(1, 1, 3)
134:     return np.clip(res, 0.0, 1.0)
135: 
136: 
137: """ Adjust image range """
138: 
139: 
140: def Adjust(im, perh, perl):
141:     im_h = np.percentile(im, perh)
142:     im_l = np.percentile(im, perl)
143:     aim = (im - im_l) / max(im_h - im_l, np.finfo(np.float32).eps)
144:     return np.clip(aim, 0.0, 1.0)
145: 
146: 
147: """ Normalize image 0 between 1 """
148: 
149: 
150: def Normalize(im):
151:     im_h = np.max(im, axis=(0, 1), keepdims=True)
152:     im_l = np.min(im, axis=(0, 1), keepdims=True)
153:     aim = (im - im_l) / np.maximum(im_h - im_l, np.finfo(np.float32).eps)
154:     return np.clip(aim, 0.0, 1.0)
155: 
156: 
157: def EstimateNoiseLevel(InputImg):
158:     gray = cv2.cvtColor(InputImg, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
159:     laplacian = cv2.Laplacian(gray, cv2.CV_32F, ksize=3)
160:     return float(np.median(np.abs(laplacian)) / 0.6745)
161: 
162: 
163: def AutoTuneParameters(InputImg, gamma_limit):
164:     gray = cv2.cvtColor(InputImg, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
165:     brightness = float(np.mean(gray))
166:     contrast = float(np.std(gray))
167:     noise_level = EstimateNoiseLevel(InputImg)
168: 
169:     darkness = np.clip((0.6 - brightness) / 0.6, 0.0, 1.0)
170:     contrast_penalty = np.clip((0.25 - contrast) / 0.25, 0.0, 1.0)
171:     noise_factor = np.clip(noise_level / 0.12, 0.0, 1.0)
172: 
173:     gamma_cap = max(float(gamma_limit), 1.0)
174:     gamma_drive = np.clip(
175:         0.7 * darkness + 0.3 * contrast_penalty + 0.2 * noise_factor, 0.15, 1.0
176:     )
177:     tuned_gamma_max = 1.0 + (gamma_cap - 1.0) * gamma_drive
178: 
179:     area = InputImg.shape[0] * InputImg.shape[1]
180:     target_pixels = 1280 * 720
181:     processing_scale = 1.0
182:     if area > target_pixels:
183:         processing_scale = float(np.sqrt(target_pixels / area))
184: 
185:     return {
186:         "brightness": brightness,
187:         "contrast": contrast,
188:         "noise_level": noise_level,
189:         "noise_factor": float(noise_factor),
190:         "darkness": float(darkness),
191:         "gamma_max": float(np.clip(tuned_gamma_max, 1.0, gamma_cap)),
192:         "denoise_h": int(np.clip(round(5 + 12 * noise_factor + 5 * darkness), 5, 20)),
193:         "denoise_h_color": int(
194:             np.clip(round(5 + 8 * noise_factor + 3 * darkness), 5, 16)
195:         ),
196:         "bilateral_sigma_color": int(
197:             np.clip(round(20 + 55 * (0.6 * noise_factor + 0.4 * darkness)), 20, 75)
198:         ),
199:         "bilateral_sigma_space": int(np.clip(round(7 + 8 * noise_factor), 7, 15)),
200:         "processing_scale": processing_scale,
201:         "adjust_high": 99.7 if darkness > 0.5 else 99.5,
202:         "adjust_low": 0.3 if contrast_penalty > 0.5 else 0.5,
203:     }
204: 
205: 
206: def ResizeImage(image, scale, interpolation):
207:     if scale >= 0.999:
208:         return image
209: 
210:     height, width = image.shape[:2]
211:     new_size = (
212:         max(1, int(round(width * scale))),
213:         max(1, int(round(height * scale))),
214:     )
215:     return cv2.resize(image, new_size, interpolation=interpolation)
216: 
217: 
218: def DenoiseImage(InputImg, params):
219:     if params["processing_scale"] < 0.9:
220:         small = ResizeImage(InputImg, params["processing_scale"], cv2.INTER_AREA)
221:         small_denoised = cv2.fastNlMeansDenoisingColored(
222:             small,
223:             None,
224:             params["denoise_h"],
225:             params["denoise_h_color"],
226:             7,
227:             21,
228:         )
229:         denoise_prior = cv2.resize(
230:             small_denoised,
231:             (InputImg.shape[1], InputImg.shape[0]),
232:             interpolation=cv2.INTER_LINEAR,
233:         )
234:         edge_preserved = cv2.bilateralFilter(
235:             InputImg,
236:             7,
237:             params["bilateral_sigma_color"],
238:             params["bilateral_sigma_space"],
239:         )
240:         denoised = cv2.addWeighted(edge_preserved, 0.6, denoise_prior, 0.4, 0)
241:     else:
242:         denoised = cv2.fastNlMeansDenoisingColored(
243:             InputImg,
244:             None,
245:             params["denoise_h"],
246:             params["denoise_h_color"],
247:             7,
248:             21,
249:         )
250: 
251:     if params["noise_factor"] > 0.3 or params["darkness"] > 0.45:
252:         denoised = cv2.bilateralFilter(
253:             denoised,
254:             5,
255:             params["bilateral_sigma_color"],
256:             params["bilateral_sigma_space"],
257:         )
258: 
259:     return denoised
260: 
261: 
262: """ Main """
263: 
264: 
265: def enhance_image(InputImg, gamma_max, return_details=False):
266:     start_time = time.time()
267:     params = AutoTuneParameters(InputImg, gamma_max)
268:     denoised_input = DenoiseImage(InputImg, params)
269:     base_float = i2f(denoised_input)
270: 
271:     working_float = ResizeImage(base_float, params["processing_scale"], cv2.INTER_AREA)
272:     DenoiseImg = 1.0 - working_float
273: 
274:     A = Compute_A_Tang(DenoiseImg)
275:     NormImg = Normalize(DenoiseImg / A.reshape(1, 1, 3))
276: 
277:     Transmap, gamma_map = EstimateTransmission(
278:         working_float, NormImg, params["gamma_max"]
279:     )
280:     if params["processing_scale"] < 0.999:
281:         target_size = (InputImg.shape[1], InputImg.shape[0])
282:         Transmap = cv2.resize(Transmap, target_size, interpolation=cv2.INTER_LINEAR)
283:         gamma_map = cv2.resize(gamma_map, target_size, interpolation=cv2.INTER_LINEAR)
284: 
285:     RecoverImg = Recover(base_float, Transmap, A)
286:     AdjustImg = Adjust(RecoverImg, params["adjust_high"], params["adjust_low"])
287: 
288:     end_time = time.time()
289:     details = {
290:         **params,
291:         "gamma_map": gamma_map,
292:         "transmission_map": Transmap,
293:         "runtime": end_time - start_time,
294:     }
295:     print(
296:         "--- %.3f seconds | gamma_max=%.2f | denoise_h=%d | scale=%.2f ---"
297:         % (
298:             details["runtime"],
299:             details["gamma_max"],
300:             details["denoise_h"],
301:             details["processing_scale"],
302:         )
303:     )
304: 
305:     if return_details:
306:         return AdjustImg, details
307:     return AdjustImg
308: 
309: 
310: def run_folder(InputPath, OutputPath, gamma_max):
311:     FolderTemp = os.path.normpath(InputPath).split(os.sep)
312:     output_dir = os.path.join(OutputPath, "Output", FolderTemp[-1])
313:     os.makedirs(output_dir, exist_ok=True, mode=0o777)
314: 
315:     FileList = sorted(
316:         [
317:             file
318:             for file in os.listdir(InputPath)
319:             if os.path.splitext(file)[1].lower() in VALID_EXTENSIONS
320:         ]

(Showing lines 1-320 of 338. Use offset=321 to continue.)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\demo_enhancement.py",
  "offset": 1,
  "limit": 220
}
```

**Output:**
```
<path>D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\demo_enhancement.py</path>
<type>file</type>
<content>
1: import cv2
2: import matplotlib.pyplot as plt
3: import os
4: 
5: from Run_LowLight_Image_Enhancement_Pixel_Adaptive import enhance_image, f2i
6: 
7: 
8: def compute_histogram(image):
9:     hist_b = cv2.calcHist([image], [0], None, [256], [0, 256])
10:     hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
11:     hist_r = cv2.calcHist([image], [2], None, [256], [0, 256])
12:     return hist_b, hist_g, hist_r
13: 
14: 
15: def demo_enhancement(image_path, output_dir="demo_output"):
16:     os.makedirs(output_dir, exist_ok=True)
17: 
18:     InputImg = cv2.imread(image_path, cv2.IMREAD_COLOR)
19:     if InputImg is None:
20:         print(f"Error: Could not load image from {image_path}")
21:         return
22: 
23:     print("Running enhancement...")
24:     EnhancedImg, details = enhance_image(InputImg, gamma_max=6.0, return_details=True)
25: 
26:     EnhancedImg_uint8 = f2i(EnhancedImg)
27:     gamma_map = details["gamma_map"]
28:     transmap = details["transmission_map"]
29: 
30:     fig, axes = plt.subplots(2, 3, figsize=(15, 10))
31:     fig.suptitle(
32:         "Low-Light Image Enhancement Demonstration", fontsize=16, fontweight="bold"
33:     )
34: 
35:     original_rgb = cv2.cvtColor(InputImg, cv2.COLOR_BGR2RGB)
36:     enhanced_rgb = cv2.cvtColor(EnhancedImg_uint8, cv2.COLOR_BGR2RGB)
37: 
38:     axes[0, 0].imshow(original_rgb)
39:     axes[0, 0].set_title("Original Low-Light Image", fontsize=12)
40:     axes[0, 0].axis("off")
41: 
42:     axes[0, 1].imshow(enhanced_rgb)
43:     axes[0, 1].set_title("Enhanced Result", fontsize=12)
44:     axes[0, 1].axis("off")
45: 
46:     gamma_display = gamma_map
47:     gamma_normalized = (gamma_display - gamma_display.min()) / (
48:         gamma_display.max() - gamma_display.min()
49:     )
50:     axes[0, 2].imshow(gamma_normalized, cmap="jet")
51:     axes[0, 2].set_title(
52:         "Pixel-Adaptive Gamma Map\n(Dark=High Gamma, Bright=Low Gamma)", fontsize=12
53:     )
54:     axes[0, 2].axis("off")
55:     plt.colorbar(axes[0, 2].images[0], ax=axes[0, 2], fraction=0.046, pad=0.04)
56: 
57:     hist_b, hist_g, hist_r = compute_histogram(InputImg)
58:     axes[1, 0].plot(hist_b, color="b", label="Blue", alpha=0.7)
59:     axes[1, 0].plot(hist_g, color="g", label="Green", alpha=0.7)
60:     axes[1, 0].plot(hist_r, color="r", label="Red", alpha=0.7)
61:     axes[1, 0].set_title("Original Histogram\n(Compressed/Low Contrast)", fontsize=12)
62:     axes[1, 0].set_xlabel("Pixel Intensity")
63:     axes[1, 0].set_ylabel("Frequency")
64:     axes[1, 0].legend()
65:     axes[1, 0].set_xlim([0, 256])
66: 
67:     hist_b_enh, hist_g_enh, hist_r_enh = compute_histogram(EnhancedImg_uint8)
68:     axes[1, 1].plot(hist_b_enh, color="b", label="Blue", alpha=0.7)
69:     axes[1, 1].plot(hist_g_enh, color="g", label="Green", alpha=0.7)
70:     axes[1, 1].plot(hist_r_enh, color="r", label="Red", alpha=0.7)
71:     axes[1, 1].set_title("Enhanced Histogram\n(Spread/Improved Contrast)", fontsize=12)
72:     axes[1, 1].set_xlabel("Pixel Intensity")
73:     axes[1, 1].set_ylabel("Frequency")
74:     axes[1, 1].legend()
75:     axes[1, 1].set_xlim([0, 256])
76: 
77:     axes[1, 2].imshow(transmap, cmap="viridis")
78:     axes[1, 2].set_title("Transmission Map", fontsize=12)
79:     axes[1, 2].axis("off")
80:     plt.colorbar(axes[1, 2].images[0], ax=axes[1, 2], fraction=0.046, pad=0.04)
81: 
82:     plt.tight_layout()
83: 
84:     output_path = os.path.join(output_dir, "demo_result.png")
85:     plt.savefig(output_path, dpi=150, bbox_inches="tight")
86:     print(f"Demo saved to: {output_path}")
87: 
88:     plt.show()
89: 
90:     print(
91:         "Auto-tuned gamma_max=%.2f, denoise_h=%d, scale=%.2f"
92:         % (
93:             details["gamma_max"],
94:             details["denoise_h"],
95:             details["processing_scale"],
96:         )
97:     )
98: 
99:     return EnhancedImg_uint8, gamma_map
100: 
101: 
102: if __name__ == "__main__":
103:     input_dir = "inputi"
104:     image_files = [f for f in os.listdir(input_dir) if f.endswith(".png")]
105: 
106:     if image_files:
107:         sample_image = os.path.join(input_dir, image_files[0])
108:         print(f"Processing: {sample_image}")
109:         enhanced_img, gamma_map = demo_enhancement(sample_image)
110: 
111:         print("\n=== Enhancement Complete ===")
112:         print("Key observations:")
113:         print(
114:             "1. Original: Low contrast, compressed histogram, loss of details in dark regions"
115:         )
116:         print(
117:             "2. Enhanced: Expanded dynamic range, improved brightness, restored details"
118:         )
119:         print(
120:             "3. Gamma Map: Darker regions have higher gamma values (brighter after correction)"
121:         )
122:         print("4. Histogram: Shows spreading indicating improved contrast")
123:     else:
124:         print("No images found in input directory")

(End of file - total 124 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\README.md",
  "offset": 1,
  "limit": 120
}
```

**Output:**
```
<path>D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\README.md</path>
<type>file</type>
<content>
1: # Low_Light_Pattern_Recognition
2: 
3: "[Low-Light Image Enhancement Using Gamma Correction Prior in Mixed Color Spaces](https://doi.org/10.1016/j.patcog.2023.110001)," Pattern Recognition
4: [Jong Ju Jeon](https://github.com/TripleJ2543)(triplej@pusan.ac.kr), Jun Young Park(jyp9917140@pusan.ac.kr), Il Kyu Eom*(ikeom@pusan.ac.kr)(https://sites.google.com/view/ispl-pnu)   
5: 
6: [Site](https://sites.google.com/view/ispl-pnu), [Paper](https://doi.org/10.1016/j.patcog.2023.110001)
7: 
8: 
9: ### Requirements ###
10: 1. Linux
11: 2. Python (3.11.4)
12: 3. numpy
13: 4. opencv (4.6.0)
14: 5. matplotlib (for `demo_enhancement.py`)
15: 
16: 
17: ### Usage ###
18: you can just run through
19: ```shell
20: python Run_LowLight_Image_Enhancement_Pixel_Adaptive.py 
21:     --input_dir=/path/to/your/dataset/dir/ \
22:     --output_dir=/path/to/save/results/ \
23:     --gamma_max=6                               # auto-tuning upper bound, defaults to 6
24: 
25: #python Run_LowLight.py --input_dir=/path/to/your/dataset/dir/ --output_dir=/path/to/save/results/ --gamma_max=6
26: 
27: ```
28: 
29: ### Enhancements ###
30: 1. Stronger noise removal
31:    The pipeline now applies an auto-tuned denoising stage before enhancement. It combines Non-Local Means with an edge-preserving bilateral pass so noise is reduced without flattening image structure.
32: 2. Automatic parameter tuning
33:    `gamma_max` is no longer used as a single fixed value for every image. It is treated as the upper bound for a per-image tuning step based on estimated brightness, contrast, and noise.
34: 3. Faster processing
35:    The implementation now removes several Python channel loops, uses OpenCV erosion for dark-channel estimation, and downsamples only the expensive estimation branch for large images before resizing the transmission map back to full resolution.
36: 
37: ### Citation ###
38: Jong Ju Jeon, Jun Young Park, Il Kyu Eom,   
39: Low-Light Image Enhancement Using Gamma Correction Prior in Mixed Color Spaces,   
40: Pattern Recognition,   
41: 2023,   
42: https://doi.org/10.1016/j.patcog.2023.110001.
43: (https://www.sciencedirect.com/science/article/pii/S0031320323006994)
44: 
45: Keywords: Low-light image enhancement; Inverted image; Atmospheric light; Normalization; Transmission map; Retinex model; HSV color space; HSI color space; Gamma correction   

(End of file - total 45 lines)
</content>
```

---

## Assistant (Build · GPT-5.4 · 17.8s)

_Thinking:_

**Addressing potential bugs**

I noticed a potential issue with line 47 where the denominator for gamma normalization could be at risk of becoming zero, which is definitely a bug. I plan to patch that to avoid division by zero. I'm also looking at `input_dir="inputi"`; the sample images appear to be under `inputi/input`. However, I might need to adjust the script if it isn't finding any images there. It seems like something's going on with how `glob` is reading the directories — perhaps it isn't looking into nested folders correctly. I'll inspect the directory listing to clarify.

I found one small demo edge case while reviewing the updated files, and I’m fixing it so the visualizer doesn’t break on constant maps or the bundled input layout.

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\inputi",
  "offset": 1,
  "limit": 50
}
```

**Output:**
```
<path>D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi</path>
<type>directory</type>
<entries>
input/

(1 entries)
</entries>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\inputi\\input",
  "offset": 1,
  "limit": 20
}
```

**Output:**
```
<path>D:\clg\ipa\paper\Low_Light_Pattern_Recognition_2023\org\inputi\input</path>
<type>directory</type>
<entries>
10.png
12.png
13.png
14.png
15.png
16.png
17.png
18.png
2.png
21.png
24.png
25.png
26.png
27.png
28.png
33.png
35.png
36.png
38.png
39.png

(Showing 20 of 48 entries. Use 'offset' parameter to read beyond entry 21)
</entries>
```

---

## Assistant (Build · GPT-5.4 · 13.6s)

_Thinking:_

**Evaluating patch demos**

I'm considering the steps to patch the demo by adjusting the input directory and implementing gamma normalization for better division. I want to ensure everything works seamlessly together, so getting these details right is key. Oh, I hope I don’t mess up the directory structure! Normalization can make a real difference, but I need to double-check that it aligns with the overall setup. It’s all in the details, right?

**Tool: apply_patch**

**Input:**
```json
{
  "patchText": "*** Begin Patch\n*** Update File: D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org\\demo_enhancement.py\n@@\n     gamma_display = gamma_map\n-    gamma_normalized = (gamma_display - gamma_display.min()) / (\n-        gamma_display.max() - gamma_display.min()\n-    )\n+    gamma_span = max(gamma_display.max() - gamma_display.min(), 1e-6)\n+    gamma_normalized = (gamma_display - gamma_display.min()) / gamma_span\n@@\n if __name__ == \"__main__\":\n-    input_dir = \"inputi\"\n+    input_dir = os.path.join(\"inputi\", \"input\")\n*** End Patch"
}
```

**Output:**
```
Success. Updated the following files:
M org/demo_enhancement.py
```

---

## Assistant (Build · GPT-5.4 · 22.4s)

_Thinking:_



**Tool: bash**

**Input:**
```json
{
  "command": "python -m compileall \"Run_LowLight_Image_Enhancement_Pixel_Adaptive.py\" \"demo_enhancement.py\"",
  "timeout": 120000,
  "workdir": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org",
  "description": "Recompiles updated Python scripts"
}
```

**Tool: bash**

**Input:**
```json
{
  "command": "python -c \"from demo_enhancement import demo_enhancement; print(demo_enhancement.__name__)\"",
  "timeout": 120000,
  "workdir": "D:\\clg\\ipa\\paper\\Low_Light_Pattern_Recognition_2023\\org",
  "description": "Imports demo module successfully"
}
```

**Output:**
```
demo_enhancement

```

---

## Assistant (Build · GPT-5.4 · 34.4s)

_Thinking:_



Implemented the three enhancements across the project.

**What Changed**
- Better noise removal:
  `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py:157-259`
  Added per-image noise estimation and a stronger denoising stage that auto-tunes `fastNlMeansDenoisingColored` and adds an edge-preserving bilateral pass when needed.
- Automatic parameter tuning:
  `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py:163-203`
  `gamma_max` is now treated as an upper bound, and the actual gamma is chosen per image from brightness, contrast, and noise.
- Faster processing:
  `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py:52-154`
  `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py:179-183`
  `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py:271-283`
  Replaced slower morphology usage with OpenCV erosion, removed channel loops with vectorized NumPy ops, and added a reduced-resolution estimation path for large images.

**Other Updates**
- `demo_enhancement.py:5-29`
  The demo now uses the same upgraded core pipeline.
- `demo_enhancement.py:46-49`, `77-80`, `102-109`
  Fixed gamma-map normalization, transmission map display, and the sample input path.
- `README.md:9-35`
  Documented the new behavior and updated requirements.

**Verification**
- `python -m compileall "Run_LowLight_Image_Enhancement_Pixel_Adaptive.py" "demo_enhancement.py"`
- Sample execution on `input\\2.png` succeeded:
  output shape `(400, 600, 3)`, auto-tuned `gamma_max=5.279`, runtime about `0.493s`

If you want, I can also add a small batch benchmark script to compare old vs new runtime on the dataset.

---

## User

is @demo_enhancement.py and @Run_LowLight_Image_Enhancement_Pixel_Adaptive.py same?

---

## Assistant (Build · GPT-5.4 · 18.8s)

_Thinking:_

**Clarifying demo and run files**

The user wants to know if the demo and run files are the same. I need to explain that they are not the same, but they share core enhancements. The demo imports `enhance_image` and `f2i` from the run file. Essentially, the demo serves as a visualization wrapper for a single image and plots histograms related to gamma transmission. In contrast, the run file contains the actual algorithm and batch CLI. Before my change, there was a duplication in implementation, but now the demo correctly delegates to the core, ensuring the output uses the same algorithm. I'll keep the answer concise and include relevant references.

No.

They now use the same enhancement algorithm, but they serve different purposes.

- `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py`
  - Main implementation file
  - Contains the full pipeline: `enhance_image(...)` at `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py:265`
  - Supports folder/batch processing via CLI: `run_folder(...)` at `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py:310`

- `demo_enhancement.py`
  - Demo/visualization wrapper
  - Imports the core logic from the main file at `demo_enhancement.py:5`
  - Runs one image, then displays:
    - original vs enhanced image
    - gamma map
    - transmission map
    - histograms

So:

- Same algorithm output path: yes
- Same file / same role: no

In fact, `demo_enhancement.py` now depends on `Run_LowLight_Image_Enhancement_Pixel_Adaptive.py` instead of re-implementing the algorithm, which is better because there is only one source of truth.

---

