# test_nftsplice.py
"""
Tests for NftSplice module.
"""

import unittest
from nftsplice import NftSplice

class TestNftSplice(unittest.TestCase):
    """Test cases for NftSplice class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftSplice()
        self.assertIsInstance(instance, NftSplice)

    def test_run_method(self):
        """Test the run method."""
        instance = NftSplice()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
