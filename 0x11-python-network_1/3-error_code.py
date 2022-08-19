#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response"""
if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode("utf-8"))

    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
