#!/bin/bash
day="$1"

if [ -z "$day" ]; then
    echo "Missing day parameter"
    return
fi

mkdir "$day"
cd "$day"

cp ../template.py ./part_a.py
cp ../template.py ./part_b.py
touch input-example.txt input.txt
code part_a.py input-example.txt input.txt part_b.py

export day