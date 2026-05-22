#!/usr/bin/env bash
# Copyright (C) dirlt

for x in Average ComplexArrays ConvertToBin Pong Seven Square
do
    echo "==================== $x ===================="
    module=`basename $x`
    input_files=`ls $x/*.jack`
    echo "Compiling $x"
    ./compiler.py --file-ext .vm ${input_files}
done
