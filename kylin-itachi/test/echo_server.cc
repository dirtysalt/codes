/*
 * Copyright (C) dirlt
 */

#include <signal.h>
#include "itachi/itachi.h"
#include "share/logging.h"
#include "share/util.h"
#include "share/socket.h"

using namespace itachi;
using namespace share;

class EchoServer: public AsyncClient {
public:
    static const int kLength = 1024;
    struct EchoContext : public AsyncContext {
        char rbuf[kLength];
        char wbuf[kLength];
        int rpos;
        int wpos;
        EchoContext(AsyncClient* client):
            AsyncContext(client),
            rpos(0), wpos(0) {
        }
        virtual ~EchoContext() {
            close_fd();
        }
    }; // class EchoContext
    EchoContext* ctx;
    // ------------------------------
    EchoServer(Itachi* itachi):
        AsyncClient(itachi),
        ctx(NULL) {
    }
    virtual ~EchoServer() {
        delete ctx;
    }
    enum {
        AA_BIND_LISTEN = AsyncContext::AA_USER + 1,
        AA_READ,
        AA_WRITE,
    };
    //#define ip "10.26.140.39"
#define ip "127.0.0.1"
    void start() {
        ctx = new EchoContext(this);
        int fd = create_tcp_socket();
        set_nonblock(fd);
        set_ip_reuseaddr(fd);
        tcp_bind_listen(fd, ip, 19870, 1024);
        ctx->initNetReadEvent(AA_BIND_LISTEN, fd);
        itachi->launch(ctx);
    }
    virtual void onComplete(AsyncContext* ctx_) {
        EchoContext* ctx = static_cast<EchoContext*>(ctx_);
        DEBUG("onComplete(%p)", ctx);
        if(ctx->action == AA_BIND_LISTEN) {
            DEBUG("ready to accept...");
            int conn = tcp_accept(ctx->fd());
            if(conn == -1) {
                // failed.
                return ;
            }
            set_nonblock(conn);
            EchoContext* ctx2 = new EchoContext(ctx->client);
            ctx2->initNetReadEvent(AA_READ, conn);
            itachi->launch(ctx2);
            ctx->initNetReadEvent(AA_BIND_LISTEN, ctx->fd());
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
            memcpy(ctx->rbuf + ctx->rpos , buf , size);
            ctx->rpos += size;
            if(ctx->rpos == kLength) {
                DEBUG("read to write back...");
                ctx->wpos = 0;
                memcpy(ctx->wbuf , ctx->rbuf, kLength);
                ctx->rpos = 0;
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
            if(ctx->wpos == kLength) {
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
};  // class EchoServer

static volatile bool exit_ = false;
void sig_handler(int /*signo*/) {
    exit_ = true;
}


int main() {
    Itachi itachi;
    signal(SIGINT, sig_handler);
    signal(SIGPIPE, SIG_IGN);
    DEBUG("itachi.start...");
    itachi.start(8, 5); // specify threads.
    EchoServer server(&itachi);
    server.start();
    while(1) {
        if(exit_) {
            itachi.stop();
            break;
        }
        sleep_ms(1000);
    };
    return 0;
}
