#!/bin/bash
# google search
text=""
first="true"

for i in "$@"; do
  if [ "$first" = "true" ]
  then
    text="$text$i"
    first="false"
  else
    text="$text+$i"
  fi
done

open -a 'Google Chrome' https://www.google.com/search?q=$text