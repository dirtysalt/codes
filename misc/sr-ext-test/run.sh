#!/bin/bash

source common.sh

ok=()
fail=()
for t in ./test-*.sh
do
    echo-green "===== running $t ====="
    ./$t
    if [ $? = 0 ]; then
        ok+=("$t")
    else
        fail+=("$t")
    fi
done

echo-green "===== summary ====="    
for item in "${ok[@]}"; do
    echo-green "[PASSED] $item"    
done
for item in "${fail[@]}"; do
    echo-red "[FAILED] $item"
done