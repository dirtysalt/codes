/*
 * Copyright (C) dirlt
 */

#include <pthread.h>
#include <sys/time.h>
#include <linux/futex.h>
#include "share/lock.h"
#include "share/cond.h"
#include "share/logging.h"

namespace share {

// ------------------------------------------------------------
// Condition Implementation
Condition::Condition(MutexLock& mutex): mutex_(mutex) {
    int ret = pthread_cond_init(&cond_, NULL);
    if(ret < 0) {
        FATAL("pthread_cond_init(%p) failed(%s)", &cond_, SERRNO2(ret));
    }
}

Condition::~Condition() {
    int ret = pthread_cond_destroy(&cond_);
    if(ret < 0) {
        FATAL("pthread_cond_destroy(%p) failed(%s)", &cond_, SERRNO2(ret));
    }
}

void Condition::wait() {
    int ret = pthread_cond_wait(&cond_, mutex_.getPthreadMutex());
    if(ret < 0) {
        FATAL("pthread_cond_wait(%p) failed(%s)", &cond_, SERRNO2(ret));
    }
}

bool Condition::timedWait(struct timespec* tp) {
    int ret = pthread_cond_timedwait(&cond_, mutex_.getPthreadMutex(), tp);
    if(ret < 0 && ret != ETIMEDOUT) {
        FATAL("pthread_cond_timedwait(%p,%p) failed(%s)", &cond_, tp, SERRNO2(ret));
    }
    if(ret == ETIMEDOUT) {
        return false;
    }
    return true;
}

void Condition::notify() {
    int ret = pthread_cond_signal(&cond_);
    if(ret < 0) {
        FATAL("pthread_cond_signal(%p) failed(%s)", &cond_, SERRNO2(ret));
    }
}

void Condition::notifyAll() {
    int ret = pthread_cond_broadcast(&cond_);
    if(ret < 0) {
        FATAL("pthread_cond_broadcast(%p) failed(%s)", &cond_, SERRNO2(ret));
    }
}
// ------------------------------------------------------------
TcpPairFactory::TcpPairFactory():
    rd_(-1), wr_(-1), server_(-1) {
    // local_ip_ = get_local_ip();
    local_ip_ = "127.0.0.1";
}

TcpPairFactory::~TcpPairFactory() {
    if(rd_ != -1) {
        close(rd_);
        rd_ = -1;
    }
    if(wr_ != -1) {
        close(wr_);
        wr_ = -1;
    }
    if(server_ != -1) {
        close(server_);
        server_ = -1;
    }
}

static void* tcp_pair_factory_thread_function(void* arg) {
    TcpPairFactory* p = static_cast<TcpPairFactory*>(arg);
    return p->thread_function();
}

void* TcpPairFactory::thread_function() {
    sleep_ms(kWaitServerMillSeconds);
    tcp_connect(rd_, local_ip_.c_str(), kListenPort);
    return NULL;
}

int TcpPairFactory::create(int fds[2]) {
    server_ = create_tcp_socket();
    set_ip_reuseaddr(server_);
    tcp_bind_listen(server_, local_ip_.c_str(), kListenPort, 5);
    rd_ = create_tcp_socket(); // client. connect in thread_function.
    pthread_t tid;
    pthread_create(&tid, NULL, tcp_pair_factory_thread_function, this);
    wr_ = tcp_accept(server_);
    pthread_join(tid, NULL);
    fds[0] = rd_;
    fds[1] = wr_;
    return 0;
}

// ------------------------------------------------------------
// FutexCondition Implementation
FutexCondition::FutexCondition(int32_t resource):
    lockword_(kLockWordValue),
    counter_(resource) {
}

bool FutexCondition::wait(int wait_ms) {
    int n = atomic_exchange_and_add(&counter_, -1);
    //DEBUG("dec futex counter=%d",n);
    if(n >= 1) { // at least 1 item, so we can use it.
        //DEBUG("acquire futex tid=%zu,n=%d",static_cast<size_t>(get_tid()),n);
        return true;
    }
    struct timespec* tp = NULL;
    struct timespec ctp;
    if(wait_ms != -1) {
        //DEBUG("futex wait_ms=%d",wait_ms);
        memset(&ctp, 0, sizeof(ctp));
        addtime_timespec(&ctp, wait_ms);
        tp = &ctp;
    }
again:
    n = syscall(__NR_futex, &(lockword_),
                FUTEX_WAIT, kLockWordValue, tp);
    if(n == 0) {
        return true;
    }
    if(errno == EINTR) {
        goto again;
    } else if(errno == ETIMEDOUT) {
        // here we can't AtomicInc otherwise if there are some
        // block threads won't be woke up.
        // but here the threshold is a little bit different.
        // since here we give up FUTEX_WAIT by ourself,
        // we don't need to be woke up.
        anotify_(1, -1);
        //DEBUG("futex timeout wait_ms=%d",wait_ms);
        return false;
    }
    assert(errno != EWOULDBLOCK);
    WARNING("futex(%p,FUTEX_WAIT,0,%p) failed(%s)", &(lockword_), tp, SERRNO);
    return false;
}

bool FutexCondition::anotify() {
    anotify_(1, 0);
    return true;
}

void FutexCondition::anotify_(int wakeup_thread, int counter_threshold) {
    int n = atomic_exchange_and_add(&counter_, 1); // how many resources are there when we up
    if(n >= counter_threshold) {
        return ;
    }
    syscall(__NR_futex, &(lockword_), FUTEX_WAKE, wakeup_thread);
    return ;
}

void FutexCondition::notify() {
    int n = atomic_exchange_and_add(&counter_, 1); // how many resources are there when we up
    if(n >= 0) {
        return ;
    }
    int retry = kRetryCounter;
    while(syscall(__NR_futex, &(lockword_), FUTEX_WAKE, 1) != 1) {
        // maybe the counter_ already dec in 'wait'
        // but in 'wait' not call 'FUTEX_WAIT'
        // so here we have to wait for some rounds.
        if(retry--) {
            nop();
        } else {
            retry = kRetryCounter;
            thread_yield();
        }
    }
}

} // namespace share
