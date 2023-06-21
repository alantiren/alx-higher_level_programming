#!/usr/bin/python3

"""
Unit tests for the json_operations module.
"""

import unittest
from json_operations import load_json, save_json

class TestJsonOperations(unittest.TestCase):
    """
    Test cases for json_operations module.
    """

    def test_load_json(self):
        """
        Test load_json function.
        """
        data = load_json('test.json')
        self.assertEqual(data['name'], 'John Doe')

    def test_save_json(self):
        """
        Test save_json function.
        """
        data = {'name': 'Jane Smith'}
        save_json('test_output.json', data)
        loaded_data = load_json('test_output.json')
        self.assertEqual(loaded_data['name'], 'Jane Smith')

if __name__ == '__main__':
    unittest.main()
