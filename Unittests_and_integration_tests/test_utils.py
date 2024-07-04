#!/usr/bin/env python3
"""_summary_:module for testing purpose
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """Testing class for testing utils functions
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected) -> str:
        """test for nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test nested_map_exception"""
        with self.assertRaises(KeyError):
            raise KeyError


if __name__ == '__main__':
    unittest.main()
