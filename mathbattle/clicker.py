"""
Mouse control and automatic clicking module
"""

import pyautogui
from typing import Tuple


class AutoClicker:
    """Mouse control and automatic clicking class"""
    
    @staticmethod
    def click_button(position: Tuple[int, int]) -> None:
        """Click at specified coordinates"""
        try:
            pyautogui.moveTo(position[0], position[1], duration=0.1)
            pyautogui.click()
        except Exception as e:
            raise Exception(f"Error clicking: {e}")

