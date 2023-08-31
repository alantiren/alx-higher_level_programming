#!/bin/bash
# Takes a URL and displays all HTTP methods the server will accept

URL="$1"
curl -sI "$URL" | grep "Allow" | cut -d ' ' -f 2-
