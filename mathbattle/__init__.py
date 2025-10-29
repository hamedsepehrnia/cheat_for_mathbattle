"""
Math Battle Auto Checker
Automated mathematical equation detection and verification program
"""

__version__ = "1.0.0"
__author__ = "Math Battle Team"

from mathbattle.config import Config
from mathbattle.processor import ImageProcessor
from mathbattle.checker import EquationChecker
from mathbattle.clicker import AutoClicker
from mathbattle.gui import MathBattleApp

__all__ = [
    "Config",
    "ImageProcessor",
    "EquationChecker",
    "AutoClicker",
    "MathBattleApp",
]

