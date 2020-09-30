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
        repo = [value for value in repo_list("poojarkpatel")]
        result = ['Repo: Banking-System  and Number of commits: 13',
                  'Repo: GitHubRestAPI  and Number of commits: 1',
                  'Repo: helloworld  and Number of commits: 6',
                  'Repo: Sentiment_Analyzer  and Number of commits: 2',
                  'Repo: Smart_IDcard  and Number of commits: 2',
                  'Repo: Smart_Id_Card  and Number of commits: 2',
                  'Repo: SSW555_GEDCOM_Analyzer  and Number of commits: 4',
                  'Repo: Student_Repository  and Number of commits: 30',
                  'Repo: Testing_Triangle_Classification  and Number of commits: 2',
                  "Repo: Triangle567  and Number of commits: 8"
                  ]
        self.assertEqual(repo, result)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)