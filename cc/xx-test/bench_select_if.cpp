/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <benchmark/benchmark.h>

#include <cstdint>
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

void opt_select_if2(int* a, int* b, int* c, int* out, size_t size) {
    for (size_t i = 0; i < size; i++) {
        out[i] = (a[i] >= b[i]) ? c[i] : 0;
    }
}

static void run_select_if(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<int> a, b, c, out;
    size_t size = state.range(0);
    size_t range = state.range(1);

    ConstructRandomSet(size, range, a);
    ConstructRandomSet(size, range, b);
    ConstructRandomSet(size, range, c);
    out.resize(size);

    for (auto _ : state) {
        select_if(a.data(), b.data(), c.data(), out.data(), size);
    }
}

static void run_opt_select_if(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<int> a, b, c, out;
    size_t size = state.range(0);
    size_t range = state.range(1);

    ConstructRandomSet(size, range, a);
    ConstructRandomSet(size, range, b);
    ConstructRandomSet(size, range, c);
    out.resize(size);

    for (auto _ : state) {
        opt_select_if(a.data(), b.data(), c.data(), out.data(), size);
    }
}

static void run_opt_select_if2(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<int> a, b, c, out;
    size_t size = state.range(0);
    size_t range = state.range(1);

    ConstructRandomSet(size, range, a);
    ConstructRandomSet(size, range, b);
    ConstructRandomSet(size, range, c);
    out.resize(size);

    for (auto _ : state) {
        opt_select_if2(a.data(), b.data(), c.data(), out.data(), size);
    }
}

static const int N = 1000000;
static const int RANGE = std::numeric_limits<int>::max();

BENCHMARK(run_select_if)->Args({N, RANGE});
BENCHMARK(run_opt_select_if)->Args({N, RANGE});
BENCHMARK(run_opt_select_if2)->Args({N, RANGE});
