#!/usr/bin/env python3
"""_summary_:module for testing purpose
"""
from unittest.mock import Mock
import utils
import unittest
from parameterized import parameterized
from unittest.mock import patch


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
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test nested_map_exception"""
        with self.assertRaises(KeyError):
            raise KeyError


class TestGetJson(unittest.TestCase):
    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        # Test cases
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            # Setup the mock to return a Mock object with a json method that
            # returns test_payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            # Call the function with the test URL
            result = utils.get_json(test_url)
            # Assert that requests.get was called once with the test_url
            mock_get.assert_called_once_with(test_url)

            # Assert that the result is equal to the test_payload
            self.assertEqual(result, test_payload)

            # Reset the mock for the next iteration
            mock_get.reset_mock()


if __name__ == '__main__':
    unittest.main()
