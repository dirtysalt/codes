#!/usr/bin/env bash
# Copyright (C) dirlt

for x in Average ComplexArrays ConvertToBin Pong Seven Square
do
    echo "==================== $x ===================="
    module=`basename $x`
    input_files=`ls $x/*.jack`
    echo "Compiling $x"
    ./compiler.py --file-ext .txt ${input_files}
    sh ../../tools/JackCompiler.sh $x
    for f in $input_files
    do
        exp=${f/jack/vm}
        res=${f/jack/txt}
        echo "comparing $res $exp"
        diff $res $exp
    done
done
