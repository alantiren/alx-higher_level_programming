#!/bin/bash
# Takes a URL, sends a request, and displays the size of the response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
