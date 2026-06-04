/*
 * Copyright (C) dirlt
 */

#include <signal.h>
#include "itachi/itachi.h"
#include "share/logging.h"
#include "share/util.h"

using namespace itachi;

class Client: public AsyncClient {
public:
    AsyncContext* ctx;
    Client(Itachi* itachi):
        AsyncClient(itachi),
        ctx(NULL) {
    }
    virtual ~Client() {
        delete ctx;
    }
    virtual void onComplete(AsyncContext* ctx) {
        TRACE("onComplete(%p)", ctx);
        sleep_ms(1000); // 50ms.
        ctx->initCpuEvent(AsyncContext::AA_NOP);
        itachi->launch(ctx);
    }
    void start() {
        ctx = new AsyncContext(this);
        ctx->initCpuEvent(AsyncContext::AA_NOP);
        itachi->launch(ctx);
    }
};

static volatile bool exit_ = false;
void sig_handler(int /*signo*/) {
    exit_ = true;
}

int main() {
    Itachi itachi;
    signal(SIGINT, sig_handler);
    TRACE("itachi.start...");
    itachi.start(1, 1); // specify threads.
    Client client(&itachi);
    client.start();
    while(1) {
        if(exit_) {
            itachi.stop();
            break;
        }
        sleep_ms(1000);
    };
    return 0;
}
