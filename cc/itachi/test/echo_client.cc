/*
 * Copyright (C) dirlt
 */

#include <signal.h>
#include "itachi/itachi.h"
#include "share/logging.h"
#include "share/util.h"
#include "share/socket.h"
#include "share/lock.h"
using namespace itachi;
using namespace share;

class EchoClient: public AsyncClient {
public:
    static const int kLength = 1024;
    struct EchoContext : public AsyncContext {
        char rbuf[kLength];
        char wbuf[kLength];
        int rpos;
        int wpos;
        double session_ms;
        EchoContext(AsyncClient* client):
            AsyncContext(client),
            rpos(0), wpos(0) {
            for(int i = 0; i < kLength; i++) {
                wbuf[i] = 'x';
            }
        }
        virtual ~EchoContext() {
            close_fd();
        }
    }; // class EchoContext
    EchoContext* ctx;
    // ------------------------------
    EchoClient(Itachi* itachi):
        AsyncClient(itachi),
        ctx(NULL) {
    }
    virtual ~EchoClient() {
        // we don't delete ctx explicitly.
    }
    enum {
        AA_CONNECT = AsyncContext::AA_USER + 1,
        AA_READ,
        AA_WRITE,
    };
    //#define ip "10.26.140.39"
#define ip "127.0.0.1"
    void start() {
        ctx = new EchoContext(this);
        int fd = create_tcp_socket();
        set_nonblock(fd);
        if(tcp_connect(fd, ip, 19870) == 1) {
            ctx->initNetWriteEvent(AA_CONNECT, fd);
            itachi->launch(ctx);
        } else {
            // connected.
            ctx->initNetWriteEvent(AA_WRITE, fd);
            itachi->launch(ctx);
        }
    }
    virtual void onComplete(AsyncContext* ctx_) {
        EchoContext* ctx = static_cast<EchoContext*>(ctx_);
        DEBUG("onComplete(%p)", ctx);
        if(ctx->action == AA_CONNECT) {
            tcp_connect(ctx->fd(), ip, 19870);
            ctx->session_ms = gettime_ms();
            ctx->initNetWriteEvent(AA_WRITE, ctx->fd());
            itachi->launch(ctx);
        } else if(ctx->action == AA_READ) {
            DEBUG("ready to read...");
            char buf[64 * 1024];
            int size = read(ctx->fd(), buf, sizeof(buf));
            if(size <= 0 ) { // connection close.
                if(size == 0) {
                    DEBUG("connection#%zu closed", static_cast<size_t>(ctx->id));
                } else {
                    WARNING("read(%d) failed(%s)", ctx->fd(), SERRNO);
                }
                ctx->release();
                return ;
            }
            DEBUG("read size=%d", size);
            memcpy(ctx->rbuf + ctx->rpos, buf , size);
            ctx->rpos += size;
            if(ctx->rpos == kLength) {
                ctx->rpos = 0;
                ctx->wpos = 0;
                memcpy(ctx->wbuf , ctx->rbuf, kLength);
                double current_ms = gettime_ms();
#ifdef TIMER
                TRACE("ping-pong delay %.3lf", current_ms - ctx->session_ms);
#endif
                ctx->session_ms = current_ms;
                ctx->initNetWriteEvent(AA_WRITE, ctx->fd());
                itachi->launch(ctx);
            } else {
                ctx->initNetReadEvent(AA_READ, ctx->fd());
                itachi->launch(ctx);
            }

        } else if(ctx->action == AA_WRITE) {
            DEBUG("ready to write...");
            int size = write(ctx->fd(), ctx->wbuf + ctx->wpos, kLength - ctx->wpos);
            if(size <= 0 ) { // connection close.
                if(size == 0) {
                    DEBUG("connection#%zu closed", static_cast<size_t>(ctx->id));
                } else {
                    WARNING("write(%d) failed(%s)", ctx->fd(), SERRNO);
                }
                ctx->release();
                return ;
            }
            ctx->wpos += size;
            DEBUG("written %d, whole %d", size, kLength);
            if(ctx->wpos >= kLength) {
                ctx->wpos = 0;
                ctx->rpos = 0;
                ctx->initNetReadEvent(AA_READ, ctx->fd());
                itachi->launch(ctx);
            } else {
                ctx->initNetWriteEvent(AA_WRITE, ctx->fd());
                itachi->launch(ctx);
            }
        }
    }
}; // class EchoClient

static volatile bool exit_ = false;
void sig_handler(int /*signo*/) {
    exit_ = true;
}


int main() {
    Itachi itachi;
    signal(SIGINT, sig_handler);
    signal(SIGPIPE, SIG_IGN);
    DEBUG("itachi.start...");
    itachi.start(8 , 5); // specify threads.
    static const int kConnectionNumber = 2;
    EchoClient* client[kConnectionNumber];
    for(int i = 0; i < kConnectionNumber; i++) {
        client[i] = new EchoClient(&itachi);
        client[i]->start();
    }
    TRACE("connections %d start over", kConnectionNumber);
    while(1) {
        if(exit_) {
            itachi.stop();
            break;
        }
        sleep_ms(1000);
    };
    for(int i = 0; i < kConnectionNumber; i++) {
        delete client[i];
    }
    return 0;
}
