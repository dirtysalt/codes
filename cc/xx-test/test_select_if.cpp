/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <benchmark/benchmark.h>
#include <emmintrin.h>
#include <immintrin.h>

#include <cstdint>
#include <iostream>
using namespace std;

// out[i] = (a[i] >= b[i] ? c[i] : 0)

void ConstructRandomSet(size_t size, size_t range, std::vector<int>& rs) {
    rs.resize(size);
    std::srand(42);
    for (size_t i = 0; i < size; i++) {
        rs[i] = std::rand() % range;
    }
}

void select_if(int* a, int* b, int* c, int* out, size_t size) {
    for (size_t i = 0; i < size; i++) {
        if (a[i] >= b[i]) {
            out[i] = c[i];
        } else {
            out[i] = 0;
        }
    }
}

void opt_select_if(int* a, int* b, int* c, int* out, size_t size) {
    for (size_t i = 0; i < size; i++) {
        uint8_t diff = (a[i] >= b[i]);
        out[i] = (~diff + 1) & c[i];
    }
}

int main() {
    std::vector<int> a, b, c, out0, out1;
    size_t n = 100000;
    size_t range = std::numeric_limits<int>::max();
    ConstructRandomSet(n, range, a);
    ConstructRandomSet(n, range, b);
    ConstructRandomSet(n, range, c);
    out0.resize(n);
    out1.resize(n);

    std::cout << "Comparing Result...\n";
    select_if(a.data(), b.data(), c.data(), out0.data(), n);
    opt_select_if(a.data(), b.data(), c.data(), out1.data(), n);
    for (size_t i = 0; i < n; i++) {
        if (out0[i] != out1[i]) {
            std::cout << "Diff: a=" << a[i] << ", b=" << b[i] << ", c=" << c[i] << "\n";
            break;
        }
    }
    std::cout << "Succeed\n";
    return 0;
}