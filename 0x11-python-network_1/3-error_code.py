#!/usr/bin/python3
"""
sends a request to a url and displays the reponse and associated error codes
"""

from sys import argv
import urllib.error as error
import urllib.request as req

if __name__ == "__main__":
    url = argv[1]

    request = req.Request(url)
    try:
        with req.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
