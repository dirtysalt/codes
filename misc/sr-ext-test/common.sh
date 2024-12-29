#!/bin/bash

function echo-red {
    echo -e "\033[31m$1\033[0m"
}
function echo-green {
    echo -e "\033[32m$1\033[0m"
}

function gen-working-dir {    
    x="working/$1"
    mkdir -p $x
    echo $x
}

export FE_IP="127.0.0.1"
export FE_PORT="9030"
export FE_USER="root"
export FE_PASS=""

if [ -f env.sh ]; then
    source env.sh
fi

set -euo pipefail