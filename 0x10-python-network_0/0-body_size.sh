#!/bin/bash
# takes in a URL, sends a request to it and returns the response length
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
