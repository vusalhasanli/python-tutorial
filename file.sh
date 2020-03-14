#!/bin/zsh

# delete file
rm -f file.txt

count=10
i=0
while true; do
  if [[ "$i" -gt $count ]]; then
       exit 1
  fi
  text="hello"
  # append
  echo $i $text >> file.txt
  ((i++))
done
