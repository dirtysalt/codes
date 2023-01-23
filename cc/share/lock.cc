/*
 * Copyright (C) dirlt
 */

#include <cassert>
#include "share/logging.h"
#include "share/lock.h"

namespace share {

// ------------------------------------------------------------
// MutexLock Implementation
MutexLock::MutexLock(): holder_(0) {
    int ret = pthread_mutex_init(&mutex_, NULL);
    if(ret < 0) {
        FATAL("pthread_mutex_init(%p) failed(%s)", &mutex_, SERRNO2(ret));
    }
}

MutexLock::~MutexLock() {
    assert(holder_ == 0);
    int ret = pthread_mutex_destroy(&mutex_);
    if(ret < 0) {
        FATAL("pthread_mutex_destroy(%p) failed(%s)", &mutex_, SERRNO2(ret));
    }
}

void MutexLock::lock() {
    int ret = pthread_mutex_lock(&mutex_);
    if(ret < 0) {
        FATAL("pthread_mutex_lock(%p) failed(%s)", &mutex_, SERRNO2(ret));
    }
    holder_ = get_tid();
}

void MutexLock::unlock() {
    int ret = pthread_mutex_unlock(&mutex_);
    if(ret < 0) {
        FATAL("pthread_mutex_unlock(%p) failed(%s)", &mutex_, SERRNO2(ret));
    }
    holder_ = 0;
}

bool MutexLock::trylock() {
    int ret = pthread_mutex_trylock(&mutex_);
    if(ret < 0 && ret != EBUSY) {
        FATAL("pthread_mutex_trylock(%p) failed(%s)", &mutex_, SERRNO2(ret));
    }
    if(ret == EBUSY) {
        return false;
    }
    return true;
}

// ------------------------------------------------------------
// RWLock Implementation
RWLock::RWLock() {
    int ret = pthread_rwlock_init(&lock_, NULL);
    if(ret < 0) {
        FATAL("pthread_rwlock_init(%p) failed(%s)", &lock_, SERRNO2(ret));
    }
}

RWLock::~RWLock() {
    int ret = pthread_rwlock_destroy(&lock_);
    if(ret < 0) {
        WARNING("pthread_rwlock_destroy(%p) failed(%s)", &lock_, SERRNO2(ret));
    }
}

void RWLock::lockForRead() {
    int ret = pthread_rwlock_rdlock(&lock_);
    if(ret < 0) {
        FATAL("pthread_rwlock_rdlock(%p) failed(%s)", &lock_, SERRNO2(ret));
    }
}

void RWLock::lockForWrite() {
    int ret = pthread_rwlock_wrlock(&lock_);
    if(ret < 0) {
        FATAL("pthread_rwlock_wrlock(%p) failed(%s)", &lock_, SERRNO2(ret));
    }
}

void RWLock::unlock() {
    int ret = pthread_rwlock_unlock(&lock_);
    if(ret < 0) {
        FATAL("pthread_rwlock_unlock(%p) failed(%s)", &lock_, SERRNO2(ret));
    }
}

// ------------------------------------------------------------
// SpinLock Implementation
SpinLock::SpinLock(): holder_(0) {
    int ret = pthread_spin_init(&spinlock_, PTHREAD_PROCESS_PRIVATE);
    if(ret < 0) {
        FATAL("pthread_spin_init(%p,PTHREAD_PROCESS_PRIVATE) failed(%s)", &spinlock_, SERRNO2(ret));
    }
}

SpinLock::~SpinLock() {
    assert(holder_ == 0);
    int ret = pthread_spin_destroy(&spinlock_);
    if(ret < 0) {
        FATAL("pthread_pin_destroy(%p) failed(%s)", &spinlock_, SERRNO2(ret));
    }
}

void SpinLock::lock() {
    int ret = pthread_spin_lock(&spinlock_);
    if(ret < 0) {
        FATAL("pthread_spin_lock(%p) failed(%s)", &spinlock_, SERRNO2(ret));
    }
    holder_ = get_tid();
}

void SpinLock::unlock() {
    int ret = pthread_spin_unlock(&spinlock_);
    if(ret < 0) {
        FATAL("pthread_spin_unlock(%p) failed(%s)", &spinlock_, SERRNO2(ret));
    }
    holder_ = 0;
}

bool SpinLock::trylock() {
    int ret = pthread_spin_trylock(&spinlock_);
    if(ret < 0 && ret != EBUSY) {
        FATAL("pthrad_spin_trylock(%p) failed(%s)", &spinlock_, SERRNO2(ret));
    }
    if(ret == EBUSY) {
        return false;
    }
    return true;
}

} // namespace share
