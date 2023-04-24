#!/usr/bin/python3
"""
displays the X-Request-Id header  variable of a reuest to a given URL
"""
from sys import argv
import urllib.request as req
import urllib.parse as parser

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = parser.urlencode(value).encode("ascii")

    request = req.Request(url, data)
    with req.urlopen(request) as response:
        print(response.read().decode("utf-8"))
