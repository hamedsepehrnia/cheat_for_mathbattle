"""
Mathematical equation checking module
"""

import re


class EquationChecker:
    """Mathematical equation checking class"""
    
    @staticmethod
    def sanitize_equation(equation: str) -> str:
        """Sanitize and fix equation"""
        if not equation:
            return ""
        
        equation = equation.replace(' ', '')
        equation = equation.replace('-0', '-').replace('0-', '0')
        equation = equation.replace('(', '1').replace(')', '1')
        equation = equation.replace('[', '1').replace(']', '1')
        equation = equation.replace('{', '1').replace('}', '1')
        equation = equation.replace('\u00d7', '*').replace('x', '*')
        equation = equation.replace('+=', '=').replace('-=', '=')
        
        # Remove invalid characters
        allowed_chars = re.compile(r'[0-9+\-*/=]')
        sanitized = ''.join(filter(allowed_chars.match, equation))
        return sanitized.strip()
    
    @staticmethod
    def check_equation(equation: str) -> bool:
        """Check if equation is correct"""
        try:
            if "=" not in equation:
                return False
            
            left, right = equation.split("=", 1)
            left = left.strip()
            right = right.strip()
            
            if not left or not right:
                return False
            
            # Calculate each side
            left_value = eval(left)
            right_value = eval(right)
            
            return abs(left_value - right_value) < 0.0001  # For floating point comparison
        except Exception:
            return False

