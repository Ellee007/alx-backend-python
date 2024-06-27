#!/usr/bin/env python3
"""
This is our module
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
GithubOrgClient = __import__("client").GithubOrgClient
"""
These are testing modules
"""


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class to test GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {"name": "google"}),
        ("abc", {"name": "abc"})
        ])
    @patch("client.get_json")
    def test_org(self, org_name, org_json, get_mock):
        """
        Testing org function
        """
        get_mock.return_value = org_json
        test = GithubOrgClient(org_name)
        self.assertEqual(test.org, org_json)
        get_mock.assert_called_once()

    @patch('client.GithubOrgClient.org', return_value={"repos_url": 'url'})
    def test_public_repos_url(self, mocked_org):
        """Test the _public_repos_url property of GithubOrgClient."""
        inst = GithubOrgClient('random org url')
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_property:
            mocked_property.return_value = mocked_org.return_value["repos_url"]
            repo_url = inst._public_repos_url
        self.assertEqual('url', repo_url)

    @patch("client.get_json", return_value=[{"name": "El"}])
    def test_public_repos(self, get_mock1):
        """Test public_repos"""
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as get_mock2:
            get_mock2.return_value = "url"
            test = GithubOrgClient("random url")
            self.assertEqual(test.public_repos(None), ["El"])
            get_mock1.assert_called_once_with("url")

    @parameterized.expand([
        ({"repo": {"license": {"key": "my_license"}},
            "license_key": "my_license"}, "True"),
        ({"repo": {"license": {"key": "other_license"}},
            "license_key": "my_license"}, "False")
        ])
    def test_has_license(self, input, expected):
        """Test has_license function"""
        test = GithubOrgClient("url")
        self.assertEqual(str(test.has_license(input["repo"],
                         input["license_key"])), expected)


if __name__ == "__main__":
    unittest.main()
