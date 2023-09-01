#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary containing the email parameter.
    data = {
        'email': email
    }

    # Encode the data dictionary as a URL-encoded string.
    data = urllib.parse.urlencode(data).encode('utf-8')

    # Create a POST request with the URL and encoded data.
    req = urllib.request.Request(url, data)

    # Send the POST request and read the response.
    with urllib.request.urlopen(req) as response:
        response_text = response.read().decode('utf-8')
        print(response_text)
