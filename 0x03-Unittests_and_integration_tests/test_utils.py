#!/usr/bin/env python3
"""
This is our python module
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize
"""
These are testing modules
"""


class TestAccessNestedMap(unittest.TestCase):
    """
    This is our test class
    """
    @parameterized.expand([
        ({"nm": {"a": 1}, "p": ("a",)}, 1),
        ({"nm": {"a": {"b": 2}}, "p": ("a",)}, {"b": 2}),
        ({"nm": {"a": {"b": 2}}, "p": ("a", "b")}, 2)
        ])
    def test_access_nested_map(self, input, expected):
        """This function tests access_nested_map function"""
        self.assertEqual(access_nested_map(input["nm"], input["p"]), expected)

    @parameterized.expand([
        ({"nm": {}, "p": ("a",), "key": "\'a\'"}, 2),
        ({"nm": {"a": 1}, "p": ("a", "b"), "key": "\'b\'"}, 2)
        ])
    def test_access_nested_map_exception(self, input, expected):
        """This function tests access_ensted_map() if it raises exceptions"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(input["nm"], input["p"])
        self.assertEqual(str(e.exception), input["key"])


class TestGetJson(unittest.TestCase):
    """
    This class tests getjson function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """Tests utils.get_json function"""
        with patch("utils.requests.get") as g_mock:
            g_mock.return_value.json.return_value = test_payload
            result = get_json(test_url)
            g_mock.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    This class tests memoize decorator
    """
    def test_memoize(self):
        """
        test_memoize function
        """
        class TestClass:
            """
            Our test class
            """

            def a_method(self):
                """
                a_method of test class
                """
                return 42

            @memoize
            def a_property(self):
                """
                a_property of test class
                """
                return self.a_method()
        test = TestClass()
        with patch.object(test, "a_method", return_value=42) as g_mock:
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            g_mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
