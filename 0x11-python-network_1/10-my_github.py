#!/usr/bin/python3
"""uses the GitHub API to display your id"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"
    username = sys.argv[1]
    passwd = sys.argv[2]

    req = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(req.json().get("id"))
