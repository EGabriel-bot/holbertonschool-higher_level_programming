#!/usr/bin/python3
"""POST request to url with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    info = {"q": letter}

    req = requests.post(url, data=info)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
