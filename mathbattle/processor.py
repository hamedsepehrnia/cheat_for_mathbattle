"""
Image processing and OCR module
"""

import pytesseract
import cv2
import numpy as np
import platform
import os
from typing import Optional
from PIL import Image

from mathbattle.config import Config


class ImageProcessor:
    """Image processing and OCR class"""
    
    def __init__(self, tesseract_path: Optional[str] = None):
        """Initialize image processor"""
        self.tesseract_path = tesseract_path or self._find_tesseract()
        if self.tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = self.tesseract_path
    
    def _find_tesseract(self) -> Optional[str]:
        """Find Tesseract path automatically"""
        system = platform.system()
        default_path = Config.TESSERACT_PATHS.get(system)
        
        if default_path and os.path.exists(default_path):
            return default_path
        
        # Try to find in PATH
        try:
            import shutil
            tesseract_cmd = shutil.which('tesseract')
            if tesseract_cmd:
                return tesseract_cmd
        except:
            pass
        
        return None
    
    def preprocess_image(self, image: Image.Image) -> Image.Image:
        """Preprocess image to improve detection accuracy"""
        try:
            image_array = np.array(image)
            if len(image_array.shape) == 2:
                gray_image = image_array
            else:
                image_bgr = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
                gray_image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
            
            _, threshold_image = cv2.threshold(
                gray_image, 
                Config.THRESHOLD_VALUE, 
                Config.THRESHOLD_MAX, 
                cv2.THRESH_BINARY_INV
            )
            return Image.fromarray(threshold_image)
        except Exception as e:
            raise Exception(f"Error in image preprocessing: {e}")
    
    def extract_text(self, image: Image.Image) -> str:
        """Extract text from image using OCR"""
        if not self.tesseract_path:
            raise Exception("Tesseract path not found. Please specify the path in settings.")
        
        try:
            processed_image = self.preprocess_image(image)
            text = pytesseract.image_to_string(
                processed_image, 
                config=f'--psm {Config.OCR_PSM}'
            )
            return text
        except Exception as e:
            raise Exception(f"Error in text recognition: {e}")

