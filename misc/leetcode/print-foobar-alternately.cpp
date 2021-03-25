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

class FooBar {
private:
    int n;
    mutex m;
    condition_variable cv;
    int stage;

public:
    FooBar(int n) {
        this->n = n;
        stage = 0;
    }

    void foo(function<void()> printFoo) {

        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lk(m);
            while(stage != 0) {
                cv.wait(lk);
            }
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            stage = 1;
            cv.notify_one();
        }
    }

    void bar(function<void()> printBar) {

        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lk(m);
            while(stage != 1) {
                cv.wait(lk);
            }
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            stage = 0;
            cv.notify_one();
        }
    }
};

int main() {
    return 0;
}
