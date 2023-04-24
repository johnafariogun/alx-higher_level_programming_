#!/usr/bin/python3
"""
displays the X-Request-Id header  variable of a reuest to a given URL
"""
from sys import argv
import requests as req

if __name__ == "__main__":
    url = argv[1]

    request = req.get(url)
    print(request.headers.get("X-Request-Id"))
