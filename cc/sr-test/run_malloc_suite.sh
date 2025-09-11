#!/bin/bash

SUITES="4K,50000000 16K,10000000 256K,200000 1M,20000 4M,10000 16M,2000 32M,1000"
W=64

for x in $(echo $SUITES)
do
IFS=","; set -- $x;
echo "------ BLOCK $1 -----"
# ./run_malloc_perf.sh pt -B $1 -R $2 -W $W
./run_malloc_perf.sh je -B $1 -R $2 -W $W
./run_malloc_perf.sh tc -B $1 -R $2 -W $W
./run_malloc_perf.sh mi -B $1 -R $2 -W $W

# ./run_malloc_perf.sh je -B $1 -R $2 --nofree -W $W
echo -e "\n"
done
