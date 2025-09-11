#!/bin/bash


# https://man7.org/linux/man-pages/man1/time.1.html
function better-time {
    /usr/bin/time -f "real=%es, kernel/user=%S/%Us, cpu=%P, maxrss=%MKB, pgflt=%F/%R, ctxsw=%c/%w, fsio=%I/%O, sockio=%r/%s" $@
}

opt=${1:-"pt"}
shift 1;

SODIR="/home/disk1/sr/"
SODIR="/home/disk4/zhangyan/installed/lib/"
TASKSET="taskset -c 0-63 "

if [ $opt = "pt" ] ; then
    
    PTMALLOC_CONF=""
    
    echo "=== ptmalloc: $PTMALLOC_CONF ==="
    MALLOC_CONF=$PTMALLOC_CONF \
    better-time $TASKSET ./malloc_perf.exe $@
    
fi

if [ $opt = "je" ] ; then
    
    #JEMALLOC_CONF="percpu_arena:percpu,oversize_threshold:0,muzzy_decay_ms:5000,dirty_decay_ms:5000,metadata_thp:auto,background_thread:true"
    JEMALLOC_CONF="percpu_arena:disabled,narenas:64,oversize_threshold:0,muzzy_decay_ms:5000,dirty_decay_ms:5000,metadata_thp:auto,background_thread:true"

    echo "=== jemalloc: $JEMALLOC_CONF ==="
    LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH LD_PRELOAD=$SODIR/libjemalloc.so \
    MALLOC_CONF=$JEMALLOC_CONF \
    better-time $TASKSET ./malloc_perf.exe $@
    
fi

if [ $opt == "tc" ]; then
    
    TCMALLOC_CONF=""
    
    echo "=== tcmalloc: $TCMALLOC_CONF ==="
    
    LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH LD_PRELOAD=$SODIR/libtcmalloc_minimal.so \
    MALLOC_CONF=$TCMALLOC_CONF \
    better-time $TASKSET ./malloc_perf.exe $@
fi

if [ $opt == "mi" ]; then
    
    MIMALLOC_CONF=""
    
    echo "=== mimalloc: $MIMALLOC_CONF ==="
    
    LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH LD_PRELOAD=$SODIR/libmimalloc.so \
    MALLOC_CONF=$MIMALLOC_CONF \
    better-time $TASKSET ./malloc_perf.exe $@
    
fi