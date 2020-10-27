#!/usr/bin/env bash
# Copyright (C) dirlt

T=$1
OUT="output$T"

rm -rf $OUT
mkdir -p $OUT

for ((i=0;i<50;i++))
do
    go test -run $T | tee $OUT/run$i.txt
done

grep "^FAIL" $OUT/*
