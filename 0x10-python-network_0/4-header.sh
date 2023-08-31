#!/bin/bash
# Takes a URL, sends a GET request with a specific header
curl -s "$1" -H "X-School-User-Id: 98"
