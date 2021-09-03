/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <memory>
#include <vector>
#include <functional>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

// float
// 1bit(A) + 8bit(B) + 23bit(C)
// 6bit(B) + 11bit(C) + 1bit(A) = 18bit < 256K

inline uint32_t zigzag(uint32_t value) {
    return (value << 1) ^ (value >> 31);
}

uint32_t float_to_int(float f) {
    union {
        struct{
            uint32_t fact: 23;
            uint32_t exp: 8;
            uint32_t sign: 1;
        };
        float f;
    } u;
    u.f = f;
    // cout << "s = " << u.sign << ", exp = " << u.exp << ", fact = " << u.fact << endl;

    static const int lsb = 12;
    static const int lsb_mask = (1 << lsb) - 1;
    static const int exp_base = (1 << 7) - 1;
    uint32_t exp = zigzag(u.exp - exp_base);
    if (exp < 64 && (u.fact & lsb_mask) == 0) {
        return (exp << (23 - lsb + 1)) | ((u.fact >> lsb) << 1) | u.sign;
    }
    return (uint32_t)(-1);
}


// double
// 1bit(A) + 11bit(B) + 52bit(C)
// 6bit(B) + 11bit(C) + 1bit(A) = 18bit < 256K

uint32_t double_to_int(double f) {
    union {
        struct{
            uint64_t fact: 52;
            uint32_t exp: 11;
            uint32_t sign: 1;
        };
        double f;
    } u;
    u.f = f;
    // cout << "s = " << u.sign << ", exp = " << u.exp << ", fact = " << u.fact << endl;
    static const int lsb = 41;
    static const uint64_t lsb_mask = (1ULL << lsb) - 1;
    static const int exp_base = (1 << 10) - 1;
    uint32_t exp = zigzag(u.exp - exp_base);
    if (exp < 64 && (u.fact & lsb_mask) == 0) {
        return (exp << (52 - lsb + 1)) | ((u.fact >> lsb) << 1) | u.sign;
    }
    return (uint32_t)(-1);
}

int main() {
    std::vector<float> fs = {1.125, 1.25, 0.25, 0.2, 0.32};
    uint32_t failed = (uint32_t)(-1);

    for(float f: fs) {
        uint32_t v = float_to_int(f);
        if (v == failed) continue;
        cout << f << " => " << v << endl;
    }
    return 0;
}
