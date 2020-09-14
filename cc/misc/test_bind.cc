/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <boost/function.hpp>
#include <boost/bind.hpp>
#include <queue>
#include <string>
#include <iostream>

class Executor {
    typedef boost::function<void(Executor*, int)> Callable;
    typedef std::queue<Callable> Q;
public:
    void push(Callable c) {
        q_.push(c);
    }
    void run() {
        while(!q_.empty()) {
            Callable c = q_.front();
            q_.pop();
            c(this, 1);
        }
    }
private:
    Q q_;
}; // class Executor

class A {
public:
    void fun(Executor* x, std::string s, int) {
        std::cout << "executor=" << x << ", s=" << s << std::endl;
    }
}; // class A

class B {
public:
    void fun(Executor* x, int s, int) {
        std::cout << "executor=" << x << ", s=" << s << std::endl;
    }
}; // class B

int main() {
    Executor x;
    A a;
    B b;
    x.push(boost::bind(&A::fun, &a, _1, "hello", _2));
    x.push(boost::bind(&A::fun, &a, _1, "world", _2));
    x.push(boost::bind(&B::fun, &b, _1, 123, _2));
    x.push(boost::bind(&B::fun, &b, _1, 456, _2));
    x.run();
    return 0;
}
