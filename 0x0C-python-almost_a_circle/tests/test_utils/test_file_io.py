#!/usr/bin/python3

"""
Unit tests for the file_io module.
"""

import unittest
from file_io import read_file, write_file

class TestFileIO(unittest.TestCase):
    """
    Test cases for file_io module.
    """

    def test_read_file(self):
        """
        Test read_file function.
        """
        content = read_file('test.txt')
        self.assertEqual(content, 'This is a test file.')

    def test_write_file(self):
        """
        Test write_file function.
        """
        content = 'This is a test content.'
        write_file('test_output.txt', content)
        result = read_file('test_output.txt')
        self.assertEqual(result, content)

if __name__ == '__main__':
    unittest.main()
