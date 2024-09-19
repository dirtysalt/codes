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

class Foo {
public:
    mutex m;
    condition_variable cv;
    int stage;
    Foo() {
        stage = 1;
    }

    void run(function<void()> f, int wait) {
        unique_lock<mutex> lk(m);
        while(stage != wait) {
            cv.wait(lk);
        }
        f();
        stage = wait + 1;
        cv.notify_all();
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        run(printFirst, 1);
    }

    void second(function<void()> printSecond) {
        run(printSecond, 2);
    }

    void third(function<void()> printThird) {
        run(printThird, 3);
    }
};

int main() {
    return 0;
}
