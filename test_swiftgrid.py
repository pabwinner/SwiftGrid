# test_swiftgrid.py
"""
Tests for SwiftGrid module.
"""

import unittest
from swiftgrid import SwiftGrid

class TestSwiftGrid(unittest.TestCase):
    """Test cases for SwiftGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SwiftGrid()
        self.assertIsInstance(instance, SwiftGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SwiftGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
