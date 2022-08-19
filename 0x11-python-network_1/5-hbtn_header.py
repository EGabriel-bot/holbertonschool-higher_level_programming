#!/usr/bin/python3
"""fetches url passed as an argument"""
import requests
import sys

r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
