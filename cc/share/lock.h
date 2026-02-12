/*
 * Copyright (C) dirlt
 */

#ifndef __CC_SHARE_LOCK_H__
#define __CC_SHARE_LOCK_H__

#include <sys/types.h>
#include <pthread.h>
#include "share/util.h"

namespace share {

// ------------------------------------------------------------
// MutexLock Inteface.
class MutexLock {
public:
    MutexLock();
    ~MutexLock();
    void lock();
    void unlock();
    bool trylock();
    bool isLockedByThisThread() const {
        return holder_ == get_tid();
    }
    pthread_mutex_t* getPthreadMutex() {
        return &mutex_;
    }
private:
    pthread_mutex_t mutex_;
    pid_t holder_;
}; // MutexLock

// ------------------------------------------------------------
// RWLock Inteface.
class RWLock {
public:
    RWLock();
    ~RWLock();
    void lockForRead();
    void lockForWrite();
    void unlock();
private:
    pthread_rwlock_t lock_;
}; // class RWLock;

// ------------------------------------------------------------
// SpinLock Interface.
class SpinLock {
public:
    SpinLock();
    ~SpinLock();
    void lock();
    void unlock();
    bool trylock();
    bool isLockedByThisThread() const {
        return holder_ == get_tid();
    }
private:
    pthread_spinlock_t spinlock_;
    pid_t holder_;
}; // class SpinLock

// ------------------------------------------------------------
// LockGuard Interface.
template<typename T>
class LockGuard {
public:
    explicit LockGuard(T* lock):
        lock_(lock) {
        lock_->lock();
    }
    ~LockGuard() {
        lock_->unlock();
    }
private:
    T* lock_;
}; // class LockGuard

// ------------------------------------------------------------
// NopLock
class NopLock {
public:
    NopLock() {}
    ~NopLock() {}
    void lock() {}
    void unlock() {}
}; // class NopLock

} // namespace share

#endif // __CC_SHARE_LOCK_H__
