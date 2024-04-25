#!/bin/bash
# get the byte size of the HTTP  ressponse header 
curl -s "$1" | wc -c
