/*
 * Copyright (C) dirlt
 */

#include <cassert>
#include "bench/perf_base.h"
#include "bench/define.h"

using namespace bench::perf_base;

// ------------------------------------------------------------
// clock_gettime
typedef PerfBase< ClockGetTime > PBClockGetTime;
static void* PBClockGetTime_callback(void* arg) {
    PBClockGetTime* p = static_cast<PBClockGetTime*>(arg);
    p->perf();
    return NULL;
}
void test_clockgettime() {
    static const int kThreadNumber = 1;
    pthread_t tid[kThreadNumber];
    static const int kDelayMillSeconds = 1000;
    ClockGetTime c;
    PBClockGetTime p(&c);
    TC(PBClockGetTime_callback, &p);
    p.start();
    sleep_ms(kDelayMillSeconds);
    p.stop();
    TW();
    p.stat();
}

// ------------------------------------------------------------
// gettimeofday
typedef PerfBase< GetTimeOfDay > PBGetTimeOfDay;
static void* PBGetTimeOfDay_callback(void* arg) {
    PBGetTimeOfDay* p = static_cast<PBGetTimeOfDay*>(arg);
    p->perf();
    return NULL;
}
void test_gettimeofday() {
    static const int kThreadNumber = 1;
    pthread_t tid[kThreadNumber];
    static const int kDelayMillSeconds = 1000;
    GetTimeOfDay c;
    PBGetTimeOfDay p(&c);
    TC(PBGetTimeOfDay_callback, &p);
    p.start();
    sleep_ms(kDelayMillSeconds);
    p.stop();
    TW();
    p.stat();
}

// ------------------------------------------------------------
// time
typedef PerfBase< Time > PBTime;
static void* PBTime_callback(void* arg) {
    PBTime* p = static_cast<PBTime*>(arg);
    p->perf();
    return NULL;
}
void test_time() {
    static const int kThreadNumber = 1;
    pthread_t tid[kThreadNumber];
    static const int kDelayMillSeconds = 1000;
    Time c;
    PBTime p(&c);
    TC(PBTime_callback, &p);
    p.start();
    sleep_ms(kDelayMillSeconds);
    p.stop();
    TW();
    p.stat();
}

// ------------------------------------------------------------
// rdtsc
#ifdef __x86_64__
typedef PerfBase< Rdtsc > PBRdtsc;
static void* PBRdtsc_callback(void* arg) {
    PBRdtsc* p = static_cast<PBRdtsc*>(arg);
    p->perf();
    return NULL;
}
void test_rdtsc() {
    static const int kThreadNumber = 1;
    pthread_t tid[kThreadNumber];
    static const int kDelayMillSeconds = 1000;
    Rdtsc c;
    PBRdtsc p(&c);
    TC(PBRdtsc_callback, &p);
    p.start();
    sleep_ms(kDelayMillSeconds);
    p.stop();
    TW();
    p.stat();
}
#endif

int main() {
    test_clockgettime();
    test_gettimeofday();
    test_time();
#ifdef __x86_64__
    test_rdtsc();
#endif
    return 0;
}
