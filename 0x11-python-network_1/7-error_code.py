#!/usr/bin/python3
"""Error code #1"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    try:
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError:
        print(f"Error code: {response.status_code}")
