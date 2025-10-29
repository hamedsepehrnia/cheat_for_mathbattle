# Math Battle Auto Checker
# تشخیص خودکار معادلات ریاضی

<div dir="rtl">

## 📋 فهرست مطالب / Table of Contents

- [معرفی / Introduction](#معرفی--introduction)
- [قابلیت‌ها / Features](#قابلیت‌ها--features)
- [الزامات / Requirements](#الزامات--requirements)
- [نصب و راه‌اندازی / Installation](#نصب-و-راه‌اندازی--installation)
- [راهنمای استفاده / Usage](#راهنمای-استفاده--usage)
- [تنظیمات / Configuration](#تنظیمات--configuration)
- [مشکلات رایج / Troubleshooting](#مشکلات-رایج--troubleshooting)
- [ملاحظات امنیتی / Security Notes](#ملاحظات-امنیتی--security-notes)
- [مجوز / License](#مجوز--license)

---

## معرفی / Introduction

<div dir="rtl">

**پرشی:**

این یک برنامه خودکار برای تشخیص و بررسی معادلات ریاضی در بازی Math Battle است. برنامه با استفاده از OCR (تشخیص متن از تصویر) معادلات را از روی صفحه تشخیص می‌دهد، آن‌ها را بررسی می‌کند و به صورت خودکار روی دکمه صحیح یا غلط کلیک می‌کند.

**English:**

This is an automated tool for detecting and verifying mathematical equations in Math Battle game. The program uses OCR (Optical Character Recognition) to extract equations from the screen, verifies them, and automatically clicks on the correct or wrong button.

</div>

---

## قابلیت‌ها / Features

<div dir="rtl">

**پرشی:**

- ✅ رابط کاربری گرافیکی با Tkinter
- ✅ تشخیص خودکار معادلات از صفحه نمایش با OCR
- ✅ بررسی خودکار صحت معادلات ریاضی
- ✅ کلیک خودکار روی دکمه‌های صحیح/غلط
- ✅ تنظیمات کامل مختصات منطقه معادله و دکمه‌ها
- ✅ تست مختصات و OCR قبل از شروع عملیات
- ✅ نمایش لاگ عملیات به صورت زنده
- ✅ پشتیبانی از سیستم‌عامل‌های Windows، Linux و macOS
- ✅ کد تمیز و استاندارد با معماری شی‌گرا

**English:**

- ✅ Graphical user interface with Tkinter
- ✅ Automatic equation detection from screen using OCR
- ✅ Automatic verification of mathematical equations
- ✅ Automatic clicking on correct/wrong buttons
- ✅ Full configuration for equation region and button coordinates
- ✅ Test coordinates and OCR before starting operations
- ✅ Real-time operation logs display
- ✅ Support for Windows, Linux, and macOS
- ✅ Clean and standardized object-oriented code

</div>

---

## الزامات / Requirements

<div dir="rtl">

**پرشی:**

### نرم‌افزارهای مورد نیاز:
- Python 3.7 یا بالاتر
- Tesseract OCR (برای تشخیص متن از تصویر)

### کتابخانه‌های Python:
- `pyautogui` - برای کنترل ماوس و گرفتن اسکرین‌شات
- `pytesseract` - رابط Python برای Tesseract OCR
- `opencv-python` - برای پردازش تصویر
- `numpy` - برای عملیات ریاضی روی آرایه‌ها
- `Pillow` - برای کار با تصاویر
- `tkinter` - برای رابط کاربری گرافیکی (معمولاً با Python نصب می‌شود)

**English:**

### Required Software:
- Python 3.7 or higher
- Tesseract OCR (for text recognition from images)

### Python Libraries:
- `pyautogui` - for mouse control and screenshots
- `pytesseract` - Python interface for Tesseract OCR
- `opencv-python` - for image processing
- `numpy` - for mathematical operations on arrays
- `Pillow` - for image manipulation
- `tkinter` - for graphical user interface (usually comes with Python)

</div>

---

## نصب و راه‌اندازی / Installation

<div dir="rtl">

### مرحله 1: نصب Tesseract OCR

**ویندوز:**
1. دانلود Tesseract از [صفحه رسمی](https://github.com/UB-Mannheim/tesseract/wiki)
2. نصب فایل اجرایی (معمولاً در `C:\Program Files\Tesseract-OCR\`)
3. مسیر نصب را به PATH اضافه کنید (اختیاری)

**لینوکس (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

**لینوکس (Fedora):**
```bash
sudo dnf install tesseract
```

**macOS:**
```bash
brew install tesseract
```

### مرحله 2: نصب tkinter (در صورت نیاز)

tkinter معمولاً با Python نصب می‌شود، اما در برخی توزیع‌های لینوکس ممکن است نیاز به نصب جداگانه داشته باشد:

**لینوکس (Ubuntu/Debian):**
```bash
sudo apt-get install python3-tk
```

**لینوکس (Fedora):**
```bash
sudo dnf install python3-tkinter
```

**ویندوز و macOS:** tkinter معمولاً با Python پیش‌نصب است.

### مرحله 3: نصب کتابخانه‌های Python

```bash
pip install pyautogui pytesseract opencv-python numpy Pillow
```

یا با استفاده از `requirements.txt`:

```bash
pip install -r requirements.txt
```

**English:**

### Step 1: Install Tesseract OCR

**Windows:**
1. Download Tesseract from [official page](https://github.com/UB-Mannheim/tesseract/wiki)
2. Install the executable (usually in `C:\Program Files\Tesseract-OCR\`)
3. Add installation path to PATH (optional)

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

**Linux (Fedora):**
```bash
sudo dnf install tesseract
```

**macOS:**
```bash
brew install tesseract
```

### Step 2: Install tkinter (if needed)

tkinter usually comes with Python, but on some Linux distributions it may need separate installation:

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-tk
```

**Linux (Fedora):**
```bash
sudo dnf install python3-tkinter
```

**Windows and macOS:** tkinter is usually pre-installed with Python.

### Step 3: Install Python Libraries

```bash
pip install pyautogui pytesseract opencv-python numpy Pillow
```

Or using `requirements.txt`:

```bash
pip install -r requirements.txt
```

</div>

---

## راهنمای استفاده / Usage

<div dir="rtl">

### اجرای برنامه:

```bash
python main.py
```

### مراحل استفاده:

1. **تنظیم مسیر Tesseract:**
   - اگر مسیر به صورت خودکار پیدا نشد، روی دکمه "انتخاب فایل" کلیک کنید و مسیر `tesseract.exe` را انتخاب کنید.

2. **تنظیم مختصات:**
   - مختصات بالا-چپ و پایین-راست منطقه معادله را وارد کنید.
   - مختصات دکمه صحیح و غلط را وارد کنید.

3. **تست قبل از استفاده:**
   - روی دکمه "تست مختصات" کلیک کنید تا مطمئن شوید مختصات درست است.
   - روی دکمه "تست OCR" کلیک کنید تا دقت تشخیص متن را بررسی کنید.

4. **شروع عملیات:**
   - روی دکمه "شروع" کلیک کنید.
   - برنامه به طور خودکار شروع به بررسی معادلات می‌کند.
   - لاگ عملیات در قسمت پایین نمایش داده می‌شود.

5. **توقف برنامه:**
   - روی دکمه "تست" کلیک کنید تا برنامه متوقف شود.

### نکات مهم:

- قبل از شروع، مطمئن شوید بازی Math Battle باز است و در حالت مناسب قرار دارد.
- مختصات را با دقت تنظیم کنید تا برنامه بتواند معادله را به درستی تشخیص دهد.
- از تنظیمات "تست مختصات" برای اطمینان از صحت مختصات استفاده کنید.

**English:**

### Running the Program:

```bash
python main.py
```

### Usage Steps:

1. **Configure Tesseract Path:**
   - If the path is not automatically detected, click "Browse" button and select the path to `tesseract.exe`.

2. **Configure Coordinates:**
   - Enter the top-left and bottom-right coordinates of the equation region.
   - Enter the coordinates of the correct and wrong buttons.

3. **Test Before Use:**
   - Click "Test Coordinates" button to verify coordinates are correct.
   - Click "Test OCR" button to check text recognition accuracy.

4. **Start Operation:**
   - Click "Start" button.
   - The program will automatically start checking equations.
   - Operation logs will be displayed in the bottom section.

5. **Stop Program:**
   - Click "Stop" button to stop the program.

### Important Notes:

- Before starting, make sure Math Battle game is open and in the appropriate state.
- Configure coordinates carefully so the program can detect equations correctly.
- Use "Test Coordinates" settings to ensure coordinate accuracy.

</div>

---

## تنظیمات / Configuration

<div dir="rtl">

### تنظیمات پیش‌فرض:

برنامه دارای تنظیمات پیش‌فرض برای مختصات است که می‌توانید آن‌ها را تغییر دهید:

- **منطقه معادله:** بالا-چپ: (685, 237) | پایین-راست: (1023, 386)
- **دکمه صحیح:** (776, 551)
- **دکمه غلط:** (940, 542)

### تغییر تنظیمات در کد:

می‌توانید در کلاس `Config` در فایل `main.py` تنظیمات پیش‌فرض را تغییر دهید:

```python
class Config:
    DEFAULT_TOP_LEFT = (685, 237)
    DEFAULT_BOTTOM_RIGHT = (1023, 386)
    DEFAULT_CORRECT_BUTTON = (776, 551)
    DEFAULT_WRONG_BUTTON = (940, 542)
    INITIAL_DELAY = 3  # تأخیر قبل از شروع (ثانیه)
    LOOP_DELAY = 0.1  # تأخیر بین هر بررسی (ثانیه)
```

**English:**

### Default Settings:

The program has default settings for coordinates that you can change:

- **Equation Region:** Top-Left: (685, 237) | Bottom-Right: (1023, 386)
- **Correct Button:** (776, 551)
- **Wrong Button:** (940, 542)

### Changing Settings in Code:

You can modify default settings in the `Config` class in `main.py`:

```python
class Config:
    DEFAULT_TOP_LEFT = (685, 237)
    DEFAULT_BOTTOM_RIGHT = (1023, 386)
    DEFAULT_CORRECT_BUTTON = (776, 551)
    DEFAULT_WRONG_BUTTON = (940, 542)
    INITIAL_DELAY = 3  # Delay before starting (seconds)
    LOOP_DELAY = 0.1  # Delay between each check (seconds)
```

</div>

---

## مشکلات رایج / Troubleshooting

<div dir="rtl">

### مشکل: مسیر Tesseract پیدا نمی‌شود

**راه‌حل:**
- مسیر Tesseract را به صورت دستی در قسمت تنظیمات وارد کنید.
- مطمئن شوید Tesseract نصب شده است.
- در سیستم عامل لینوکس، از دستور `which tesseract` برای یافتن مسیر استفاده کنید.

### مشکل: معادله به درستی تشخیص داده نمی‌شود

**راه‌حل:**
- مختصات منطقه معادله را دوباره بررسی کنید.
- از دکمه "تست OCR" استفاده کنید تا ببینید چه متنی تشخیص داده می‌شود.
- ممکن است نیاز به تنظیم پارامترهای OCR باشد (در کلاس `Config`).

### مشکل: برنامه روی دکمه‌های اشتباه کلیک می‌کند

**راه‌حل:**
- مختصات دکمه‌ها را با استفاده از ابزارهای سیستم عامل بررسی کنید.
- از دکمه "تست مختصات" برای نمایش موقعیت‌های تنظیم شده استفاده کنید.

### مشکل: برنامه کند کار می‌کند

**راه‌حل:**
- می‌توانید `LOOP_DELAY` را کاهش دهید (اما نه خیلی کم).
- مطمئن شوید سیستم شما منابع کافی دارد.

### مشکل: خطای X11 Display Connection (لینوکس)

**خطا:**
```
Xlib.error.DisplayConnectionError: Can't connect to display ":0": b'Authorization required, but no authorization protocol specified'
```

**راه‌حل:**
این مشکل معمولاً در لینوکس هنگام استفاده از `pyautogui` رخ می‌دهد. برای حل آن:

```bash
xhost +
```

این دستور دسترسی به X11 display را برای همه کلاینت‌ها باز می‌کند. برای بازگشت به حالت امن‌تر بعد از استفاده:

```bash
xhost -
```

**نکته امنیتی:** دستور `xhost +` دسترسی را برای همه باز می‌کند. اگر می‌خواهید فقط کاربر فعلی دسترسی داشته باشد، می‌توانید از `xhost +SI:localuser:$(whoami)` استفاده کنید.

**English:**

### Issue: Tesseract path not found

**Solution:**
- Manually enter the Tesseract path in settings.
- Make sure Tesseract is installed.
- On Linux, use `which tesseract` command to find the path.

### Issue: Equation not detected correctly

**Solution:**
- Recheck the equation region coordinates.
- Use "Test OCR" button to see what text is being detected.
- You may need to adjust OCR parameters (in `Config` class).

### Issue: Program clicks on wrong buttons

**Solution:**
- Check button coordinates using OS tools.
- Use "Test Coordinates" button to display configured positions.

### Issue: Program runs slowly

**Solution:**
- You can reduce `LOOP_DELAY` (but not too much).
- Make sure your system has adequate resources.

### Issue: X11 Display Connection Error (Linux)

**Error:**
```
Xlib.error.DisplayConnectionError: Can't connect to display ":0": b'Authorization required, but no authorization protocol specified'
```

**Solution:**
This error usually occurs on Linux when using `pyautogui`. To fix it:

```bash
xhost +
```

This command opens X11 display access for all clients. To revert to a more secure state after use:

```bash
xhost -
```

**Security Note:** The `xhost +` command opens access for everyone. If you want only the current user to have access, you can use `xhost +SI:localuser:$(whoami)`.

</div>

---

## ملاحظات امنیتی / Security Notes

<div dir="rtl">

⚠️ **هشدار مهم:**

1. این برنامه برای استفاده آموزشی و شخصی است.
2. استفاده از این برنامه ممکن است قوانین بازی Math Battle را نقض کند.
3. استفاده از این برنامه به عهده کاربر است.
4. از این برنامه در مسابقات رسمی استفاده نکنید.

**English:**

⚠️ **Important Warning:**

1. This program is for educational and personal use.
2. Using this program may violate Math Battle game rules.
3. Use of this program is at your own risk.
4. Do not use this program in official competitions.

</div>

---

## مجوز / License

<div dir="rtl">

این پروژه برای استفاده آزاد و آموزشی منتشر شده است. استفاده به عهده خود شماست.

**English:**

This project is released for free and educational use. Use at your own risk.

</div>

---

## مشارکت / Contributing

<div dir="rtl">

اگر می‌خواهید در بهبود این پروژه مشارکت کنید، می‌توانید:

1. Issues را گزارش کنید
2. پیشنهادات خود را ارائه دهید
3. Pull Request ارسال کنید

**English:**

If you want to contribute to improving this project, you can:

1. Report issues
2. Provide suggestions
3. Submit Pull Requests

</div>

---

## پشتیبانی / Support

<div dir="rtl">

برای سوالات و مشکلات می‌توانید Issue در GitHub ایجاد کنید.

**English:**

For questions and issues, you can create an Issue on GitHub.

</div>

---

<div dir="rtl">

**نوشته شده با ❤️ برای جامعه توسعه‌دهندگان**

**Written with ❤️ for the developer community**

</div>
