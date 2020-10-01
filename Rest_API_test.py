"""
Created on September 30 2020

@author: Pooja Patel
cwid: 10456923

This file is a test for the Rest_API file.

"""
import unittest
from Rest_API import repo_list


class TestRepo(unittest.TestCase):
    """Test for the repo_list function"""
    def test_repo_list(self):
        repo = [value for value in repo_list("richkempinski")]
        result = ['Repo: csp and Number of commits: 2',
                  'Repo: hellogitworld and Number of commits: 30',
                  'Repo: helloworld and Number of commits: 6',
                  'Repo: Mocks and Number of commits: 10',
                  'Repo: Project1 and Number of commits: 2',
                  'Repo: richkempinski.github.io and Number of commits: 9',
                  'Repo: try_nbdev and Number of commits: 2',
                  'Repo: try_nbdev2 and Number of commits: 5']
        self.assertEqual(repo, result)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
