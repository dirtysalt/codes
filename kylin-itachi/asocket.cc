/* coding:utf-8
 * Copyright (C) dirlt
 */

#include "share/util.h"
#include "share/socket.h"
#include "itachi/asocket.h"

namespace itachi {

using namespace share;

// ------------------------------------------------------------
// Message Implementation.
void Message::onRecv() {
    body_off = 0;
    body.clear();
}
void Message::onSend() {
    body_off = 0;
    body_len = body.size();
}

int Message::read(int fd) {
    char buf[kReadBufferSize];
    while(1) {
        int code =::read(fd, buf, sizeof(buf));
        if(code == 0) {
            return kEOF;
        } else if(code == -1) {
            if(errno == EAGAIN) {
                return kWouldBlock;
            } else {
                return kError;
            }
        }
        int off = 0;
        // fill header.
        if(body_off < sizeof(body_len)) {
            int x = std::min(sizeof(body_len) - body_off, static_cast<size_t>(code));
            memcpy(reinterpret_cast<char*>(&body_len) + body_off, buf + off, x);
            body_off += x;
            off += x;
        }

        // if header is not OK or no rest data.
        if((body_off < sizeof(body_len)) ||
                (code <= off)) {
            continue;
        }

        body.append(buf + off, code - off);
        body_off += (code - off);
        // check whether it's OK.
        if(body_len >= body.size()) {
            DEBUG("(sizeof(body_len) + body_len)=%zu, body_off=%zu",
                  sizeof(body_len) + body_len,
                  static_cast<size_t>(body_off));
            assert((sizeof(body_len) + body_len) == body_off);
            return kDone;
        }

    } // while(1)
    FATAL("impossible");
}

int Message::write(int fd) {
    int code = 0;
    while(1) {
        if(body_off < sizeof(body_len)) {
            code =::write(fd, reinterpret_cast<const char*>(&body_len) + body_off,
                          sizeof(body_len) - body_off);
        } else {
            int rest = body.size() - body_off + sizeof(body_len);
            if(rest <= 0) {
                return kDone;
            }
            code =::write(fd, string_as_array(&body) + body_off - sizeof(body_len), rest);
        }
        if(code == -1) {
            if(errno == EAGAIN) {
                return kWouldBlock;
            } else if(errno == EPIPE) {
                return kBrokenPipe;
            } else {
                return kError;
            }
        } else if(code == 0) {
            FATAL("::write(%d)=0 ?", fd);
        } else {
            body_off += code;
        }
    } // while(1)
    FATAL("impossible");
}

// ------------------------------------------------------------
// AsyncSocket Implementation.
AsyncSocket::AsyncSocket(Itachi* itachi):
    AsyncContext(&iclient_),
    msg_(NULL),
    ip_("255.255.255.255"),
    port_(-1),
    iclient_(itachi),
    itachi(itachi) {
    net.fd = -1;
}

AsyncSocket::AsyncSocket(AsyncSocket* conn, int fd):
    AsyncContext(&iclient_),
    msg_(NULL),
    ip_("255.255.255.255"),
    port_(-1),
    iclient_(conn->itachi),
    itachi(conn->itachi) {
    net.fd = fd;
}

AsyncSocket::~AsyncSocket() {
    close();
}

int AsyncSocket::bindAndListen(const char* ip, int port, int backlog) {
    int fd = create_tcp_socket();
    if(fd == -1) {
        WARNING("create_tcp_socket failed");
        return -1;
    }
    set_tcp_nodelay(fd);
    set_ip_reuseaddr(fd);
    set_nonblock(fd);
    if(tcp_bind_listen(fd, ip, port, backlog) == -1) {
        WARNING("tcp_bind_listen failed");
        return -1;
    }
    initNetReadEvent(AA_BIND_LISTEN, fd);
    if(itachi->launch(this) == -1) {
        WARNING("itachi->launch(%p) failed", this);
        return -1;
    }
    return 0;
}

int AsyncSocket::connect(const char* ip, int port, int timeout_ms) {
    ip_ = ip;
    port_ = port;
    timeout_ms_ = timeout_ms;

    int fd = create_tcp_socket();
    if(fd == -1) {
        WARNING("create_tcp_socket failed");
        return -1;
    }
    set_tcp_nodelay(fd);
    set_nonblock(fd);
    int code = tcp_connect(fd, ip, port);
    if(code == -1) {
        WARNING("tcp_connect failed");
        return -1;
    }
    if(code == 0) { // already connected.
        net.fd = fd;
        initCpuEvent(AA_CONNECTED);
    } else { // in progress
        initNetWriteEvent(AA_CONNECT, fd, timeout_ms);
    }
    if(itachi->launch(this) == -1) {
        WARNING("itachi->launch(%p) failed", this);
        return -1;
    }
    return 0;
}

int AsyncSocket::reconnect() {
    close();
    return connect(ip_.c_str(), port_, timeout_ms_);
}

int AsyncSocket::accept() {
    int sock = tcp_accept(fd());
    set_nonblock(sock);
    set_tcp_nodelay(sock);
    return sock;
}

void AsyncSocket::close() {
    close_fd();
    delete msg_;
}

int AsyncSocket::recv(Message* msg, int timeout_ms) {
    initNetReadEvent(AA_READ, fd(), timeout_ms);
    if(itachi->launch(this) == -1) {
        WARNING("itachi->launch(%p) failed", this);
        return -1;
    }
    if(msg_) {
        WARNING("message resides in socket");
        return -1;
    }
    msg->onRecv();
    io_timestamp_ = static_cast<uint64_t>(gettime_ms());
    io_timeout_ms_ = timeout_ms;
    msg_ = msg;

    return 0;
}

int AsyncSocket::send(Message* msg, int timeout_ms) {
    initNetWriteEvent(AA_WRITE, fd(), timeout_ms);
    if(itachi->launch(this) == -1) {
        WARNING("itachi->launch(%p) failed", this);
        return -1;
    }
    if(msg_) {
        WARNING("message resides in socket");
        return -1;
    }
    msg->onSend();
    io_timestamp_ = static_cast<uint64_t>(gettime_ms());
    io_timeout_ms_ = timeout_ms;
    msg_ = msg;
    return 0;
}

#define ITACHI_WITHOUT_CODE() do {                             \
        WARNING("%s",__PRETTY_FUNCTION__);                   \
        release();                                                 \
    }while(0)
#define ITACHI_WITH_CODE()  do {                                        \
        WARNING("%s(%s)",__PRETTY_FUNCTION__,SERRNO2(code));          \
        release();                                                          \
    }while(0)
void AsyncSocket::onConnectTimeout() {
    ITACHI_WITHOUT_CODE();
}
void AsyncSocket::onConnected() {
    ITACHI_WITHOUT_CODE();
}
void AsyncSocket::onConnectFailed(int code) {
    ITACHI_WITH_CODE();
}
void AsyncSocket::onAccept() {
    ITACHI_WITHOUT_CODE();
}
void AsyncSocket::onRecvOK() {
    ITACHI_WITHOUT_CODE();
}
void AsyncSocket::onRecvTimeout() {
    ITACHI_WITHOUT_CODE();
}
void AsyncSocket::onPeerClosed() {
    ITACHI_WITHOUT_CODE();
}
void AsyncSocket::onRecvFailed(int code) {
    ITACHI_WITH_CODE();
}
void AsyncSocket::onSendOK() {
    ITACHI_WITHOUT_CODE();
}
void AsyncSocket::onSendTimeout() {
    ITACHI_WITHOUT_CODE();
}
void AsyncSocket::onBrokenPipe() {
    ITACHI_WITHOUT_CODE();
}
void AsyncSocket::onSendFailed(int code) {
    ITACHI_WITH_CODE();
}
#undef ITACHI_WITH_CODE
#undef ITACHI_WITHOUT_CODE

// ------------------------------------------------------------
// AsyncSocket::Client Implementation.
AsyncSocket::Client::Client(Itachi* itachi):
    AsyncClient(itachi) {
}

void AsyncSocket::Client::onComplete(AsyncContext* ctx_) {
    AsyncSocket* ctx = static_cast<AsyncSocket*>(ctx_);
    int code = 0;
    switch(ctx->action) {
        case AA_CONNECT: {
            if(ctx->isTimeout()) {
                ctx->onConnectTimeout();
            } else {
                // NOTE(dirlt): not right to connect again.
                // code = tcp_connect(ctx->fd(), ctx->ip_.c_str(), ctx->port_);
                // assert(code != 1 && (code == 0 || code == -1));
                code = get_socket_error(ctx->fd());
                if(code == 0) {
                    ctx->onConnected();
                } else {
                    ctx->onConnectFailed(errno);
                }
            }
        }
        break;
        case AA_CONNECTED:
            ctx->onConnected();
            break;
        case AA_BIND_LISTEN:
            ctx->onAccept();
            break;
        case AA_READ:
            assert(ctx->msg_);
            code = ctx->msg_->read(ctx->fd());
            if(code == Message::kDone) {
                ctx->onRecvOK();
            } else if(code == Message::kWouldBlock) {
                int64_t rest_ms = -1;
                if(ctx->io_timeout_ms_ > 0) {
                    rest_ms = (ctx->io_timestamp_ + ctx->io_timeout_ms_) -
                              static_cast<uint64_t>(gettime_ms());
                    if(rest_ms <= 0) {
                        ctx->onRecvTimeout();
                        return ;
                    }
                }
                ctx->initNetReadEvent(AA_READ, ctx->fd(), rest_ms);
                if(itachi->launch(ctx) == -1) {
                    FATAL("itachi->launch(%p) failed", ctx);
                }
            } else if(code == Message::kEOF) {
                ctx->onPeerClosed();
            } else if(code == Message::kError) {
                ctx->onRecvFailed(errno);
            }
            break;
        case AA_WRITE:
            assert(ctx->msg_);
            code = ctx->msg_->write(ctx->fd());
            if(code == Message::kDone) {
                ctx->onSendOK();
            } else if(code == Message::kWouldBlock) {
                int64_t rest_ms = -1;
                if(ctx->io_timeout_ms_ > 0) {
                    rest_ms = (ctx->io_timestamp_ + ctx->io_timeout_ms_) -
                              static_cast<uint64_t>(gettime_ms());
                    if(rest_ms <= 0) {
                        ctx->onSendTimeout();
                        return ;
                    }
                }
                ctx->initNetWriteEvent(AA_WRITE, ctx->fd(), rest_ms);
                if(itachi->launch(ctx) == -1) {
                    FATAL("itachi->launch(%p) failed", ctx);
                }
            } else if(code == Message::kBrokenPipe) {
                ctx->onBrokenPipe();
            } else if(code == Message::kError) {
                ctx->onSendFailed(errno);
            }
            break;
        default:
            FATAL("unknown ctx(%p)->action(%d)", ctx, ctx->action);
    }
    return ;
}

} // namespace itachi
