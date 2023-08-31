#!/bin/bash
# Sends a request to a URL and displays only the status code of the response

URL="$1"
curl -s -o /dev/null -w "%{http_code}" "$URL"
