#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    params = {
        "email": sys.argv[2],
    }

    query_string = urllib.parse.urlencode(params)
    data = query_string.decode("ascii")

    with urllib.request.urlopen(url, data) as response:
        response_text = response.read()
        print(response_text.decode('utf-8'))
