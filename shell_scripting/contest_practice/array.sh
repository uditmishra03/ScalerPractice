#!/bin/bash

arr=(1 2 3 4 5 56 67 9)
echo "Complete array without for loop:"
echo "${arr[@]}"

len="${#arr[@]}"
echo "size of array: $len"

for each in "${arr[@]}"; do
    echo "$each"
done
