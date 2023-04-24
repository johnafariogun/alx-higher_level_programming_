#!/usr/bin/python3
"""
displays the X-Request-Id header  variable of a reuest to a given URL
"""
from sys import argv
import urllib.request as req

if __name__ == "__main__":
    url = argv[1]

    request = req.Request(url)
    with req.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
