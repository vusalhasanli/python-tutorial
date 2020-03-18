#!/bin/zsh

# delete file
rm -f file.txt
count=10
i=0
text="hello"
while true; do
  if [[ "$i" -gt $count ]]: then
       exit 1
  fi
  # append
  echo $i $text >> file.txt
  i++
done
