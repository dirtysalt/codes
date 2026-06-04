/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <atomic>
#include <cstdint>
#include <iostream>
#include <thread>
using namespace std;

volatile int value = 0;
std::atomic<int> flag{0};

void watch() {
    int tick = 20;
    for (;;) {
        if (tick == 0) {
            break;
        }
        bool x = flag.load();
        if (x == 1) {
            fprintf(stderr, "*** ");
            tick--;
        }
        fprintf(stderr, "[%s] %d\n", value == 0 ? "F" : "", value);
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
}

void update() {
    std::this_thread::sleep_for(std::chrono::milliseconds(2000));
    flag.store(1);
    return;
}

int main() {
    std::thread t1(watch);
    std::thread t2(update);
    t1.join();
    t2.join();
    return 0;
}
