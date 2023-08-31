#!/bin/bash
# Takes a URL, sends a GET request, and displays the body of the response

URL="$1"
curl -sL "$URL"
