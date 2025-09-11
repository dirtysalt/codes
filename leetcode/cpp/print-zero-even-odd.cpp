/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <functional>
#include <thread>
#include <condition_variable>
#include <mutex>

using namespace std;

class ZeroEvenOdd {
private:
    int n;
    int stage;
    mutex m;
    condition_variable cv;

public:
    ZeroEvenOdd(int n) {
        this->n = n;
        stage = 0;
    }

#define waitStage(oldValue,newValue)            \
        unique_lock<mutex> lk(m);               \
        while(stage != oldValue) {              \
            cv.wait(lk);                        \
        }                                       \
        stage = newValue;


    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber) {
        int tt = n;
        while(tt > 0) {
            {
                waitStage(0, 1);
                printNumber(0);
                cv.notify_all();
            }
            tt -= 1;
            if (tt <= 0) break;
            {
                waitStage(0, 2);
                printNumber(0);
                cv.notify_all();
            }
            tt -= 1;
        }
    }

    void even(function<void(int)> printNumber) {
        for(int i=2;i<=n;i+=2) {
            waitStage(2, 0);
            printNumber(i);
            cv.notify_all();
        }
    }

    void odd(function<void(int)> printNumber) {
        for(int i=1;i<=n;i+=2) {
            waitStage(1, 0);
            printNumber(i);
            cv.notify_all();
        }
    }
};

void print(int x) {
    printf("%d", x);
}

void test(int n) {
    printf("n = %d -> ", n);
    auto x = ZeroEvenOdd(n);
    std::thread t0(&ZeroEvenOdd::zero, &x, print);
    std::thread t1(&ZeroEvenOdd::odd, &x, print);
    std::thread t2(&ZeroEvenOdd::even, &x, print);
    t0.join();
    t1.join();
    t2.join();
    printf("\n");
}

int main() {
    for(int n = 2; n < 10; n++) {
        test(n);
    }
}
