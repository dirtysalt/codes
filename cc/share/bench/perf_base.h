/*
 * Copyright (C) dirlt
 */

#ifndef __BENCH_PERF_BASE_H__
#define __BENCH_PERF_BASE_H__

#include <pthread.h>
#include <stdint.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
#include "share/lock.h"
#include "share/cond.h"
#include "share/logging.h"
#include "share/atomic.h"
#include "share/util.h"
#include "share/fast_memcpy.h"

namespace bench {
namespace perf_base {

// ------------------------------------------------------------
template< typename Callable >
class PerfBase {
public:
    PerfBase(Callable* callable):
        callable_(callable),
        stop_(true),
        counter_(0),
        acc_ms_(0) {
    }
    void perf() {
        while(stop_) {
            nop();
        }
        while(!stop_) {
            if(callable_->call()) {
                atomic_add(&counter_, 1);
            }
        }
    }
    void start() {
        last_ms_ = gettime_ms();
        stop_ = false;
    }
    void stop() {
        stop_ = true;
        acc_ms_ += gettime_ms() - last_ms_;
    }
    void reset() {
        counter_ = 0;
        acc_ms_ = 0;
    }
    double timeMs() const {
        return acc_ms_;
    }
    uint32_t counter() const {
        return counter_;
    }
    void stat() const {
        printf("[%25s] time=%.3lfms counter=%u average=%.3lfms\n",
               callable_->tag(),
               acc_ms_,
               counter_,
               acc_ms_ / counter_);
    }
private:
    Callable* callable_;
    volatile bool stop_;
    volatile uint32_t counter_;
    double acc_ms_;
    double last_ms_;
}; // class PerfBase

// ------------------------------------------------------------
// clock_gettime
class ClockGetTime {
public:
    inline const char* tag() const {
        return "clock_gettime";
    }
    inline bool call() {
        struct timespec tp;
        clock_gettime(CLOCK_REALTIME, &tp);
        return true;
    }
}; // ClockGetTime

// ------------------------------------------------------------
// gettimeofday
class GetTimeOfDay {
public:
    inline const char* tag() const {
        return "gettimeofday";
    }
    inline bool call() {
        struct timeval tv;
        gettimeofday(&tv, NULL);
        return true;
    }
}; // class Gettimeofday

// ------------------------------------------------------------
// time
class Time {
public:
    inline const char* tag() const {
        return "time";
    }
    inline bool call() {
        time_t t = time(NULL);
        // t can't be 0.
        return t;
    }
}; // class Time

// ------------------------------------------------------------
// rdstc
#ifdef __x86_64__
class Rdtsc {
public:
    inline const char* tag() const {
        return "rdtsc";
    }
    inline bool call() {
        uint64_t tc = rdtsc();
        // tc can't be 0.
        return tc;
    }
}; // class Rdtsc
#endif

// ------------------------------------------------------------
// mutexlock
class MutexLock {
public:
    inline const char* tag() const {
        return "mutexlock";
    }
    inline bool call() {
        lock_.lock();
        lock_.unlock();
        return true;
    }
private:
    share::MutexLock lock_;
}; // class MutexLock

// ------------------------------------------------------------
// spinlock
class SpinLock {
public:
    inline const char* tag() const {
        return "spinlock";
    }
    inline bool call() {
        lock_.lock();
        lock_.unlock();
        return true;
    }
private:
    share::SpinLock lock_;
}; // class SpinLock

// ------------------------------------------------------------
// rwlock
class ReadLock {
public:
    ReadLock(share::RWLock* lock):
        lock_(lock) {}
    inline const char* tag() const {
        return "rwlock:read";
    }
    inline bool call() {
        lock_->lockForRead();
        lock_->unlock();
        return true;
    }
private:
    share::RWLock* lock_;
}; // class ReadLock

class WriteLock {
public:
    WriteLock(share::RWLock* lock):
        lock_(lock) {}
    inline const char* tag() const {
        return "rwlock:write";
    }
    inline bool call() {
        lock_->lockForWrite();
        lock_->unlock();
        return true;
    }
private:
    share::RWLock* lock_;
}; // class WriteLock

// ------------------------------------------------------------
// getpid
class GetPid {
public:
    inline const char* tag() const {
        return "getpid";
    }
    inline bool call() {
        pid_t pid = getpid();
        return pid;
    }
}; // class GetPid

// ------------------------------------------------------------
// getpid
class GetTid {
public:
    inline const char* tag() const {
        return "gettid";
    }
    inline bool call() {
        pid_t tid = get_tid();
        return tid;
    }
}; // class GetTid

// ------------------------------------------------------------
// pthread_cond
class ConditionWait {
public:
    ConditionWait(share::Condition* cond,
                  share::MutexLock* lock,
                  int wait_ms):
        cond_(cond),
        lock_(lock) {
        gettime_timespec(&p_);
        addtime_timespec(&p_, wait_ms);
    }
    inline const char* tag() const {
        return "pthread_cond_wait";
    }
    inline bool call() {
        share::LockGuard< share::MutexLock> lockguard(lock_);
        return cond_->timedWait(&p_);
    }
private:
    share::Condition* cond_;
    share::MutexLock* lock_;
    struct timespec p_;
}; // class ConditionWait

class ConditionSignal {
public:
    ConditionSignal(share::Condition* cond,
                    share::MutexLock* lock):
        cond_(cond), lock_(lock) {}
    inline const char* tag() const {
        return "pthread_cond_signal";
    }
    inline bool call() {
        lock_->lock();
        lock_->unlock();
        cond_->notify();
        return true;
    }
private:
    share::Condition* cond_;
    share::MutexLock* lock_;
}; // class ConditionSignal

// ------------------------------------------------------------
// pipe_pair_cond
class PipePairCondWait {
public:
    PipePairCondWait(share::PipePairCondition* cond,
                     int wait_ms):
        cond_(cond), wait_ms_(wait_ms) {}
    inline const char* tag() const {
        return "pipe_cond_wait";
    }
    inline bool call() {
        return cond_->wait(wait_ms_);
    }
private:
    share::PipePairCondition* cond_;
    int wait_ms_;
}; // class PipePairCondWait

class PipePairCondSignal {
public:
    PipePairCondSignal(share::PipePairCondition* cond):
        cond_(cond) {}
    inline const char* tag() const {
        return "pipe_cond_signal";
    }
    inline bool call() {
        return cond_->anotify();
    }
private:
    share::PipePairCondition* cond_;
}; // class PipePairCondSignal

// ------------------------------------------------------------
// socket_pair_cond
class SocketPairCondWait {
public:
    SocketPairCondWait(share::SocketPairCondition* cond,
                       int wait_ms):
        cond_(cond), wait_ms_(wait_ms) {}
    inline const char* tag() const {
        return "socket_cond_wait";
    }
    inline bool call() {
        return cond_->wait(wait_ms_);
    }
private:
    share::SocketPairCondition* cond_;
    int wait_ms_;
}; // class SocketPairCondWait

class SocketPairCondSignal {
public:
    SocketPairCondSignal(share::SocketPairCondition* cond):
        cond_(cond) {}
    inline const char* tag() const {
        return "socket_cond_signal";
    }
    inline bool call() {
        return cond_->anotify();
    }
private:
    share::SocketPairCondition* cond_;
}; // class SocketPairCondSignal

// ------------------------------------------------------------
// tcp_pair_cond
class TcpPairCondWait {
public:
    TcpPairCondWait(share::TcpPairCondition* cond,
                    int wait_ms):
        cond_(cond), wait_ms_(wait_ms) {}
    inline const char* tag() const {
        return "tcp_cond_wait";
    }
    inline bool call() {
        return cond_->wait(wait_ms_);
    }
private:
    share::TcpPairCondition* cond_;
    int wait_ms_;
}; // class TcpPairCondWait

class TcpPairCondSignal {
public:
    TcpPairCondSignal(share::TcpPairCondition* cond):
        cond_(cond) {}
    inline const char* tag() const {
        return "tcp_cond_signal";
    }
    inline bool call() {
        return cond_->anotify();
    }
private:
    share::TcpPairCondition* cond_;
}; // class TcpPairCondSignal

// ------------------------------------------------------------
// futex cond.
class FutexCondWait {
public:
    FutexCondWait(share::FutexCondition* cond,
                  int wait_ms):
        cond_(cond), wait_ms_(wait_ms) {}
    inline const char* tag() const {
        return "futex_cond_wait";
    }
    inline bool call() {
        return cond_->wait(wait_ms_);
    }
private:
    share::FutexCondition* cond_;
    int wait_ms_;
}; // class FutexCondWait

class FutexCondSignal {
public:
    FutexCondSignal(share::FutexCondition* cond):
        cond_(cond) {}
    inline const char* tag() const {
        return "futex_cond_signal";
    }
    inline bool call() {
        return cond_->anotify();
    }
private:
    share::FutexCondition* cond_;
}; // class FutexCondSignal

// ------------------------------------------------------------
// memcpy
class MemcpyCase {
public:
    MemcpyCase(int size): size_(size) {
        dst = new char [size];
        src = new char [size];
    }
    ~MemcpyCase() {
        delete [] dst;
        delete [] src;
    }
    inline const char* tag() const {
        tag_ = "memcpy[";
        string_append_number(&tag_, size_);
        tag_ += "]";
        return tag_.c_str();
    }
    inline bool call() {
        memcpy(dst, src, size_);
        return true;
    }
private:
    mutable std::string tag_;
    int size_;
    char* dst;
    char* src;
}; // MemcpyCase

// ------------------------------------------------------------
// fast_memcpy
class FastMemcpyCase {
public:
    FastMemcpyCase(int size): size_(size) {
        dst = new char [size];
        src = new char [size];
    }
    ~FastMemcpyCase() {
        delete [] dst;
        delete [] src;
    }
    inline const char* tag() const {
        tag_ = "fast_memcpy[";
        string_append_number(&tag_, size_);
        tag_ += "]";
        return tag_.c_str();
    }
    inline bool call() {
        share::fast_memcpy(dst, src, size_);
        return true;
    }
private:
    mutable std::string tag_;
    int size_;
    char* dst;
    char* src;
}; // FastMemcpyCase

} // namespace perf_base
} // namespace bench

#endif // __BENCH_PERF_BASE_H__
