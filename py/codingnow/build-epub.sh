#!/usr/bin/env bash
# Copyright (C) dirlt

FROM=${1:-2014}
TO=${2:-2019}
FILES=""
for((year=$FROM;year<=$TO;year++))
do
    FILES="$FILES md/${year}-*.md"
done
FILES=`ls -r $FILES`

FMT="markdown+smart"
pandoc -f ${FMT} --toc --epub-embed-font='metadata/fonts/*.ttf' -o codingnow.epub metadata/title.txt ${FILES}
