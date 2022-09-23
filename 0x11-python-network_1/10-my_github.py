#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id.
The first argument will be your username.
The second argument will be your password (in your case, a personal
access token as password).
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    json_obj = response.json()
    print(json_obj.get("id"))
