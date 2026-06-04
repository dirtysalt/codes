/*
 * Copyright (C) dirlt
 */

#include <cassert>
#include "bench/perf_base.h"
#include "bench/define.h"

using namespace bench::perf_base;

// ------------------------------------------------------------
// mutexlock
typedef PerfBase< MutexLock > PBMutexLock;
static void* PBMutexLock_callback(void* arg) {
    PBMutexLock* p = static_cast<PBMutexLock*>(arg);
    p->perf();
    return NULL;
}
void test_mutexlock() {
    static const int kThreadNumber = 8;
    pthread_t tid[kThreadNumber];
    static const int kDelayMillSeconds = 1000;
    MutexLock c;
    PBMutexLock p(&c);
    TC(PBMutexLock_callback, &p);
    p.start();
    sleep_ms(kDelayMillSeconds);
    p.stop();
    TW();
    p.stat();
}

// ------------------------------------------------------------
// spinlock
typedef PerfBase< SpinLock > PBSpinLock;
static void* PBSpinLock_callback(void* arg) {
    PBSpinLock* p = static_cast<PBSpinLock*>(arg);
    p->perf();
    return NULL;
}
void test_spinlock() {
    static const int kThreadNumber = 8;
    pthread_t tid[kThreadNumber];
    static const int kDelayMillSeconds = 1000;
    SpinLock c;
    PBSpinLock p(&c);
    TC(PBSpinLock_callback, &p);
    p.start();
    sleep_ms(kDelayMillSeconds);
    p.stop();
    TW();
    p.stat();
}

// ------------------------------------------------------------
// rwlock
typedef PerfBase< ReadLock > PBReadLock;
static void* PBReadLock_callback(void* arg) {
    PBReadLock* p = static_cast<PBReadLock*>(arg);
    p->perf();
    return NULL;
}
typedef PerfBase< WriteLock > PBWriteLock;
static void* PBWriteLock_callback(void* arg) {
    PBWriteLock* p = static_cast<PBWriteLock*>(arg);
    p->perf();
    return NULL;
}
void test_rwlock() {
    static const int kReadThreadNumber = 8;
    static const int kWriteThreadNumber = 8;
    pthread_t rtid[kReadThreadNumber];
    pthread_t wtid[kWriteThreadNumber];
    static const int kDelayMillSeconds = 1000;
    share::RWLock lock;
    ReadLock rc(&lock);
    WriteLock wc(&lock);
    PBReadLock rp(&rc);
    PBWriteLock wp(&wc);
    RTC(PBReadLock_callback, &rp);
    WTC(PBWriteLock_callback, &wp);
    rp.start();
    wp.start();
    sleep_ms(kDelayMillSeconds);
    rp.stop();
    wp.stop();
    RTW();
    WTW();
    rp.stat();
    wp.stat();
}

int main() {
    test_mutexlock();
    test_spinlock();
    test_rwlock();
    return 0;
}
