#!/usr/bin/env bash
# Copyright (C) dirlt

for x in *Test
do
    echo "==================== $x ===================="
    sh ../../tools/JackCompiler.sh $x
done
