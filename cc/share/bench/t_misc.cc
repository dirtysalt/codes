/*
 * Copyright (C) dirlt
 */

#include <cassert>
#include "bench/perf_base.h"
#include "bench/define.h"

using namespace bench::perf_base;

// ------------------------------------------------------------
// getpid
typedef PerfBase< GetPid > PBGetPid;
static void* PBGetPid_callback(void* arg) {
    PBGetPid* p = static_cast<PBGetPid*>(arg);
    p->perf();
    return NULL;
}
void test_getpid() {
    static const int kThreadNumber = 1;
    pthread_t tid[kThreadNumber];
    static const int kDelayMillSeconds = 1000;
    GetPid c;
    PBGetPid p(&c);
    TC(PBGetPid_callback, &p);
    p.start();
    sleep_ms(kDelayMillSeconds);
    p.stop();
    TW();
    p.stat();
}

// ------------------------------------------------------------
// gettid
typedef PerfBase< GetTid > PBGetTid;
static void* PBGetTid_callback(void* arg) {
    PBGetTid* p = static_cast<PBGetTid*>(arg);
    p->perf();
    return NULL;
}
void test_gettid() {
    static const int kThreadNumber = 1;
    pthread_t tid[kThreadNumber];
    static const int kDelayMillSeconds = 1000;
    GetTid c;
    PBGetTid p(&c);
    TC(PBGetTid_callback, &p);
    p.start();
    sleep_ms(kDelayMillSeconds);
    p.stop();
    TW();
    p.stat();
}

int main() {
    test_getpid();
    test_gettid();
    return 0;
}
