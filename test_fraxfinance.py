# test_fraxfinance.py
"""
Tests for FraxFinance module.
"""

import unittest
from fraxfinance import FraxFinance

class TestFraxFinance(unittest.TestCase):
    """Test cases for FraxFinance class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FraxFinance()
        self.assertIsInstance(instance, FraxFinance)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FraxFinance()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
