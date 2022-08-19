#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request
    import sys

    with request.urlopen('{}'.format(sys.argv[1])) as response:
        header = response.info()

    print(header['X-Request-Id'])
