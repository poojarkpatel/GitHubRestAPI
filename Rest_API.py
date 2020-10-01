"""
Created on September 30 2020

@author: Pooja Patel
cwid: 10456923

This file is a test for the Rest_API file.

"""

import json
import requests


def repo_list(user_id):
    """ generator functions that returns repo name with number of commits in each repo """
    repo_url = requests.get("https://api.github.com/users/{}/repos".format(user_id))
    repo_list_name = repo_url.json()
    for value in repo_list_name:
        commit_count = 0
        repo_commits = requests.get("https://api.github.com/repos/{}/{}/commits".format(user_id, value["name"]))
        commits = repo_commits.json()
        for commit in commits:
            if commit in commits:
                commit_count += 1
        yield "Repo: {} and Number of commits: {}".format(value["name"], commit_count)


def get_user_id():
    """ get the git user ID"""
    user_id = input("Enter your user id: ")
    for item in repo_list(user_id):
        print(item)

get_user_id()