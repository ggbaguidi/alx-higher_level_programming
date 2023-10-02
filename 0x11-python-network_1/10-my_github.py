#!/usr/bin/python3
"""My github!"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    authr = HTTPBasicAuth(username, password)

    r = requests.get(url, auth=authr)
    if r.status_code >= 400:
        print('None')
    else:
        print(r.json().get('id'))
