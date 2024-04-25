#!/bin/bash
# send a get request to a give url with header variable 
curl -sH "X-School-User-Id: 98" "${1}"
