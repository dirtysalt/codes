/*
 * Copyright (C) dirlt
 */

#include <pthread.h>
#include "share/cond.h"
#include "share/logging.h"
#include "share/util.h"

using namespace share;

int main() {
    {
        PipePairCondition cond;
        assert(cond.wait(100) == false);
        cond.notify();
        assert(cond.wait(1));
        // 2 secs.
        printf("pipe cond wait 2 secs...\n");
        assert(cond.wait(2000) == false);
    }
    {
        SocketPairCondition cond;
        assert(cond.wait(100) == false);
        cond.notify();
        assert(cond.wait(1));
        // 2 secs.
        printf("socketpair cond wait 2 secs...\n");
        assert(cond.wait(2000) == false);
    }
    {
        FutexCondition cond;
        assert(cond.wait(100) == false);
        cond.notify();
        assert(cond.wait(1));
        // 2 secs.
        printf("futex cond wait 2 secs...\n");
        assert(cond.wait(2000) == false);
    }
    return 0;
}
