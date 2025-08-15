import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

def resize_to_shape(image, shape):
	return cv2.resize(image, (shape[1], shape[0]))

def to_bgr(image):
	if len(image.shape) == 2:
		return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
	return image

def add_caption(image, text):
	img_copy = image.copy()
	pil_img = Image.fromarray(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
	draw = ImageDraw.Draw(pil_img)
	try:
		font = ImageFont.truetype("./cv_unsalt/garamond.ttf", 24)
	except Exception as e:
		print("Could not load garamond.ttf, using default font.")
		font = ImageFont.load_default()
	draw.rectangle([0, 0, pil_img.width, 35], fill=(0, 0, 0))
	draw.text((10, 5), text, font=font, fill=(255, 255, 255))
	return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

target_shape = (300, 300)


while True:
	try:
		image_path = input("Enter the path to the image file (or type 'exit' to quit): ")
		if image_path.strip().lower() == 'exit':
			print("Exiting program.")
			break
		img_color = cv2.imread(image_path)
		if img_color is None:
			print(f"Error: Could not open image '{image_path}'.")
			continue
		# Filters (color)
		gaussian = cv2.GaussianBlur(img_color, (5,5), 0)
		median = cv2.medianBlur(img_color, 5)
		bilateral = cv2.bilateralFilter(img_color, 9, 75, 75)

		# Thresholding and Contrast Enhancement (grayscale)
		img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
		# Thresholding
		_, thresh_simple = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
		thresh_adaptive = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
		_, thresh_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
		# Contrast Enhancement
		hist_eq = cv2.equalizeHist(img_gray)
		clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
		clahe_img = clahe.apply(img_gray)

		# Denoising
		denoised = cv2.fastNlMeansDenoising(img_gray, None, 30, 7, 21)

		# Resize all images to same size
		img_r = resize_to_shape(img_color, target_shape)
		gaussian_r = resize_to_shape(gaussian, target_shape)
		median_r = resize_to_shape(median, target_shape)
		bilateral_r = resize_to_shape(bilateral, target_shape)
		thresh_simple_r = resize_to_shape(to_bgr(thresh_simple), target_shape)
		thresh_adaptive_r = resize_to_shape(to_bgr(thresh_adaptive), target_shape)
		thresh_otsu_r = resize_to_shape(to_bgr(thresh_otsu), target_shape)
		hist_eq_r = resize_to_shape(to_bgr(hist_eq), target_shape)
		clahe_img_r = resize_to_shape(to_bgr(clahe_img), target_shape)
		denoised_r = resize_to_shape(to_bgr(denoised), target_shape)

		# Add captions
		img_r = add_caption(img_r, "Original (Color)")
		gaussian_r = add_caption(gaussian_r, "Gaussian Blur")
		median_r = add_caption(median_r, "Median Filtering")
		bilateral_r = add_caption(bilateral_r, "Bilateral Filtering")
		thresh_simple_r = add_caption(thresh_simple_r, "Simple Threshold")
		thresh_adaptive_r = add_caption(thresh_adaptive_r, "Adaptive Threshold")
		thresh_otsu_r = add_caption(thresh_otsu_r, "Otsu's Threshold")
		hist_eq_r = add_caption(hist_eq_r, "Histogram Equalization")
		clahe_img_r = add_caption(clahe_img_r, "CLAHE")
		denoised_r = add_caption(denoised_r, "Denoised (NL Means)")

		# Arrange all images in a 3x3 grid
		row1 = np.hstack((img_r, gaussian_r, median_r))
		row2 = np.hstack((bilateral_r, thresh_simple_r, thresh_adaptive_r))
		row3 = np.hstack((thresh_otsu_r, hist_eq_r, clahe_img_r))
		grid_3x3 = np.vstack((row1, row2, row3))
		cv2.imshow("All Filters 3x3 Grid", grid_3x3)

		cv2.waitKey(0)
		cv2.destroyAllWindows()
	except Exception as error:
		print(f"An error occurred: {error}")
		print("Please enter a valid image path or type 'exit' to quit.")