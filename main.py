import pyautogui
import pytesseract
import cv2
import numpy as np
from PIL import Image
import re
import time

# مسیر Tesseract رو مشخص کن (برای ویندوز)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# مختصات بالا سمت چپ و پایین سمت راست منطقه‌ای که معادله نمایش داده می‌شه
TOP_LEFT = (685, 237)  # بالا سمت چپ (x1, y1)
BOTTOM_RIGHT = (1023, 386)  # پایین سمت راست (x2, y2)

# محاسبه مختصات مورد نیاز برای اسکرین‌شات
EQUATION_REGION = (TOP_LEFT[0], TOP_LEFT[1], BOTTOM_RIGHT[0] - TOP_LEFT[0], BOTTOM_RIGHT[1] - TOP_LEFT[1])

# مختصات دکمه‌ها
CORRECT_BUTTON = (776, 551)  # دکمه صحیح (مختصات x, y)
WRONG_BUTTON = (940, 542)  # دکمه غلط (مختصات x, y)


def preprocess_image(image):
    """پیش‌پردازش تصویر برای بهبود دقت تشخیص."""
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)
    return Image.fromarray(threshold_image)


def sanitize_equation(equation):
    """اصلاح معادله شامل جایگزینی کاراکترهای خاص مانند \u00d7 با * و تبدیل پرانتزها به اعداد مشابه."""
    equation = equation.replace(' ', '')  # حذف فاصله‌های اضافی
    equation = equation.replace('-0', '-').replace('0-', '0')
    equation = equation.replace('(', '1').replace(')', '1')
    equation = equation.replace('[', '1').replace(']', '1')
    equation = equation.replace('{', '1').replace('}', '1')
    equation = equation.replace('\u00d7', '*').replace('x', '*')
    equation = equation.replace('+=', '=').replace('-=', '=')

    # حذف کاراکترهای غیرمجاز
    allowed_chars = re.compile(r'[0-9+\-*/=]')
    sanitized = ''.join(filter(allowed_chars.match, equation))
    return sanitized.strip()


def get_equation_text():
    """متن معادله رو از صفحه‌نمایش تشخیص می‌ده."""
    screenshot = pyautogui.screenshot(region=EQUATION_REGION)
    image = preprocess_image(screenshot)
    equation_text = pytesseract.image_to_string(image, config='--psm 6')
    sanitized_text = sanitize_equation(equation_text)
    return sanitized_text


def check_equation(equation):
    """درستی معادله رو بررسی می‌کنه."""
    try:
        if "=" not in equation:
            return False
        left, right = equation.split("=")
        left = left.strip()
        right = right.strip()

        # جلوگیری از وارد شدن معادلات نادرست
        if not left or not right:
            return False
        return eval(left) == eval(right)
    except Exception as e:
        print(f"Error checking equation: {e}")
        return False


def click_button(position):
    """موس رو به مختصات مورد نظر می‌بره و کلیک می‌کنه."""
    pyautogui.moveTo(position)
    pyautogui.click()


print("Program started. Press Ctrl + C to exit.")
time.sleep(3)  # تاخیر برای آماده‌سازی

try:
    while True:
        equation = get_equation_text()
        print(f"Detected Equation: {equation}")

        if check_equation(equation):
            print("Equation is correct. Clicking CORRECT button.")
            click_button(CORRECT_BUTTON)
        else:
            print("Equation is wrong. Clicking WRONG button.")
            click_button(WRONG_BUTTON)

        time.sleep(0.1)  # افزایش تاخیر برای جلوگیری از عملکرد نادرست
except KeyboardInterrupt:
    print("Program exited.")
