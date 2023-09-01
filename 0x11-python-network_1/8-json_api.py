#!/usr/bin/python3
"""
Script that takes in a letter, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter,
and displays the response.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    data = {'q': q}
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data=data)
        user_data = response.json()
        if user_data:
            print("[{}] {}".format(user_data.get('id'), user_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
