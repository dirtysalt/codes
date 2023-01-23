/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <benchmark/benchmark.h>
#include <immintrin.h>

#include <cmath>
using namespace std;

static const int N = (100000) / 8 * 8;

std::vector<float> ConstructRandomSet(int64_t size) {
    std::vector<float> a;
    a.reserve(size);
    for (size_t i = 0; i < size; ++i) {
        a.emplace_back(i * 0.2f + 0.5f);
    }
    return a;
}

static inline __attribute__((always_inline)) float Q_rsqrt(float number) {
    long i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = number * 0.5F;
    y = number;
    i = *(long*)&y;            // evil floating point bit level hacking
    i = 0x5f3759df - (i >> 1); // what the fuck?
    y = *(float*)&i;
    y = y * (threehalfs - (x2 * y * y)); // 1st iteration
    //    y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

    return y;
}

void Q_rsqrt_simd(float* number, float* output, size_t n) {
    assert(n % 8 == 0);
    // 32 * 8 = 256 bits.
    size_t loop = n / 8;

    static const int MAG = 0x5f3759df;
    static const float THREEHALFS = 1.5f;
    static const float HALF = 0.5f;
    __m256i mag = _mm256_set_epi32(MAG, MAG, MAG, MAG, MAG, MAG, MAG, MAG);
    __m256 threehalfs = _mm256_set_ps(THREEHALFS, THREEHALFS, THREEHALFS, THREEHALFS, THREEHALFS, THREEHALFS,
                                      THREEHALFS, THREEHALFS);
    __m256 half = _mm256_set_ps(HALF, HALF, HALF, HALF, HALF, HALF, HALF, HALF);
    __m128i srl = _mm_set_epi64x(0x0, 0x1);

    for (size_t i = 0; i < loop; i++) {
        // x2 = number * 0.5f
        // output = t0
        __m256 t0 = _mm256_loadu_ps(number);
        t0 = _mm256_mul_ps(t0, half);

        // i  = * ( long * ) &y;
        // i  = 0x5f3759df - ( i >> 1 );
        // y  = * ( float * ) &i;
        // output = t1
        __m256i t1 = _mm256_loadu_si256((__m256i const*)number);
        t1 = _mm256_srl_epi32(t1, srl);
        t1 = _mm256_sub_epi32(mag, t1);
        __m256 t2 = _mm256_castsi256_ps(t1);

        // y  = y * ( threehalfs - ( x2 * y * y ) );
        // output = t2
        __m256 t3 = _mm256_mul_ps(t2, t2);
        t3 = _mm256_mul_ps(t0, t3);
        t3 = _mm256_sub_ps(threehalfs, t3);
        t3 = _mm256_mul_ps(t2, t3);

        _mm256_storeu_ps(output, t3);
        number += 8;
        output += 8;
    }
    return;
}

void rsqrt_simd(float* number, float* output, size_t n) {
    assert(n % 8 == 0);
    // 32 * 8 = 256 bits.
    size_t loop = n / 8;
    for (size_t i = 0; i < loop; i++) {
        __m256 a = _mm256_loadu_ps(number);
        __m256 b = _mm256_rsqrt_ps(a);
        _mm256_storeu_ps(output, b);
        number += 8;
        output += 8;
    }
    return;
}

static void run_std_rsqrt(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<float> a;
    std::vector<float> b;
    for (auto _ : state) {
        state.PauseTiming();
        a = ConstructRandomSet(state.range(0));
        b = ConstructRandomSet(state.range(0));
        float* p0 = a.data();
        float* p1 = b.data();
        state.ResumeTiming();
        for (size_t i = 0; i < state.range(0); ++i) {
            p1[i] = 1.0f / std::sqrt(p0[i]);
        }
    }
}
// Register the function as a benchmark
BENCHMARK(run_std_rsqrt)->Arg(N);

static void run_rsqrt_simd(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<float> a;
    std::vector<float> b;
    for (auto _ : state) {
        state.PauseTiming();
        a = ConstructRandomSet(state.range(0));
        b = ConstructRandomSet(state.range(0));
        float* p0 = a.data();
        float* p1 = b.data();
        state.ResumeTiming();
        rsqrt_simd(p0, p1, state.range(0));
    }
}

// Register the function as a benchmark
BENCHMARK(run_rsqrt_simd)->Arg(N);

static void run_Q_rsqrt(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<float> a;
    std::vector<float> b;
    for (auto _ : state) {
        state.PauseTiming();
        a = ConstructRandomSet(state.range(0));
        b = ConstructRandomSet(state.range(0));
        float* p0 = a.data();
        float* p1 = b.data();
        state.ResumeTiming();
        for (size_t i = 0; i < state.range(0); ++i) {
            p1[i] = Q_rsqrt(p0[i]);
        }
    }
}

// Register the function as a benchmark
BENCHMARK(run_Q_rsqrt)->Arg(N);

static void run_Q_rsqrt_simd(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<float> a;
    std::vector<float> b;
    for (auto _ : state) {
        state.PauseTiming();
        a = ConstructRandomSet(state.range(0));
        b = ConstructRandomSet(state.range(0));
        float* p0 = a.data();
        float* p1 = b.data();
        state.ResumeTiming();
        Q_rsqrt_simd(p0, p1, state.range(0));
    }
}

// Register the function as a benchmark
BENCHMARK(run_Q_rsqrt_simd)->Arg(N);

#ifdef TEST
int main() {
    const int n = 32;
    std::vector<float> input;
    std::vector<float> output;
    input.resize(n);
    output.resize(n);
    for (size_t i = 0; i < n; i++) {
        input[i] = (i * 0.3f + 0.5f);
    }
    Q_rsqrt_simd(input.data(), output.data(), n);
    for (size_t i = 0; i < n; i++) {
        std::cout << input[i] << ", std = " << 1.0f / sqrt(input[i]) << ", my = " << output[i] << std::endl;
    }
}
#endif
