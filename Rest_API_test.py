
"""
Created on September 30 2020
@author: Pooja Patel
cwid: 10456923
"""

import unittest
import json
import requests
from Rest_API import repo_list
from Rest_API import commits
from unittest import mock


class FakeResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data

switcher = {"https://api.github.com/users/richkempinski/repos": "Repository.json",
            "https://api.github.com/repos/richkempinski/csp/commits": "csp.json",
            "https://api.github.com/repos/richkempinski/hellogitworld/commits": "hellogitworld.json",
            "https://api.github.com/repos/richkempinski/helloworld/commits": "helloworld.json",
            "https://api.github.com/repos/richkempinski/Mocks/commits": "Mocks.json",
            "https://api.github.com/repos/richkempinski/Project1/commits": "Project1.json",
            "https://api.github.com/repos/richkempinski/richkempinski.github.io/commits":
                "richkempinski.github.io.json",
            "https://api.github.com/repos/richkempinski/try_nbdev/commits": "try_nbdev.json",
            "https://api.github.com/repos/richkempinski/try_nbdev2/commits": "try_nbdev2.json",
            "https://api.github.com/repos/richkempinski/threads-of-life/commits": "threads-of-life.json"}


def mocked_request_commit(*args):
    if args[0] in switcher:
        with open(switcher[args[0]]) as f:
            return FakeResponse(json.load(f))
    return FakeResponse(None)


def mocked_request_get(*args):
    if args[0] in switcher:
        with open(switcher[args[0]]) as f:
            return FakeResponse(json.load(f))
    return FakeResponse(None)


class TestRequestGitRepos(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_request_get)
    def test_repo(self, mock_get):
        expected = ['csp', 'hellogitworld', 'helloworld', 'Mocks', 'Project1',
                            'richkempinski.github.io', 'threads-of-life', 'try_nbdev', 'try_nbdev2']
        self.assertEqual(repo_list("richkempinski"), expected)

    @mock.patch('requests.get', side_effect=mocked_request_commit)
    def test_commits(self, mock_get):
        self.assertEqual(commits("richkempinski", "csp"), 2)
        self.assertEqual(commits("richkempinski", 'hellogitworld'), 30)
        self.assertEqual(commits("richkempinski", 'helloworld'), 6)
        self.assertEqual(commits("richkempinski", 'Mocks'), 10)
        self.assertEqual(commits("richkempinski", 'Project1'), 2)
        self.assertEqual(commits("richkempinski", 'richkempinski.github.io'), 9)
        self.assertEqual(commits("richkempinski", 'threads-of-life'), 1)
        self.assertEqual(commits("richkempinski", 'try_nbdev'), 2)
        self.assertEqual(commits("richkempinski", 'try_nbdev2'), 5)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
