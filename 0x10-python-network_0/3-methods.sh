#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | grep Allow | awk '{split($0, methods, ": "); print methods[2]}'
