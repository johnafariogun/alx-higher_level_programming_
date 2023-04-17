#!/usr/bin/env bash
# takes in a URL, sends a request to it and returns the response length
curl -s "$1" | wc -c
