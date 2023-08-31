#!/bin/bash
# Takes a URL, sends a GET request with a specific header, and displays the body of the response

URL="$1"
curl -sH "X-School-User-Id: 98" "$URL"
