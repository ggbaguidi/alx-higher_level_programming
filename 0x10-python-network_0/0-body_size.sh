#!/bin/bash

curl -X GET -sI "$1" | grep Content-Length | awk '{split($0, lenght, ": "); print lenght[2]}'
