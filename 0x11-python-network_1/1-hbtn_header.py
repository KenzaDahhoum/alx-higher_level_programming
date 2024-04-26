#!/usr/bin/python3
"""
fetch argv1 
display a value from the header
"""
import urllib.request
import sys

url = sys.argv[1] 
with urllib.request.urlopen(url) as response:
	x = response.getheader('X-Request-Id')
	print(x)
        
