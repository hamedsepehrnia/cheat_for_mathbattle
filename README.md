````markdown
# Auto Equation Checker

A Python script that automatically detects and verifies mathematical equations displayed on screen, then clicks the correct or wrong button accordingly.

## Features

- Takes a screenshot of a specific screen region containing an equation.
- Uses OCR (Tesseract) to extract the equation text.
- Processes and sanitizes the extracted text.
- Checks if the equation is mathematically correct.
- Clicks the appropriate button on screen (correct or wrong) based on the result.

## Requirements

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed (Windows path example: `C:\Program Files\Tesseract-OCR\tesseract.exe`)
- Python packages:
  - `pyautogui`
  - `pytesseract`
  - `opencv-python`
  - `numpy`
  - `Pillow`

## Installation

1. Install Tesseract OCR from its official page and note the installation path.

2. Install Python packages:

```bash
pip install pyautogui pytesseract opencv-python numpy Pillow
````

## Usage

1. Update the Tesseract path in the script if needed:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

2. Adjust the coordinates of the equation region and buttons if necessary.

3. Run the script:

```bash
python your_script_name.py
```

4. The script will start after a 3-second delay. It continuously detects and verifies equations on the screen and clicks the corresponding buttons.

5. Press `Ctrl + C` to exit.

## Notes

* Make sure the coordinates (`TOP_LEFT`, `BOTTOM_RIGHT`, `CORRECT_BUTTON`, `WRONG_BUTTON`) match your screen setup and application.
* This script assumes the equation is displayed in a fixed region and buttons are at fixed positions.
