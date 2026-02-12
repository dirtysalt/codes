#!/usr/bin/env bash
# Copyright (C) dirlt

find ProgramFlow | grep "\.vm$" | xargs ./vmasm.py

for x in FunctionCalls/*
do
    module=`basename $x`
    input_files=`ls $x/*.vm`
    ./vmasm.py --output $x/${module}.asm --compact-size ${input_files}
done
