#!/usr/bin/python3
"""
Error code management
"""
import sys
import urllib.request
import urllib

if __name__ == '__main__':
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
