#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
