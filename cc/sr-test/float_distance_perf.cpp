#include <benchmark/benchmark.h>
#include <emmintrin.h>
#include <immintrin.h>

#include <cstdio>

void ConstructRandomSet(size_t size, std::vector<float>& rs, std::vector<float>& rs2) {
    rs.resize(size);
    rs2.resize(size);
    for (size_t i = 0; i < size; i++) {
        rs[i] = 1.0 / (i % 10);
        rs2[i] = 2.0 / (i % 7);
    }
}

static void test_float_distance(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<float> a, b;
    ConstructRandomSet(state.range(0), a, b);

    for (auto _ : state) {
        float c = 0, d = 0, e = 0;
        for (size_t i = 0; i < a.size(); i++) {
            c += a[i] * b[i];
            d += a[i] * a[i];
            e += b[i] * b[i];
        }
        benchmark::DoNotOptimize(c);
        benchmark::DoNotOptimize(d);
        benchmark::DoNotOptimize(e);
    }
}

static constexpr size_t N = 487;
BENCHMARK(test_float_distance)->Args({N});
