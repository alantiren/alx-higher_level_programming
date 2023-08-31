#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file as the request body
# Displays the body of the response

URL="$1"
JSON_FILE="$2"

curl -sX POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$URL"
