#!/bin/bash

#sed "s/\([^\]\)\ /\1\\\ /g" .path | sed "s/\ /:/g"
sed "s/\n/:/g" .path

#while read line; do
    #line=$(echo "$line" | sed "s/[^\\]\ /\\\ /g")
    #new_path=$new_path:$line
#done < ~/.path
#echo $new_path
