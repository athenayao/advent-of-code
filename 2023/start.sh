#!/bin/bash
day="$1"

if [ -z "$day" ]; then
    echo "Missing day parameter"
    return
fi

mkdir "$day"
cd "$day"

cp ../template.py ./a.py
cp ../template.py ./b.py
touch input-example.txt input.txt
code a.py input-example.txt input.txt b.py

export day