#!/bin/bash
# script that takes url and displays the body of response
body=$( curl -sI "$1" | grep -i 'HTTP/1.1' |cut -d " " -f2 ); if [ "$body" -eq "200" ]; then curl -sI "$1"; fi
