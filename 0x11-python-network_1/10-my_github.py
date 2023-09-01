#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and personal access token)
and uses the GitHub API to display your user ID.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    json_obj = response.json()
    print(json_obj.get("id"))
