#!/usr/bin/python3
"""
displays the X-Request-Id header  variable of a reuest to a given URL
"""
from sys import argv
import requests as req

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}

    request = req.post(url, data=value)
    print(request.text)
