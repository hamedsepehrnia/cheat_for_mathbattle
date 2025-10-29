"""
Graphical user interface module
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import pyautogui
import platform
import time
import threading

from mathbattle.config import Config
from mathbattle.processor import ImageProcessor
from mathbattle.checker import EquationChecker
from mathbattle.clicker import AutoClicker


class MathBattleApp:
    """Main GUI application class"""
    
    def __init__(self, root: tk.Tk):
        """Initialize user interface"""
        self.root = root
        self.root.title("Math Battle Auto Checker")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Program variables
        self.is_running = False
        self.processor = None
        self.checker = EquationChecker()
        self.clicker = AutoClicker()
        
        # Coordinate settings
        self.top_left = Config.DEFAULT_TOP_LEFT
        self.bottom_right = Config.DEFAULT_BOTTOM_RIGHT
        self.correct_button = Config.DEFAULT_CORRECT_BUTTON
        self.wrong_button = Config.DEFAULT_WRONG_BUTTON
        
        # Create user interface
        self._create_widgets()
        self._setup_tesseract()
    
    def _create_widgets(self):
        """Create GUI widgets"""
        # Settings frame
        settings_frame = ttk.LabelFrame(self.root, text="Settings", padding=10)
        settings_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Tesseract path
        ttk.Label(settings_frame, text="Tesseract Path:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.tesseract_var = tk.StringVar()
        tesseract_entry = ttk.Entry(settings_frame, textvariable=self.tesseract_var, width=50)
        tesseract_entry.grid(row=0, column=1, columnspan=2, sticky=tk.EW, padx=5, pady=2)
        ttk.Button(settings_frame, text="Browse", command=self._browse_tesseract).grid(row=0, column=3, pady=2)
        
        # Equation region coordinates
        coords_frame = ttk.LabelFrame(settings_frame, text="Equation Region Coordinates", padding=5)
        coords_frame.grid(row=1, column=0, columnspan=4, sticky=tk.EW, pady=5)
        
        ttk.Label(coords_frame, text="Top-Left (X, Y):").grid(row=0, column=0, sticky=tk.W)
        self.top_left_x = tk.StringVar(value=str(self.top_left[0]))
        self.top_left_y = tk.StringVar(value=str(self.top_left[1]))
        ttk.Entry(coords_frame, textvariable=self.top_left_x, width=8).grid(row=0, column=1, padx=2)
        ttk.Entry(coords_frame, textvariable=self.top_left_y, width=8).grid(row=0, column=2, padx=2)
        
        ttk.Label(coords_frame, text="Bottom-Right (X, Y):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.bottom_right_x = tk.StringVar(value=str(self.bottom_right[0]))
        self.bottom_right_y = tk.StringVar(value=str(self.bottom_right[1]))
        ttk.Entry(coords_frame, textvariable=self.bottom_right_x, width=8).grid(row=1, column=1, padx=2)
        ttk.Entry(coords_frame, textvariable=self.bottom_right_y, width=8).grid(row=1, column=2, padx=2)
        
        # Button coordinates
        buttons_frame = ttk.LabelFrame(settings_frame, text="Button Coordinates", padding=5)
        buttons_frame.grid(row=2, column=0, columnspan=4, sticky=tk.EW, pady=5)
        
        ttk.Label(buttons_frame, text="Correct Button (X, Y):").grid(row=0, column=0, sticky=tk.W)
        self.correct_x = tk.StringVar(value=str(self.correct_button[0]))
        self.correct_y = tk.StringVar(value=str(self.correct_button[1]))
        ttk.Entry(buttons_frame, textvariable=self.correct_x, width=8).grid(row=0, column=1, padx=2)
        ttk.Entry(buttons_frame, textvariable=self.correct_y, width=8).grid(row=0, column=2, padx=2)
        
        ttk.Label(buttons_frame, text="Wrong Button (X, Y):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.wrong_x = tk.StringVar(value=str(self.wrong_button[0]))
        self.wrong_y = tk.StringVar(value=str(self.wrong_button[1]))
        ttk.Entry(buttons_frame, textvariable=self.wrong_x, width=8).grid(row=1, column=1, padx=2)
        ttk.Entry(buttons_frame, textvariable=self.wrong_y, width=8).grid(row=1, column=2, padx=2)
        
        # Control buttons
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.start_button = ttk.Button(control_frame, text="Start", command=self._start, width=15)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = ttk.Button(control_frame, text="Stop", command=self._stop, width=15, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(control_frame, text="Test Coordinates", command=self._test_coordinates, width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Test OCR", command=self._test_ocr, width=15).pack(side=tk.LEFT, padx=5)
        
        # Logs
        log_frame = ttk.LabelFrame(self.root, text="Operation Logs", padding=10)
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        settings_frame.columnconfigure(1, weight=1)
    
    def _setup_tesseract(self):
        """Configure Tesseract path"""
        processor = ImageProcessor()
        if processor.tesseract_path:
            self.tesseract_var.set(processor.tesseract_path)
            self.processor = processor
        else:
            self.tesseract_var.set(Config.TESSERACT_PATHS.get(platform.system(), ""))
            self._log("Warning: Tesseract path not found. Please specify the path.")
    
    def _browse_tesseract(self):
        """Select Tesseract file"""
        filename = filedialog.askopenfilename(
            title="Select Tesseract File",
            filetypes=[("Executable", "*.exe"), ("All files", "*.*")]
        )
        if filename:
            self.tesseract_var.set(filename)
            self.processor = ImageProcessor(filename)
            self._log(f"Tesseract path updated: {filename}")
    
    def _log(self, message: str):
        """Add message to log"""
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def _update_coordinates(self):
        """Update coordinates from input fields"""
        try:
            self.top_left = (
                int(self.top_left_x.get()),
                int(self.top_left_y.get())
            )
            self.bottom_right = (
                int(self.bottom_right_x.get()),
                int(self.bottom_right_y.get())
            )
            self.correct_button = (
                int(self.correct_x.get()),
                int(self.correct_y.get())
            )
            self.wrong_button = (
                int(self.wrong_x.get()),
                int(self.wrong_y.get())
            )
            return True
        except ValueError:
            messagebox.showerror("Error", "Coordinates must be integers.")
            return False
    
    def _test_coordinates(self):
        """Test coordinates by showing mouse position"""
        if not self._update_coordinates():
            return
        
        messagebox.showinfo(
            "Test Coordinates",
            f"Configured coordinates:\n"
            f"Equation region: {self.top_left} to {self.bottom_right}\n"
            f"Correct button: {self.correct_button}\n"
            f"Wrong button: {self.wrong_button}\n\n"
            f"The program will show coordinates in 3 seconds..."
        )
        
        def show_coordinates():
            time.sleep(Config.INITIAL_DELAY)
            pyautogui.moveTo(self.top_left[0], self.top_left[1], duration=0.5)
            time.sleep(0.5)
            pyautogui.moveTo(self.bottom_right[0], self.bottom_right[1], duration=0.5)
            time.sleep(0.5)
            pyautogui.moveTo(self.correct_button[0], self.correct_button[1], duration=0.5)
            time.sleep(0.5)
            pyautogui.moveTo(self.wrong_button[0], self.wrong_button[1], duration=0.5)
        
        threading.Thread(target=show_coordinates, daemon=True).start()
    
    def _test_ocr(self):
        """Test OCR on specified region"""
        if not self._update_coordinates():
            return
        
        if not self.processor:
            messagebox.showerror("Error", "Please specify Tesseract path first.")
            return
        
        try:
            region = (
                self.top_left[0],
                self.top_left[1],
                self.bottom_right[0] - self.top_left[0],
                self.bottom_right[1] - self.top_left[1]
            )
            
            screenshot = pyautogui.screenshot(region=region)
            text = self.processor.extract_text(screenshot)
            sanitized = self.checker.sanitize_equation(text)
            
            self._log(f"Detected text (raw): {text}")
            self._log(f"Sanitized text: {sanitized}")
            
            if sanitized:
                is_correct = self.checker.check_equation(sanitized)
                self._log(f"Check result: {'✓ Correct' if is_correct else '✗ Wrong'}")
            
            messagebox.showinfo("OCR Test", f"Detected text:\n{text}\n\nSanitized:\n{sanitized}")
        except Exception as e:
            self._log(f"OCR test error: {e}")
            messagebox.showerror("Error", f"OCR test error: {e}")
    
    def _start(self):
        """Start automatic operation"""
        if not self._update_coordinates():
            return
        
        if not self.processor:
            messagebox.showerror("Error", "Please specify Tesseract path first.")
            return
        
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        self._log("Program started...")
        threading.Thread(target=self._main_loop, daemon=True).start()
    
    def _stop(self):
        """Stop automatic operation"""
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self._log("Program stopped.")
    
    def _main_loop(self):
        """Main program loop"""
        region = (
            self.top_left[0],
            self.top_left[1],
            self.bottom_right[0] - self.top_left[0],
            self.bottom_right[1] - self.top_left[1]
        )
        
        time.sleep(Config.INITIAL_DELAY)
        
        while self.is_running:
            try:
                screenshot = pyautogui.screenshot(region=region)
                text = self.processor.extract_text(screenshot)
                sanitized = self.checker.sanitize_equation(text)
                
                self.root.after(0, self._log, f"Detected equation: {sanitized}")
                
                if sanitized:
                    is_correct = self.checker.check_equation(sanitized)
                    
                    if is_correct:
                        self.root.after(0, self._log, "Equation is correct. Clicking correct button...")
                        self.clicker.click_button(self.correct_button)
                    else:
                        self.root.after(0, self._log, "Equation is wrong. Clicking wrong button...")
                        self.clicker.click_button(self.wrong_button)
                else:
                    self.root.after(0, self._log, "Equation not detected.")
                
                time.sleep(Config.LOOP_DELAY)
                
            except Exception as e:
                self.root.after(0, self._log, f"Error: {e}")
                time.sleep(1)


def main():
    """Main program function"""
    root = tk.Tk()
    app = MathBattleApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

