/*
 * Copyright (C) dirlt
 */

#ifndef __CC_ITACHI_ITACHI_H__
#define __CC_ITACHI_ITACHI_H__

#include <stdint.h>
#include "share/atomic.h"
#include "itachi/handler.h"

namespace itachi {

class Itachi;
class AsyncClient;
class AsyncContext;

// ------------------------------------------------------------
// AsyncClient Interface.
struct AsyncClient {
    AsyncClient(Itachi* itachi):
        itachi(itachi) {}
    virtual ~AsyncClient() {}
    virtual void onComplete(AsyncContext* ctx);
    Itachi* itachi;
}; // class AsyncClient

// ------------------------------------------------------------
// AsyncContxet Interface.
struct AsyncContext:
    public share::RefCount {
public:
    AsyncContext(AsyncClient* client);
    virtual ~AsyncContext() {}
    void release();
    // --------------------
    int fd() const {
        return net.fd;
    }
    int timeout_ms() const {
        return net.timeout_ms;
    }
    bool isTimeout() const {
        return net.timeout;
    }
    bool isReadable() const {
        return net.readable;
    }
    bool isWriteable() const {
        return net.writeable;
    }
    void set_thread_hint(AsyncContext* ctx) {
        thread_hint = ctx->thread_hint;
    }
    void initCpuEvent(int action, bool emergency = false);
    void initNetWriteEvent(int action, int fd, int timeout_ms = -1);
    void initNetReadEvent(int action, int fd, int timeout_ms = -1);
    void initNetEvent(int action, int fd, int timeout_ms = -1); // read and write.
    void close_fd();
    // --------------------
    static volatile uint32_t instance_counter;
    uint64_t id;
    // put into which thread.
    uint32_t thread_hint;
    // --------------------
    // TODO(dirlt):much more type and action.
    // async type.
    enum Type { //type.
        NOP,
        CPU,
        NET,
    };
    // async action.
    enum Action { // action
        AA_NOP,
        AA_CPU,
        AA_NET,
        AA_USER,
    };
    int type;
    int action;
    // --------------------
    // cpu context.
    struct Cpu {
        bool urgent; // put at front of queue.
    } cpu;
    // --------------------
    // net context.
    struct Net {
        int fd;
        int events;
        int timeout_ms;
        bool timeout;
        bool readable;
        bool writeable;
    } net;
    // --------------------
    AsyncClient* client;
    AsyncContext* next;
}; // class AsyncContext

// ------------------------------------------------------------
// Itachi Inteface.
class Itachi {
public:
    Itachi();
    virtual ~Itachi() {}
    int start(int cpu_threads, int poll_threads);
    void stop();
    // you can't launch the same AsyncContext for twice.
    // otherwise the internal state will be out of order.
    int launch(AsyncContext* ctx);
    int launch_(AsyncContext* ctx, bool auto_acquire); // used internally.
private:
    volatile bool stop_;
    friend class AsyncClient;
    friend class CpuHandler;
    CpuHandler cpu_handler_;
    friend class PollHandler;
    PollHandler poll_handler_;
}; // class Itachi

} // namespace itachi

#endif // __CC_ITACHI_ITACHI_H__
