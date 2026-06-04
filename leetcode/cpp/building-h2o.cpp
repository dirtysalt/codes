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

class H2O {
public:
    mutex m;
    condition_variable cv;
    int h, o;
    H2O() {
        h = o = 0;
    }
    void checkReset() {
        if (h == 2 && o == 1) {
            h = o = 0;
        }
    }

    void hydrogen(function<void()> releaseHydrogen) {
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        unique_lock<mutex> lk(m);
        while(h >= 2) {
            cv.wait(lk);
        }
        releaseHydrogen();
        h += 1;
        checkReset();
        cv.notify_all();
    }

    void oxygen(function<void()> releaseOxygen) {
        unique_lock<mutex> lk(m);
        while(o >= 1) {
            cv.wait(lk);
        }
        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();
        o += 1;
        checkReset();
        cv.notify_all();
    }
};

int main() {

    return 0;
}
