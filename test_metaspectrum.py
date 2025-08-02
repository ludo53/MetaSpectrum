# test_metaspectrum.py
"""
Tests for MetaSpectrum module.
"""

import unittest
from metaspectrum import MetaSpectrum

class TestMetaSpectrum(unittest.TestCase):
    """Test cases for MetaSpectrum class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaSpectrum()
        self.assertIsInstance(instance, MetaSpectrum)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaSpectrum()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
