"""
Configuration management module
"""


class Config:
    """Configuration management class"""
    
    # Default Tesseract paths for different operating systems
    TESSERACT_PATHS = {
        'Windows': r'C:\Program Files\Tesseract-OCR\tesseract.exe',
        'Linux': '/usr/bin/tesseract',
        'Darwin': '/usr/local/bin/tesseract'
    }
    
    # Default coordinate settings
    DEFAULT_TOP_LEFT = (685, 237)
    DEFAULT_BOTTOM_RIGHT = (1023, 386)
    DEFAULT_CORRECT_BUTTON = (776, 551)
    DEFAULT_WRONG_BUTTON = (940, 542)
    
    # OCR settings
    OCR_PSM = 6
    THRESHOLD_VALUE = 150
    THRESHOLD_MAX = 255
    
    # Timing settings
    INITIAL_DELAY = 3
    LOOP_DELAY = 0.1

