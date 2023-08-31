#!/bin/bash
# Sends a DELETE request to the URL and displays the body of the response

URL="$1"
curl -sX DELETE "$URL"
