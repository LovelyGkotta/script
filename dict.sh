#!/bin/bash
# cambridge dict
text=""
first="true"

for i in "$@"; do
  if [ "$first" = "true" ];
  then
    text="$text$i"
    first="false"
  else
    text="$text+$i"
  fi
done

open -a 'Google Chrome' https://dictionary.cambridge.org/zhs/%E8%AF%8D%E5%85%B8/%E8%8B%B1%E8%AF%AD-%E6%B1%89%E8%AF%AD-%E7%AE%80%E4%BD%93/$text
