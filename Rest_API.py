import json
import requests


def repo_list(user_id):
    repo_url = requests.get("https://api.github.com/users/{}/repos".format(user_id))
    repo_list_name = repo_url.json()
    for value in repo_list_name:
        commit_count = 0
        repo_commits = requests.get("https://api.github.com/repos/{}/{}/commits".format(user_id, value["name"]))
        for commit in repo_commits.json():
            if commit in repo_commits.json():
                commit_count += 1
        yield "Repo: {}  and Number of commits: {} ".format(value["name"], commit_count)


def get_user_id():
    user_id = input("Enter your user id: ")
    for item in repo_list(user_id):
        print(item)


if __name__ == '__main__':
    get_user_id()