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

#define waitStage(oldValue,newValue)            \
        unique_lock<mutex> lk(m);               \
        while(stage != oldValue) {              \
            cv.wait(lk);                        \
        }                                       \
        stage = newValue;


class FizzBuzz {
private:
    int n;
    int stage;
    mutex m;
    condition_variable cv;
public:
    FizzBuzz(int n) {
        this->n = n;
        stage = 1;
    }

    // printFizz() outputs "fizz".
    void fizz(function<void()> printFizz) {
        for(int wait = 3;; wait += 3) {
            if (wait > n) break;
            if (wait % 5 == 0) continue;
            waitStage(wait, wait + 1);
            printFizz();
            cv.notify_all();
        }
        //        printf("fizz ok\n");
    }

    // printBuzz() outputs "buzz".
    void buzz(function<void()> printBuzz) {
        for(int wait = 5;; wait += 5) {
            if (wait > n) break;
            if (wait % 3 == 0) continue;
            waitStage(wait, wait + 1);
            printBuzz();
            cv.notify_all();
        }
        //        printf("buzz ok\n");
    }

    // printFizzBuzz() outputs "fizzbuzz".
	void fizzbuzz(function<void()> printFizzBuzz) {
        for(int wait = 15;; wait += 15) {
            if (wait > n) break;
            waitStage(wait, wait + 1);
            printFizzBuzz();
            cv.notify_all();
        }
        //printf("fizzbuzz ok\n");
    }

    // printNumber(x) outputs "x", where x is an integer.
    void number(function<void(int)> printNumber) {
        for(int wait=1; wait<= n;wait += 1) {
            if(wait % 3 == 0 || wait % 5 == 0) continue;
            waitStage(wait, wait + 1);
            printNumber(wait);
            cv.notify_all();
        }
        //        printf("number ok\n");
    }
};


void test(int n) {
    printf("n = %d -> \n", n);
    auto x = FizzBuzz(n);
    std::thread t0(&FizzBuzz::fizz, &x, []() {printf("fizz \n");});
    std::thread t1(&FizzBuzz::buzz, &x, []() { printf("buzz \n"); });
    std::thread t2(&FizzBuzz::fizzbuzz, &x, []() {printf("fizzbuzz \n");});
    std::thread t3(&FizzBuzz::number, &x, [](int x) {printf("%d \n", x);});
    t0.join();
    t1.join();
    t2.join();
    t3.join();
    printf("\n");
}


int main() {
    for(int n = 2; n < 20; n++) {
        test(n);
    }
    return 0;
}
