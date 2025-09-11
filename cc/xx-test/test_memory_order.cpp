/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <atomic>
#include <chrono>
#include <iostream>
#include <thread>

std::atomic<int64_t> M0, M1;

void thread0() {
    for (;;) {
        M0.fetch_add(1, std::memory_order_relaxed);
        M1.fetch_add(1, std::memory_order_relaxed);
        std::this_thread::sleep_for(std::chrono::seconds(2));
    }
}

void thread1() {
    for (;;) {
        int64_t m0 = M0.load(std::memory_order_relaxed);
        int64_t m1 = M1.load(std::memory_order_relaxed);
        std::cout << "m0 = " << m0 << ", m1 = " << m1 << "\n";
        std::this_thread::sleep_for(std::chrono::seconds(2));
    }
}

int main() {
    // initialization.
    M0 = 0;
    M1 = 0;
    // start thread.
    std::thread _t0(thread0);
    std::thread _t1(thread1);
    _t0.join();
    _t1.join();
    return 0;
}
