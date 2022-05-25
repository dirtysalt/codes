#include <benchmark/benchmark.h>
#include <immintrin.h>

#include <random>

std::vector<int32_t> ConstructRandomSet(int64_t size, int32_t seed) {
    std::vector<int32_t> a;
    a.reserve(size);
    std::mt19937_64 rng;
    rng.seed(seed);
    for (size_t i = 0; i < size; ++i) {
        a.emplace_back(i);
    }
    return a;
}

static const int N = 1000000;

void f_codegen(int32_t* a, int32_t* b, int32_t* c, int32_t* d, int n) {
    for (int i = 0; i < n; i++) {
        d[i] = 3 * a[i] + 4 * b[i] + 5 * c[i];
    }
}

void f_simdfusion(int32_t* a, int32_t* b, int32_t* c, int32_t* d, int n) {
    __m512i c0 = _mm512_set1_epi32(3);
    __m512i c1 = _mm512_set1_epi32(4);
    __m512i c2 = _mm512_set1_epi32(5);

    int i = 0;
    for (i = 0; (i + 16) < n; i += 16) {
        __m512i x = _mm512_loadu_epi32(a + i);
        __m512i y = _mm512_loadu_epi32(b + i);
        __m512i z = _mm512_loadu_epi32(c + i);
        x = _mm512_mul_epi32(x, c0);
        y = _mm512_mul_epi32(y, c1);
        x = _mm512_add_epi32(x, y);
        z = _mm512_mul_epi32(z, c2);
        x = _mm512_add_epi32(x, z);
        _mm512_storeu_epi32(d + i, x);
    }

    while (i < n) {
        d[i] = 3 * a[i] + 4 * b[i] + 5 * c[i];
        i += 1;
    }
}

void f_add(int32_t* a, int32_t* b, int32_t* c, int n) {
    
}

static void codegen(benchmark::State& state) {
    size_t n = state.range(0);
    auto a = ConstructRandomSet(n, 10);
    auto b = ConstructRandomSet(n, 20);
    auto c = ConstructRandomSet(n, 30);
    std::vector<int32_t> d(n);

    // Code inside this loop is measured repeatedly
    for (auto _ : state) {
        state.PauseTiming();
        d.assign(n, 0);
        state.ResumeTiming();
        f_codegen(a.data(), b.data(), c.data(), d.data(), n);
    }
}

static void simdfusion(benchmark::State& state) {
    size_t n = state.range(0);
    auto a = ConstructRandomSet(n, 10);
    auto b = ConstructRandomSet(n, 20);
    auto c = ConstructRandomSet(n, 30);
    std::vector<int32_t> d(n);

    // Code inside this loop is measured repeatedly
    for (auto _ : state) {
        state.PauseTiming();
        d.assign(n, 0);
        state.ResumeTiming();
        f_simdfusion(a.data(), b.data(), c.data(), d.data(), n);
    }
}

// Register the function as a benchmark
BENCHMARK(codegen)->Arg(N);
BENCHMARK(simdfusion)->Arg(N);