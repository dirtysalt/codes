/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <atomic>
#include <thread>

#include "Common.h"

// https://preshing.com/20120515/memory-reordering-caught-in-the-act/

using namespace std;

atomic<int> t0, t1, ctl;
int r0, r1;
int X, Y;
const int waiting = 20;

#define WAIT_AND_SET(t, exp, act)                     \
    do {                                              \
        for (;;) {                                    \
            int _exp = exp;                           \
            if (t.compare_exchange_strong(_exp, 0)) { \
                break;                                \
            }                                         \
        }                                             \
    } while (0)

#ifdef USE_FENCE
// #define FENCE() atomic_thread_fence(memory_order_seq_cst)
#define FENCE() _mm_mfence()
#else
#define FENCE()
#endif

void thread0() {
    for (;;) {
        WAIT_AND_SET(t0, 1, 0);
        while ((rand() % waiting) != 0) {
        }

        X = 1;
        FENCE();
        r0 = Y;

        ctl.fetch_add(1);
    }
}

void thread1() {
    for (;;) {
        WAIT_AND_SET(t1, 1, 0);
        while ((rand() % waiting) != 0) {
        }

        Y = 1;
        FENCE();
        r1 = X;

        ctl.fetch_add(1);
    }
}

void control() {
    int detected = 0;
    int iterations = 0;

    for (;;) {
        X = 0;
        Y = 0;
        iterations++;
        t0.store(1);
        t1.store(1);

        WAIT_AND_SET(ctl, 2, 0);
        if (r1 == 0 && r0 == 0) {
            detected++;
            printf("%d reorders detected after %d iterations\n", detected, iterations);
        }
    }
}

int main() {
    // initialization.
    r0 = 1;
    r1 = 1;
    t0 = 0;
    t1 = 0;
    ctl = 0;
    X = 0;
    Y = 0;
    // start thread.
    thread _t0(thread0);
    thread _t1(thread1);
    thread _ctl(control);
    _t0.join();
    _t1.join();
    _ctl.join();
    return 0;
}
