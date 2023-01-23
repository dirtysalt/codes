/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <signal.h>
#include "itachi/asocket.h"

using namespace itachi;

class AsyncSocketEchoClient: public AsyncSocket {
public:
    AsyncSocketEchoClient(Itachi* itachi):
        AsyncSocket(itachi) {
    }
    virtual void onRecvOK() {
        Message* msg = takeOutMessage();
        TRACE("onRecvOK body_len(%u) body(%s)", msg->body_len,
              msg->body.c_str());
        send(msg);
    }
    virtual void onSendOK() {
        Message* msg = takeOutMessage();
        TRACE("onSendOK body_len(%u) body(%s)", msg->body_len,
              msg->body.c_str());
        recv(msg);
    }
    virtual void onConnected() {
        Message* msg = new Message();
        msg->body = "hello";
        send(msg);
    }
}; // class AsyncSocketEchoClient

static volatile bool exit_ = false;
void sig_handler(int /*signo*/) {
    exit_ = true;
}

int main() {
#define ip "127.0.0.1"
    signal(SIGINT, sig_handler);
    signal(SIGPIPE, SIG_IGN);
    Itachi itachi;
    itachi.start(1, 1);
    AsyncSocketEchoClient client(&itachi);
    client.acquire();
    client.connect(ip, 19870);
    while(1) {
        if(exit_) {
            itachi.stop();
            break;
        }
        sleep_ms(1000);
    }
    return 0;
}
