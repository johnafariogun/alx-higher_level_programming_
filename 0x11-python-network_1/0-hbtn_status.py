#!/usr/bin/python3
"""
fetches the content of the intranet status page
"""
import urllib.request as req
url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    request = req.Request(url)
    with req.urlopen(request) as response:
        body = response.read()
        print("Body response:\n\t- type: {}\n\t- content: {}"
              .format(type(body), body,))
        print("\t- utf8 content: {}".format(body.decode(
                      "utf-8")))
