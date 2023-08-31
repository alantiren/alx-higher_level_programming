#!/bin/bash
# Takes a URL, sends a POST request with specific parameters, and displays the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
