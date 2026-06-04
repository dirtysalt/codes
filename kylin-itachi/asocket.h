/* coding:utf-8
 * Copyright (C) dirlt
 */

#ifndef __CC_ITACHI_ASOCKET_H__
#define __CC_ITACHI_ASOCKET_H__

#include "share/byte_array.h"
#include "share/lock.h"
#include "share/socket.h"
#include "itachi/itachi.h"

namespace itachi {

// ------------------------------------------------------------
// Message with uint32_t as body_len.
struct Message {
public:
    static const int kReadBufferSize = 64 * (1 << 10); // 64K.
    virtual ~Message() {}
    enum {
        kDone, // both.
        kWouldBlock, //both.
        kEOF, // read
        kBrokenPipe, // write.
        kError, // both.
    };
    virtual void onRecv();
    virtual void onSend();
    virtual int read(int fd);
    virtual int write(int fd);
    uint32_t body_len;
    std::string body;
    uint32_t body_off;
}; // class Message

// ------------------------------------------------------------
// AsyncSocket Interface.
class AsyncSocket: public AsyncContext {
public:
    AsyncSocket(Itachi* itachi);
    AsyncSocket(AsyncSocket* socket, int fd);
    virtual ~AsyncSocket();
    int bindAndListen(const char* ip, int port, int backlog);
    int connect(const char* ip, int port, int timeout_ms = -1);
    int reconnect();
    int accept();
    void close();
    int recv(Message* msg, int timeout_ms = -1);
    int send(Message* msg, int timeout_ms = -1);
    Message* takeOutMessage() {
        Message* ret = msg_;
        msg_ = NULL;
        return ret;
    }
    virtual void onConnectTimeout();
    virtual void onConnected();
    virtual void onConnectFailed(int code);
    virtual void onAccept();
    virtual void onRecvOK();
    virtual void onRecvTimeout();
    virtual void onPeerClosed();
    virtual void onRecvFailed(int code);
    virtual void onSendOK();
    virtual void onSendTimeout();
    virtual void onBrokenPipe();
    virtual void onSendFailed(int code);
private:
    enum Action { // action.
        AA_CONNECT = AA_USER + 1,
        AA_CONNECTED,
        AA_BIND_LISTEN,
        AA_READ,
        AA_WRITE,
    };
    class Client: public AsyncClient {
    public:
        Client(Itachi* itachi);
        virtual ~Client() {}
        virtual void onComplete(AsyncContext* ctx);
    }; // class Client
    friend class Client;
private:
    // --------------------
    uint64_t io_timestamp_;
    int io_timeout_ms_;
    Message* msg_;
    // --------------------
    // only for connector.
    std::string ip_;
    int port_;
    int timeout_ms_;
    // --------------------
    Client iclient_;
    Itachi* itachi;
}; // class AsyncSocket

} // namespace itachi

#endif // __CC_ITACHI_ASOCKET_H__
