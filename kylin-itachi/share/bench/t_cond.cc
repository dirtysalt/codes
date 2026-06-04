/*
 * Copyright (C) dirlt
 */

#include "bench/perf_base.h"
#include "bench/define.h"

using namespace bench::perf_base;

// ------------------------------------------------------------
// pthread_cond
typedef PerfBase < ConditionWait > PBConditionWait;
static void* PBConditionWait_callback(void* arg) {
    PBConditionWait* p = static_cast<PBConditionWait*>(arg);
    p->perf();
    return NULL;
}
typedef PerfBase < ConditionSignal > PBConditionSignal;
static void* PBConditionSignal_callback(void* arg) {
    PBConditionSignal* p = static_cast<PBConditionSignal*>(arg);
    p->perf();
    return NULL;
}
void test_pthread_cond() {
    static const int kReadThreadNumber = 8;
    static const int kWriteThreadNumber = 8;
    pthread_t rtid[kReadThreadNumber];
    pthread_t wtid[kWriteThreadNumber];
    static const int kDelayMillSeconds = 2000;
    share::MutexLock lock;
    share::Condition cond(lock);
    ConditionWait wc(&cond, &lock, kDelayMillSeconds);
    ConditionSignal sc(&cond, &lock);
    PBConditionWait wp(&wc);
    PBConditionSignal sp(&sc);
    RTC(PBConditionWait_callback, &wp);
    WTC(PBConditionSignal_callback, &sp);
    wp.start();
    sp.start();
    sleep_ms(kDelayMillSeconds);
    wp.stop();
    sp.stop();
    RTW();
    WTW();
    wp.stat();
    sp.stat();
}

// ------------------------------------------------------------
// pipe_pair_cond
typedef PerfBase < PipePairCondWait > PBPipePairCondWait;
static void* PBPipePairCondWait_callback(void* arg) {
    PBPipePairCondWait* p = static_cast<PBPipePairCondWait*>(arg);
    p->perf();
    return NULL;
}
typedef PerfBase < PipePairCondSignal > PBPipePairCondSignal;
static void* PBPipePairCondSignal_callback(void* arg) {
    PBPipePairCondSignal* p = static_cast<PBPipePairCondSignal*>(arg);
    p->perf();
    return NULL;
}
void test_pipe_pair_cond() {
    static const int kReadThreadNumber = 8;
    static const int kWriteThreadNumber = 8;
    pthread_t rtid[kReadThreadNumber];
    pthread_t wtid[kWriteThreadNumber];
    static const int kDelayMillSeconds = 2000;
    share::PipePairCondition cond;
    PipePairCondWait wc(&cond, kDelayMillSeconds);
    PipePairCondSignal sc(&cond);
    PBPipePairCondWait wp(&wc);
    PBPipePairCondSignal sp(&sc);
    RTC(PBPipePairCondWait_callback, &wp);
    WTC(PBPipePairCondSignal_callback, &sp);
    wp.start();
    sp.start();
    sleep_ms(kDelayMillSeconds);
    wp.stop();
    sp.stop();
    RTW();
    WTW();
    wp.stat();
    sp.stat();
}

// ------------------------------------------------------------
// socket_pair_cond
typedef PerfBase < SocketPairCondWait > PBSocketPairCondWait;
static void* PBSocketPairCondWait_callback(void* arg) {
    PBSocketPairCondWait* p = static_cast<PBSocketPairCondWait*>(arg);
    p->perf();
    return NULL;
}
typedef PerfBase < SocketPairCondSignal > PBSocketPairCondSignal;
static void* PBSocketPairCondSignal_callback(void* arg) {
    PBSocketPairCondSignal* p = static_cast<PBSocketPairCondSignal*>(arg);
    p->perf();
    return NULL;
}
void test_socket_pair_cond() {
    static const int kReadThreadNumber = 8;
    static const int kWriteThreadNumber = 8;
    pthread_t rtid[kReadThreadNumber];
    pthread_t wtid[kWriteThreadNumber];
    static const int kDelayMillSeconds = 2000;
    share::SocketPairCondition cond;
    SocketPairCondWait wc(&cond, kDelayMillSeconds);
    SocketPairCondSignal sc(&cond);
    PBSocketPairCondWait wp(&wc);
    PBSocketPairCondSignal sp(&sc);
    RTC(PBSocketPairCondWait_callback, &wp);
    WTC(PBSocketPairCondSignal_callback, &sp);
    wp.start();
    sp.start();
    sleep_ms(kDelayMillSeconds);
    wp.stop();
    sp.stop();
    RTW();
    WTW();
    wp.stat();
    sp.stat();
}

// ------------------------------------------------------------
// tcp_pair_cond
typedef PerfBase < TcpPairCondWait > PBTcpPairCondWait;
static void* PBTcpPairCondWait_callback(void* arg) {
    PBTcpPairCondWait* p = static_cast<PBTcpPairCondWait*>(arg);
    p->perf();
    return NULL;
}
typedef PerfBase < TcpPairCondSignal > PBTcpPairCondSignal;
static void* PBTcpPairCondSignal_callback(void* arg) {
    PBTcpPairCondSignal* p = static_cast<PBTcpPairCondSignal*>(arg);
    p->perf();
    return NULL;
}
void test_tcp_pair_cond() {
    static const int kReadThreadNumber = 8;
    static const int kWriteThreadNumber = 8;
    pthread_t rtid[kReadThreadNumber];
    pthread_t wtid[kWriteThreadNumber];
    static const int kDelayMillSeconds = 2000;
    share::TcpPairCondition cond;
    TcpPairCondWait wc(&cond, kDelayMillSeconds);
    TcpPairCondSignal sc(&cond);
    PBTcpPairCondWait wp(&wc);
    PBTcpPairCondSignal sp(&sc);
    RTC(PBTcpPairCondWait_callback, &wp);
    WTC(PBTcpPairCondSignal_callback, &sp);
    wp.start();
    sp.start();
    sleep_ms(kDelayMillSeconds);
    wp.stop();
    sp.stop();
    RTW();
    WTW();
    wp.stat();
    sp.stat();
}

// ------------------------------------------------------------
// futex cond
typedef PerfBase < FutexCondWait > PBFutexCondWait;
static void* PBFutexCondWait_callback(void* arg) {
    PBFutexCondWait* p = static_cast<PBFutexCondWait*>(arg);
    p->perf();
    return NULL;
}
typedef PerfBase < FutexCondSignal > PBFutexCondSignal;
static void* PBFutexCondSignal_callback(void* arg) {
    PBFutexCondSignal* p = static_cast<PBFutexCondSignal*>(arg);
    p->perf();
    return NULL;
}
void test_futex_cond() {
    static const int kReadThreadNumber = 8;
    static const int kWriteThreadNumber = 8;
    pthread_t rtid[kReadThreadNumber];
    pthread_t wtid[kWriteThreadNumber];
    static const int kDelayMillSeconds = 2000;
    share::FutexCondition cond;
    FutexCondWait wc(&cond, kDelayMillSeconds);
    FutexCondSignal sc(&cond);
    PBFutexCondWait wp(&wc);
    PBFutexCondSignal sp(&sc);
    RTC(PBFutexCondWait_callback, &wp);
    WTC(PBFutexCondSignal_callback, &sp);
    wp.start();
    sp.start();
    sleep_ms(kDelayMillSeconds);
    wp.stop();
    sp.stop();
    RTW();
    WTW();
    wp.stat();
    sp.stat();
}

int main() {
    test_pthread_cond();
    test_pipe_pair_cond();
    test_socket_pair_cond();
    test_tcp_pair_cond();
    test_futex_cond();
    return 0;
}
