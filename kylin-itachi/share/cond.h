/*
 * Copyright (C) dirlt
 */

#ifndef __CC_SHARE_CONDITION_H__
#define __CC_SHARE_CONDITION_H__

#include <sys/time.h>
#include <sys/epoll.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h>
#include <pthread.h>
#include <cassert>
#include <string>
//#include "share/lock.h"
#include "share/logging.h"
#include "share/socket.h"
#include "share/atomic.h"
#include "share/util.h"

namespace share {

// ------------------------------------------------------------
// Condition Interface.
class MutexLock;
class Condition {
public:
    explicit Condition(MutexLock& mutex);
    ~Condition();
    void wait();
    bool timedWait(struct timespec* tp);
    void notify();
    void notifyAll();
private:
    MutexLock& mutex_;
    pthread_cond_t cond_;
}; // class Condition

// ------------------------------------------------------------
// NopCondition Interface.
class NopCondition {
public:
    NopCondition() {}
    ~NopCondition() {}
    bool wait(int /*wait_sec*/) {
        return true;
    }
    void notify() {}
    bool anotify() {
        return true;
    }
}; // class NopCondition

// ------------------------------------------------------------
// TODO(dirlt): I don't think the following code is stable and
// don not have well test!!!
// ------------------------------------------------------------
// FileDescriptorCondition Interface.(MWMR)
template< typename T >
class FileDescriptorCondition {
public:
    FileDescriptorCondition(): epfd_(-1) {
        fds_[0] = -1;
        fds_[1] = -1;
        if(factory_.create(fds_) != 0) {
            FATAL("factory create fds(%p) failed(%s)", fds_, SERRNO);
        }
        set_nonblock(fds_[0]);
        set_nonblock(fds_[1]);
        // fds_[0] for reading.
        // fds_[1] for writing.
        epfd_ = epoll_create(2);
        if(epfd_ == -1) {
            FATAL("epoll_create(2) failed(%s)", SERRNO);
        }
        memset(&event_, 0, sizeof(event_));
        event_.events = EPOLLIN;
        if(epoll_ctl(epfd_, EPOLL_CTL_ADD, fds_[0], &event_) != 0) {
            FATAL("epoll_ctl(%d,EPOLL_CTL_ADD,%d,%p) failed(%s)",
                  epfd_, fds_[0], &event_, SERRNO);
        }
    }
    ~FileDescriptorCondition() {
        if(fds_[0] != -1) {
            close(fds_[0]);
            fds_[0] = -1;
        }
        if(fds_[1] != -1) {
            close(fds_[1]);
            fds_[1] = -1;
        }
        if(epfd_ != -1) {
            close(epfd_);
            epfd_ = -1;
        }
    }
    bool wait(int wait_ms) {
        // notice it's not atomic here in multithreads.
        // if epoll_wait return n==1, in multithreads.
        // doesn't means ::read will nonblock.
        // but in single threads, it works fine.
        // however we can try one more time since ::read is atomic.
        char c[1];
        if(::read(fds_[0], c, sizeof(c)) == 1) {
            return true;
        }
        if(errno != EAGAIN && errno != EWOULDBLOCK) {
            WARNING("read(%d) failed(%s)", fds_[0], SERRNO);
            return false;
        }
        if(wait_ms <= 0) {
            return false;
        }
        struct epoll_event events[1];
        while(wait_ms > 0) {
            double now = gettime_ms();
            int n = epoll_wait(epfd_, events, 1, wait_ms);
            if(n < 0) {
                WARNING("epoll_wait(%d,%p,1,%d) failed(%s)",
                        epfd_, events, wait_ms, SERRNO);
                return false;
            }
            if(n == 0) {
                return false;
            }
            assert(n == 1);
            if(::read(fds_[0], c, sizeof(c)) == 1) {
                return true;
            }
            if(errno != EAGAIN && errno != EWOULDBLOCK) {
                WARNING("read(%d) failed(%s)", fds_[0], SERRNO);
                return false;
            }
            double now2 = gettime_ms();
            wait_ms -= static_cast<int>(now2 - now);
            if(wait_ms <= 0) {
                return false;
            }
            now = now2;
        } // while(wait_ms > 0)
        return true;
    }
    bool anotify() {
        char c[1] = {'x'};
        if(::write(fds_[1], c, sizeof(c)) != 1) {
            if(errno != EAGAIN && errno != EWOULDBLOCK) {
                WARNING("write(%d) failed(%s)", fds_[1], SERRNO);
            }
            return false;
        }
        return true;
    }
    static const int kRetryCounter = 10;
    void notify(int retry_counter = kRetryCounter) {
        int retry = retry_counter;
        while(!anotify()) {
            if(errno != EAGAIN && errno != EWOULDBLOCK) {
                return ;
            }
            retry--;
            if(retry == 0) {
                retry = kRetryCounter;
                thread_yield();
            }
        }
    }
private:
    T factory_; // int create(int fds[2]);
    int fds_[2];
    int epfd_;
    struct epoll_event event_;
}; // class FileDescriptorCondition

class PipePairFactory {
public:
    int create(int fds[2]) {
        return pipe(fds);
    }
}; // class PipeFdFactory

class SocketPairFactory {
public:
    int create(int fds[2]) {
        return socketpair(AF_UNIX, SOCK_STREAM, 0, fds);
    }
}; // class SocketPairFactory

// just for benchcase.
class TcpPairFactory {
public:
    TcpPairFactory();
    void* thread_function();
    static const int kListenPort = 19870;
    static const int kWaitServerMillSeconds = 200;
    int create(int fds[2]);
    ~TcpPairFactory();
private:
    int rd_;
    int wr_;
    int server_;
    std::string local_ip_;
}; // class TcpPairFactory

typedef FileDescriptorCondition< PipePairFactory > PipePairCondition;
typedef FileDescriptorCondition< SocketPairFactory > SocketPairCondition;
typedef FileDescriptorCondition< TcpPairFactory > TcpPairCondition;

// ------------------------------------------------------------
// FutexCondition Interface.(MWMR)
class FutexCondition {
public:
    FutexCondition(int32_t resource = 0);
    bool wait(int wait_ms);
    bool anotify();
    void notify();
    int32_t counter() const {
        return AtomicGetValue(counter_);
    }
private:
    void anotify_(int wakeup_thread, int counter_threshold);
    static const int kLockWordValue = 0;
    static const int kRetryCounter = 10;
    static const int kWakeupThreadNumber = 1;
    volatile int lockword_;
    mutable volatile int32_t counter_;
}; // class FutexCondition

} // namespace share

#endif // __CC_SHARE_CONDITION_H__
