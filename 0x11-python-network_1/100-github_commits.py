#!/usr/bin/python3
"""Time for an interview"""
import sys
import requests

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    response = requests.get(url)
    for commit in response.json()[:10]:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
