/*
 * Copyright (C) dirlt
 */

#include "share/util.h"
#include "share/logging.h"
#include "itachi/itachi.h"
#include "itachi/handler.h"

namespace itachi {

// ------------------------------------------------------------
// Handler Implementation.
Handler::Handler(Itachi* itachi):
    itachi_(itachi), threads_(0),
    tids_(NULL), args_(NULL) {
}

Handler::~Handler() {
    fini();
}

void Handler::init(int threads) {
    fini();
    tids_ = new pthread_t[threads];
    args_ = new ThreadArg[threads];
}

void Handler::fini() {
    if(tids_) {
        delete [] tids_;
        tids_ = NULL;
    }
    if(args_) {
        delete [] args_;
        args_ = NULL;
    }
}

static void* proxy_thread_function(void* arg) {
    Handler::ThreadArg* xarg = static_cast<Handler::ThreadArg*>(arg);
    xarg->tid = get_tid();
    return xarg->handler->thread_function(xarg->id);
}

void Handler::start(int threads) {
    init(threads);
    threads_ = threads;
    for(int i = 0; i < threads; i++) {
        args_[i].handler = this;
        args_[i].id = i;
        int ret = pthread_create(tids_ + i, NULL, proxy_thread_function, args_ + i);
        if(ret != 0) {
            FATAL("pthread_create(%p+%d,%p,%p) failed(%s)",
                  tids_ + i, i, proxy_thread_function,
                  this, SERRNO2(ret));
        }
    }
}

void Handler::stop() {
    for(int i = 0; i < threads_; i++) {
        pthread_join(tids_[i], NULL);
    }
    fini();
}

// ------------------------------------------------------------
// CpuHandler Implementation.
CpuHandler::CpuHandler(Itachi* itachi):
    Handler(itachi), queue_(NULL) {
}

CpuHandler::~CpuHandler() {
    fini();
}

void CpuHandler::init(int threads) {
    fini();
    queue_ = new Q[threads];
}

void CpuHandler::fini() {
    if(queue_) {
        delete [] queue_;
        queue_ = NULL;
    }
}

void CpuHandler::start(int threads) {
    init(threads);
    Handler::start(threads);
}

void CpuHandler::stop() {
    Handler::stop();
    fini();
}

int CpuHandler::push(AsyncContext* ctx) {
    if(itachi_->stop_) {
        WARNING("itachi %p already stop", itachi_);
        return -1;
    }
    int id = ctx->thread_hint % threads_;
    DEBUG("cpu push ctx(%p) to queue#%d%s", ctx, id,
          ctx->cpu.urgent ? "(urgent)" : "");
    if(ctx->cpu.urgent) {
        queue_[id].push_front(ctx);
    } else {
        queue_[id].push(ctx);
    }
    return 0;
}

void* CpuHandler::thread_function(int id) {
    while(1) {
        if(itachi_->stop_) {
            break;
        }
        AsyncContext* ctx = NULL;
        if(!queue_[id].pop(&ctx, kQueueWaitTimeoutMillSeconds)) {
            DEBUG("cpu queue#%d empty", id);
            continue;
        }
        ctx->client->onComplete(ctx);
        ctx->release();

        // try to fetch more contexts.
        queue_[id].clear(&ctx);
        while(ctx) {
            AsyncContext* next = ctx->next;
            ctx->client->onComplete(ctx);
            ctx->release();
            ctx = next;
        }
    } // while(1)
    return NULL;
}

// ------------------------------------------------------------
// PollHandler Implementation
PollHandler::PollHandler(Itachi* itachi):
    Handler(itachi), queue_(NULL),  loop_(NULL), async_(NULL) {
}

PollHandler::~PollHandler() {
    fini();
}

static void async_callback(struct ev_loop* loop, ev_async* watcher, int revents) {
    assert(loop);
    assert(watcher);
    assert(revents == EV_ASYNC);
}

void PollHandler::init(int threads) {
    fini();
    queue_ = new Q[threads];
    loop_ = new struct ev_loop* [threads];
    async_ = new ev_async [threads];
    for(int i = 0; i < threads; i++) {
        loop_[i] = ev_loop_new(EVBACKEND_EPOLL);
        if(!loop_[i]) {
            FATAL("ev_loop_new(EVBACKEND_EPOLL) failed");
        }
        ev_ref(loop_[i]);
        ev_async_init(async_ + i, async_callback);
        ev_async_start(loop_[i], async_ + i);
    }
}

void PollHandler::fini() {
    if(queue_) {
        delete [] queue_;
        queue_ = NULL;
    }
    if(loop_) {
        for(int i = 0; i < threads_; i++) {
            ev_unref(loop_[i]);
            ev_loop_destroy(loop_[i]);
        }
        delete [] loop_;
        loop_ = NULL;
    }
    if(async_) {
        delete [] async_;
        async_ = NULL;
    }
}

void PollHandler::start(int threads) {
    init(threads);
    Handler::start(threads);
}


void PollHandler::stop() {
    for(int i = 0; i < threads_; i++) {
        ev_async_send(loop_[i], async_ + i);
    }
    Handler::stop();
    fini();
}

int PollHandler::push(AsyncContext* ctx) {
    if(itachi_->stop_) {
        WARNING("itachi %p already stop", itachi_);
        return -1;
    }
    int id = ctx->thread_hint % threads_;
    DEBUG("poll push ctx(%p) to queue#%d", ctx, id);
    queue_[id].push(ctx);
    // TODO(dirlt):not too frequent notification.
    ev_async_send(loop_[id], async_ + id);
    return 0;
}

static void net_callback(int revents, void* arg) {
    AsyncContext* ctx = static_cast<AsyncContext*>(arg);
    if(revents & EV_ERROR) {
        FATAL("libev raise EV_ERROR");
    }
    ctx->net.readable = (revents & EV_READ);
    ctx->net.writeable = (revents & EV_WRITE);
    ctx->net.timeout = (revents & EV_TIMER) &&  !ctx->net.readable && !ctx->net.writeable;
    ctx->initCpuEvent(ctx->action);
    if(ctx->client->itachi->launch_(ctx, false) == -1) { // !auto_acquire.
        FATAL("ctx->client->itachi->_launch(%p) failed", ctx);
    }
}

void* PollHandler::thread_function(int id) {
    while(1) {
        if(itachi_->stop_) {
            break;
        }
        ev_run(loop_[id], EVRUN_ONCE);
        AsyncContext* ctx = NULL;
        queue_[id].clear(&ctx);
        while(ctx) {
            switch(ctx->type) {
                case AsyncContext::NET:
                    ev_once(loop_[id], ctx->net.fd, ctx->net.events,
                            ctx->net.timeout_ms < 0 ? -1 : ctx->net.timeout_ms * 0.001,
                            net_callback, ctx);
                    break;
                default:
                    FATAL("unknown %p->type(%d)", ctx, ctx->type);
            }
            ctx = ctx->next;
        }
    } // while(1)
    return NULL;
}

} // namespace itachi
