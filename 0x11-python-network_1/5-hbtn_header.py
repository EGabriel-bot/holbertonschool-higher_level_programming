#!/usr/bin/python3
"""fetches url passed as an argument"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
