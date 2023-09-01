#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and personal access token)
and uses the GitHub API to display your user ID.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    
    # Set up the API endpoint and headers
    url = 'https://api.github.com/user'
    headers = {
        'Authorization': 'Basic ' + f'{username}:{password}'.encode('utf-8').hex(),
    }
    
    # Send a GET request to the GitHub API
    response = requests.get(url, headers=headers)
    
    # Check the response status code
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        print(None)
