#!/usr/bin/python3
"""Response header value #1"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    header = requests.get(url).headers
    print(header.get("X-Request-Id"))
