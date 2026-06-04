#!/usr/bin/env bash
# Copyright (C) dirlt

for x in `find . | grep "\.jack$"`
do
    exp=${x/jack/xml}
    res=${x/jack/txt}
    echo "==================== $x ===================="
    diff $res $exp
done
