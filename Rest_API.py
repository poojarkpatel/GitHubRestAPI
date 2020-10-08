"""
@author: Pooja Patel
cwid: 10456923
This file is a test for the Rest_API file.

"""
import requests


def repo_list(user_id):
    """ generator functions that returns repo name with number of commits in each repo """
    repo_url = requests.get("https://api.github.com/users/{}/repos".format(user_id))
    list_repo = [item["name"] for item in repo_url.json()]
    return list_repo


def commits(user_id, repo):
    repo_commit = requests.get("https://api.github.com/repos/{}/{}/commits".format(user_id, repo))
    commit_count = 0
    for _ in repo_commit.json():
        commit_count += 1
    return commit_count



