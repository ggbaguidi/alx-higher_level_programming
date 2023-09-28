#!/bin/bash
# cURL a JSON file
curl -X POST "$1" -H 'Content-Type: application/json' -s -d "$(cat "$2")"
