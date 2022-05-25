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

void f_codegen(int32_t* a, int32_t* b, int32_t* c, int32_t* d, int n) {
    for (int i = 0; i < n; i++) {
        d[i] = 3 * a[i] + 4 * b[i] + 5 * c[i];
    }
}

void f_simd_fusion(int32_t* a, int32_t* b, int32_t* c, int32_t* d, int n) {
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

#define RE __restrict__

void f_add(int32_t* RE a, int32_t* RE b, int32_t* RE c, int n) {
    int i = 0;
    for (i = 0; (i + 16) < n; i += 16) {
        __m512i x = _mm512_loadu_epi32(a + i);
        __m512i y = _mm512_loadu_epi32(b + i);
        x = _mm512_add_epi32(x, y);
        _mm512_storeu_epi32(c + i, x);
    }

    while (i < n) {
        c[i] = a[i] + b[i];
        i += 1;
    }
}

void f_mul(int32_t* RE a, int32_t b, int32_t* RE c, int n) {
    int i = 0;
    __m512i c0 = _mm512_set1_epi32(b);
    for (i = 0; (i + 16) < n; i += 16) {
        __m512i x = _mm512_loadu_epi32(a + i);
        x = _mm512_mul_epi32(x, c0);
        _mm512_storeu_epi32(c + i, x);
    }

    while (i < n) {
        c[i] = a[i] * b;
        i += 1;
    }
}

void f_simd_compose(int32_t* a, int32_t* b, int32_t* c, int32_t* d, int n) {
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

static void simd_fusion(benchmark::State& state) {
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
        f_simd_fusion(a.data(), b.data(), c.data(), d.data(), n);
    }
}

static void simd_compose(benchmark::State& state) {
    size_t n = state.range(0);
    auto a = ConstructRandomSet(n, 10);
    auto b = ConstructRandomSet(n, 20);
    auto c = ConstructRandomSet(n, 30);
    std::vector<int32_t> d(n);

    // Code inside this loop is measured repeatedly
    for (auto _ : state) {
        state.PauseTiming();
        d.assign(n, 0);
        std::vector<int32_t> t0(n), t1(n), t2(n), t3(n), t4(n);
        state.ResumeTiming();
        f_mul(a.data(), 3, t0.data(), n);
        f_mul(b.data(), 4, t1.data(), n);
        f_mul(c.data(), 5, t2.data(), n);
        f_add(t0.data(), t1.data(), t3.data(), n);
        f_add(t2.data(), t3.data(), d.data(), n);
    }
}

// Register the function as a benchmark
static const int N0 = 4096;
static const int N1 = 40960;
static const int N2 = 409600;

BENCHMARK(codegen)->Arg(N0)->Arg(N1)->Arg(N2);
BENCHMARK(simd_fusion)->Arg(N0)->Arg(N1)->Arg(N2);
BENCHMARK(simd_compose)->Arg(N0)->Arg(N1)->Arg(N2);