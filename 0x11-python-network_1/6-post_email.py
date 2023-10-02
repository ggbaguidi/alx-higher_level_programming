#!/usr/bin/python3
"""POST an email #1"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    response = requests.post(url, data=payload)
    print(response.text)
