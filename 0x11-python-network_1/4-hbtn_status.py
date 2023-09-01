#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
using the requests package and displays the body of the response.
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    
    response = requests.get(url)
    
    print("Body response:")
    print("    - type: {}".format(type(response.text)))
    print("    - content: {}".format(response.text))
