/*
 * Copyright (C) dirlt
 */

#include <cassert>
#include "bench/perf_base.h"
#include "bench/define.h"

using namespace bench::perf_base;

// ------------------------------------------------------------
// memcpy
typedef PerfBase< MemcpyCase > PBMemcpyCase;
static void* PBMemcpyCase_callback(void* arg) {
    PBMemcpyCase* p = static_cast<PBMemcpyCase*>(arg);
    p->perf();
    return NULL;
}
void test_memcpy() {
    static const int kThreadNumber = 1;
    pthread_t tid[kThreadNumber];
    static const int kDelayMillSeconds = 1000;
    for(int size = 64;;) {
        MemcpyCase c(size);
        PBMemcpyCase p(&c);
        TC(PBMemcpyCase_callback, &p);
        p.start();
        sleep_ms(kDelayMillSeconds);
        p.stop();
        TW();
        p.stat();
        break;
    }
}


// ------------------------------------------------------------
// fast_memcpy
typedef PerfBase< FastMemcpyCase > PBFastMemcpyCase;
static void* PBFastMemcpyCase_callback(void* arg) {
    PBFastMemcpyCase* p = static_cast<PBFastMemcpyCase*>(arg);
    p->perf();
    return NULL;
}
void test_fast_memcpy() {
    static const int kThreadNumber = 1;
    pthread_t tid[kThreadNumber];
    static const int kDelayMillSeconds = 1000;
    for(int size = 64;;) {
        FastMemcpyCase c(size);
        PBFastMemcpyCase p(&c);
        TC(PBFastMemcpyCase_callback, &p);
        p.start();
        sleep_ms(kDelayMillSeconds);
        p.stop();
        TW();
        p.stat();
        break;
    }
}

int main() {
    test_memcpy();
    test_fast_memcpy();
    return 0;
}
