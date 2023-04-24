#!/usr/bin/python3
"""
fetches the content of the intranet status page
"""
import requests as req
url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    request = req.get(url)
    print("Body response:\n\t- type: {}\n\t- content: {}"
         .format(type(request.text), request.text))
