#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from typing import List
from parameterized import parameterized
from unittest.mock import patch, call
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    @parameterized.expand([
        ([1, 2, 3, 4], 4),
        ([1, 3, 4, 2], 4),
        ([1, 2, 2, 2], 2),
        ([10, -10, 5, 0], 10),
        ([10], 10),
        ([-1, -2, -3, -4], -1),
        ([0], 0),
        ([5, 5, 5, 5], 5),
        ([], None)
    ])
    def test_max_integer(self, lst: List[int], expected_result: int):
        """Test with different lists"""
        self.assertEqual(max_integer(lst), expected_result)

if __name__ == '__main__':
    unittest.main()
