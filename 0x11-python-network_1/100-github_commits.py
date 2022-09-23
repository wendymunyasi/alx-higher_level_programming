#!/usr/bin/python3
"""
script that takes 2 arguments in order to list 10 commits (from the most
recent to oldest) of the repository "rails" by the user "rails".
Print all commits by: `<sha>: <author name>` (one by line)
"""
import sys
import requests


if __name__ == "__main__":
    try:
        repo_name = sys.argv[1]
        username = sys.argv[2]
        commmits_url = "https://api.github.com/repos/{}/{}/commits" \
            .format(username, repo_name)
        response = requests.get(commmits_url)
        json_obj = response.json()
        for i in range(0, 10):
            sha = json_obj[i].get("sha")
            commit = json_obj[i].get("commit").get("author").get("name")
            print("{}: {}".format(sha, commit))
    except ValueError as invalid_json:
        pass
