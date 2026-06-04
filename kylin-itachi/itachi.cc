/*
 * Copyright (C) dirlt
 */

#include "share/atomic.h"
#include "share/logging.h"
#include "itachi/itachi.h"

namespace itachi {

// ------------------------------------------------------------
// AsyncClient Implementation.
void AsyncClient::onComplete(AsyncContext* ctx) {
    DEBUG("AsyncClient::onComplete(%p)", ctx);
}

// ------------------------------------------------------------
// AsyncContext Implementation
volatile uint32_t AsyncContext::instance_counter = 0;
AsyncContext::AsyncContext(AsyncClient* client):
    type(NOP),
    action(AA_NOP),
    client(client),
    next(NULL) {
    id = AtomicInc(instance_counter);
    thread_hint = id;
}

void AsyncContext::initCpuEvent(int action, bool emergency) {
    type = CPU;
    this->action = action;
    cpu.urgent = emergency;
}

void AsyncContext::initNetReadEvent(int action, int fd, int timeout_ms) {
    type = NET;
    this->action = action;
    net.fd = fd;
    net.events = EV_READ;
    net.timeout_ms = timeout_ms;
    net.timeout = false;
}

void AsyncContext::initNetWriteEvent(int action, int fd, int timeout_ms) {
    type = NET;
    this->action = action;
    net.fd = fd;
    net.events = EV_WRITE;
    net.timeout_ms = timeout_ms;
    net.timeout = false;
}

void AsyncContext::initNetEvent(int action, int fd, int timeout_ms) {
    type = NET;
    this->action = action;
    net.fd = fd;
    net.events = EV_READ | EV_WRITE;
    net.timeout_ms = timeout_ms;
    net.timeout = false;
}

void AsyncContext::close_fd() {
    ::close(net.fd);
    net.fd = -1;
}

void AsyncContext::release() {
    DEBUG("AsyncContext::release");
    if(RefCount::release() == 0) {
        delete this;
    }
}

// ------------------------------------------------------------
// Itachi Implementation
Itachi::Itachi():
    stop_(true),
    cpu_handler_(this),
    poll_handler_(this) {
}

int Itachi::start(int cpu_threads, int poll_threads) {
    if(!stop_) { // already started.
        WARNING("itachi %p already started", this);
        return -1;
    }
    stop_ = false;
    cpu_handler_.start(cpu_threads);
    poll_handler_.start(poll_threads);
    return 0;
}

void Itachi::stop() {
    stop_ = true;
    cpu_handler_.stop();
    poll_handler_.stop();
}

int Itachi::launch_(AsyncContext* ctx, bool auto_acquire) {
    if(ctx->client->itachi != this) {
        WARNING("ctx->client->itachi(%p)!=this(%p)", ctx->client->itachi, this);
        return -1;
    }
    if(auto_acquire) {
        ctx->acquire();
    }
    int code = 0;
    switch(ctx->type) {
        case AsyncContext::CPU:
            DEBUG("%p->type==CPU", ctx);
            code = cpu_handler_.push(ctx);
            break;
        case AsyncContext::NET:
            DEBUG("%p->type==NET", ctx);
            code = poll_handler_.push(ctx);
            break;
        default:
            DEBUG("unknown %p->type(%d)", ctx, ctx->type);
            code = -1;
            break;
    }
    // rollback.
    if(code != 0) {
        if(auto_acquire) {
            ctx->release();
        }
    }
    return code;
}

int Itachi::launch(AsyncContext* ctx) {
    return launch_(ctx, true);
}

} // namespace itachi
