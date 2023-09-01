#!/usr/bin/python3
"""
Script that sends a request to a URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./1-hbtn_header.py <URL>")

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print(x_request_id)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
