#!/usr/bin/python3
if __name__ == "__main__":
    from urllib import request
    import sys

    with request.urlopen(f'{sys.argv[1]}') as response:
        header = response.info()

    print(header['X-Request-Id'])
