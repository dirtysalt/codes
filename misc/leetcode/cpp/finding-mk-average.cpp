/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <memory>
#include <vector>
#include <functional>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;
typedef pair<int,int> PII;
typedef long long LL;

class MKAverage {
    set<PII> left;
    set<PII> middle;
    set<PII> right;
    LL midsum;
    int* buf;
    int cnt;
    int m;
    int k;
    int off;
    int midsize;
public:
    MKAverage(int m, int k): m(m), k(k) {
        midsum = 0;
        cnt = 0;
        buf = new int[m];
        off = 0;
        midsize = m - 2 * k;
    }

    void popElement(int x, int index) {
        cnt -= 1;
        auto p = PII(x, index);
        auto it = left.find(p);
        if (it != left.end()) {
            left.erase(it);
            return;
        }
        it = middle.find(p);
        if (it != middle.end()) {
            midsum -= it->first;
            middle.erase(it);
            return;
        }
        it = right.find(p);
        if (it != right.end()) {
            right.erase(it);
            return;
        }
        assert(0 == 1);
        return;
    }

    void pushElement(int x, int index) {
        left.insert(PII(x, index));
        cnt += 1;
    }

    void balance() {
        while (left.size() > k) {
            auto it = left.rbegin();
            midsum += it->first;
            middle.insert(*it);
            left.erase(*it);
        }
        if (left.rbegin()->first > middle.begin()->first) {
            // swap
            auto a = *left.rbegin();
            auto b = *middle.begin();
            middle.insert(a);
            left.insert(b);
            middle.erase(b);
            left.erase(a);
            midsum += a.first - b.first;
        }
        while (middle.size() > midsize) {
            auto it = middle.rbegin();
            right.insert(*it);
            midsum -= it->first;
            middle.erase(*it);
        }
        if (middle.rbegin()->first > right.begin()->first) {
            // swap
            auto a = *right.begin();
            auto b = *middle.rbegin();
            middle.insert(a);
            right.insert(b);
            middle.erase(b);
            right.erase(a);
            midsum += a.first - b.first;
        }
    }

    void addElement(int num) {
        if(cnt == m) {
            popElement(buf[off], off);
        }
        buf[off] = num;
        pushElement(num, off);
        off = (off + 1) % m;
        if (cnt == m) {
            balance();
        }
    }

    int calculateMKAverage() {
        if (cnt == m) {
            debug();
            return midsum / midsize;
        }
        return -1;
    }


    void debug() {
        int a = left.rbegin() -> first;
        int b = middle.rbegin() -> first;
        int c = right.rbegin() -> first;
        cout << "left size = " << left.size() << ", middle size = " << middle.size() << ", right size = " << right.size() << endl;
        cout << "left = " << a << ", middle = " << b << ", right = " << c << endl;
        assert((b >= a) && (b <= c));
        LL d = 0;
        for(auto p: middle) {
            d += p.first;
        }
        cout << midsum << " " << d << endl;
        assert(d == midsum);
    }


    ~MKAverage() {
        delete[] buf;
    }
};

#ifdef MAIN
/**
 * Your MKAverage object will be instantiated and called as such:
 * MKAverage* obj = new MKAverage(m, k);
 * obj->addElement(num);
 * int param_2 = obj->calculateMKAverage();
 */

int main() {
    // MKAverage* obj = new MKAverage(3, 1);
    // obj->addElement(3);
    // obj->addElement(1);
    // cout << obj->calculateMKAverage() << endl;
    // obj->addElement(10);
    // cout << obj->calculateMKAverage() << endl;
    // obj->addElement(5);
    // obj->addElement(5);
    // obj->addElement(5);
    // cout << obj->calculateMKAverage() << endl;

    MKAverage* obj = new MKAverage(3, 1);
    obj->addElement(176);
    obj->addElement(746);
    cout << obj->calculateMKAverage() << endl;
    obj->addElement(82);
    obj->addElement(334);
    cout << obj->calculateMKAverage() << endl;
    obj->addElement(154);
    obj->addElement(649);
    obj->debug();
    cout << obj->calculateMKAverage() << endl;
    return 0;
}
#endif
