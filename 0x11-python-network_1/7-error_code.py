#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
if __name__ == "__main__":
    import requests
    import sys

    bad_r = requests.get(sys.argv[1])
    if bad_r.status_code >= 400:
        print('Error code: {}'.format(bad_r.status_code))
    else:
        print(bad_r.text)
