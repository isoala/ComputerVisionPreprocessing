# Computer Vision Preprocessing

## Overview
This program provides a command-line tool for image preprocessing and enhancement using computer vision techniques. It is designed to help users clean, filter, and improve images, especially those affected by salt-and-pepper noise or other artifacts. The processed images are displayed in a grid format for easy comparison.

## Features
- Loads an input image (PNG, JPG, etc.)
- Applies multiple filters: Gaussian, Median, Bilateral
- Performs thresholding and contrast enhancement
- Denoises images using Non-Local Means
- Arranges processed images in a 3x3 grid with captions
- Uses default font for captions (cross-platform reliability)
- Command-line interface for easy use

## Requirements
- Python 3.9+
- OpenCV (`cv2`)
- NumPy
- Pillow (`PIL`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/isoala/ComputerVisionPreprocessing.git
   cd ComputerVisionPreprocessing
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your input image (e.g., `salt.png`) in the project directory.
2. Run the program:
   ```bash
   python computer_vision_preprocessing.py
   ```
3. Follow the prompts to select and process your image.
4. The output will display a 3x3 grid of processed images with captions.

## Example
```
$ python computer_vision_preprocessing.py
Enter the path to your image: salt.png
Processing...
[Displays grid of images]
```

## Troubleshooting
- If you see errors about missing packages, ensure you have installed all dependencies.
- For font issues, the program defaults to a reliable system font.
- For git issues, make sure your local branch matches the remote before pushing or pulling.

## License
MIT License

## Author
isoala
