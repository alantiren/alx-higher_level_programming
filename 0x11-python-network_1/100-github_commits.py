#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest) of a repository
by a user on GitHub using the GitHub API.
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    try:
        response = requests.get(url)
        commits_data = response.json()
        if response.status_code == 200:
            for commit in commits_data[:10]:
                sha = commit.get('sha')
                author_name = commit.get('commit').get('author').get('name')
                print(f'{sha}: {author_name}')
        else:
            print("Error: Unable to retrieve commits")
    except Exception as e:
        print("Error:", e)
