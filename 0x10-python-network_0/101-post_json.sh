#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file as the request body
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
