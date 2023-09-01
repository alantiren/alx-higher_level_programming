#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, displays the body of
the response, and handles HTTP status codes greater than or equal to 400 by
printing "Error code:" followed by the value of the HTTP status code.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    body = response.text
    # Display the response body
    print(response.text)
    
    # Check for HTTP status code >= 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(body)