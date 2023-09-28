#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -X GET -sI "$1" | grep Content-Length | awk '{split($0, lenght, ": "); print lenght[2]}'
