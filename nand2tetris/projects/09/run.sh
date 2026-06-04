#!/usr/bin/env bash
# Copyright (C) dirlt

osdir="MyOS"
sh ../../tools/JackCompiler.sh MyOS

osdir="MyOS"

for x in Average Fraction HelloWorld List Square Pong
do
    sh ../../tools/JackCompiler.sh $x
    module=`basename $x`
    input_files=`ls $x/*.vm`
    os_files=`ls $osdir/*.vm`
    ./vmasm.py --output $x/${module}.asm --init-code --remove-unused-fn --compact-size ${input_files} ${os_files}
done

find . | grep "\.asm$" | xargs ./asm.py
