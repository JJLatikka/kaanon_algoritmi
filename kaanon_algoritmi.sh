#!/bin/bash

k="kaanon_algoritmi"
lisattavat_paketit=("$k/domain" "$k/in_out" "$k/logic")
kooste="$PWD:"

for p in "${lisattavat_paketit[@]}";
  do kooste+="$PWD$p:"
done

export PYTHONPATH=$kooste
version_ly=$(lilypond -v 2>&1)
python3 -m kaanon_algoritmi $version_ly
status=$?

if [ $status -eq 0 ]; then
  kaanon=$(cat output/ly/kaanon_temp.txt 2>&1)
  lilypond -o output/pdf output/ly/"$kaanon.ly"
  atril output/pdf/"$kaanon.pdf"
  rm output/ly/kaanon_temp.txt
fi

