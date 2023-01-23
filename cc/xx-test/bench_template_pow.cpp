/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <benchmark/benchmark.h>
#include <immintrin.h>

#include <cstdint>
#include <ctime>
#include <random>
using namespace std;

template <size_t N>
struct Pow {
    double operator()(double x) const { return x * Pow<N - 1>()(x); }
};
template <>
struct Pow<1> {
    double operator()(double x) const { return x; }
};

double rt_pow(double x, size_t n) {
    double ans = 1;
    while (n) {
        if (n & 0x1) {
            ans = ans * x;
        }
        x = x * x;
        n = n >> 1;
    }
    return ans;
}

static void run_template_pow(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::srand(std::time(nullptr));
    double value = std::rand() * 1.0;
    size_t loops = state.range(0);
    for (auto _ : state) {
        for (size_t i = 0; i < loops; i++) {
            double res = Pow<10>()(value);
            benchmark::DoNotOptimize(res);
            // benchmark::ClobberMemory();
        }
    }
}

static void run_rt_pow(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::srand(std::time(nullptr));
    double value = std::rand() * 1.0;
    size_t loops = state.range(0);
    for (auto _ : state) {
        for (size_t i = 0; i < loops; i++) {
            double res = rt_pow(value, 10);
            benchmark::DoNotOptimize(res);
            // benchmark::ClobberMemory();
        }
    }
}

static void run_cmath(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::srand(std::time(nullptr));
    double value = std::rand() * 1.0;
    size_t loops = state.range(0);
    for (auto _ : state) {
        for (size_t i = 0; i < loops; i++) {
            double res = std::pow(value, 10);
            benchmark::DoNotOptimize(res);
            // benchmark::ClobberMemory();
        }
    }
}

static const size_t N = 1 << 20;
BENCHMARK(run_cmath)->Args({N});
BENCHMARK(run_template_pow)->Args({N});
BENCHMARK(run_rt_pow)->Args({N});
