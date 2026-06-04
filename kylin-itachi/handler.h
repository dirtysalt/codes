/*
 * Copyright (C) dirlt
 */

#ifndef __CC_ITACHI_HANDLER_H__
#define __CC_ITACHI_HANDLER_H__


#include <pthread.h>
#include <ev.h>
#include "share/lock.h"
#include "share/cond.h"
#include "share/queue.h"
#include "share/util.h"
#include "share/logging.h"

namespace itachi {

class Itachi;
class AsyncContext;

// ------------------------------------------------------------
// Handler Interface. In essence it's a threadpool.
class Handler {
public:
    Handler(Itachi* itachi);
    virtual ~Handler();
    void start(int threads);
    void stop();
    virtual void* thread_function(int id) = 0;
    struct ThreadArg {
        Handler* handler;
        int id;
        pid_t tid;
    }; // struct ThreadArg
    pid_t get_tid(int n) {
        return args_[n % threads_].tid;
    }
protected:
    Itachi* itachi_;
    int threads_;
private:
    friend class Itachi;
    void init(int threads);
    void fini();
    pthread_t* tids_;
    ThreadArg* args_;
}; // class Handler

// ------------------------------------------------------------
// CpuHandler Interface.
class CpuHandler: public Handler {
public:
    CpuHandler(Itachi* itachi);
    ~CpuHandler();
    void start(int threads);
    void stop();
    int push(AsyncContext* ctx);
    virtual void* thread_function(int id);
private:
    void init(int threads);
    void fini();
    friend class Itachi;
    static const int kQueueWaitTimeoutMillSeconds = 2000;
    typedef share::BlockingSLinkedListQueue < AsyncContext* > Q;
    Q* queue_;
}; // class CpuHandler

// ------------------------------------------------------------
// PollHandler Interface.
class PollHandler: public Handler {
public:
    PollHandler(Itachi* itachi);
    ~PollHandler();
    void start(int threads);
    void stop();
    int push(AsyncContext* ctx);
    virtual void* thread_function(int id);
private:
    void init(int threads);
    void fini();
    friend class Itachi;
    typedef share::BlockingSLinkedListQueue < AsyncContext* > Q;
    Q* queue_;
    struct ev_loop** loop_;
    struct ev_async* async_;
}; // class PollHandler

} // namespace itachi

#endif // __CC_ITACHI_HANDLER_H__
