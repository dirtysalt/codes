#include <benchmark/benchmark.h>
#include <immintrin.h>

void batch_update1(int* res, int col[], int size);
void batch_update2(int* res, int col[], int size);
void batch_update3(int* __restrict__ res, int* col, int size);
void batch_update4(int* res, int* col, int size);

static const int N = 4096000;

void initarray(int col[], int size) {
    for (int i = 0; i < size; ++i) {
        col[i] = i * 2 + 1;
    }
}

static void BatchUpdateVec(benchmark::State& state) {
    std::vector<int> arrayx(N);
    initarray(arrayx.data(), arrayx.size());
    int result_val = 0;
    for (auto _ : state) {
        batch_update1(&result_val, arrayx.data(), arrayx.size());
        benchmark::DoNotOptimize(result_val);
    }
}
// Register the function as a benchmark
BENCHMARK(BatchUpdateVec);

static void BatchUpdateNoVec(benchmark::State& state) {
    std::vector<int> arrayx(N);
    initarray(arrayx.data(), arrayx.size());
    int result_val = 0;
    for (auto _ : state) {
        batch_update2(&result_val, arrayx.data(), arrayx.size());
        benchmark::DoNotOptimize(result_val);
    }
}
BENCHMARK(BatchUpdateNoVec);

static void BatchUpdateRestrict(benchmark::State& state) {
    std::vector<int> arrayx(N);
    initarray(arrayx.data(), arrayx.size());
    int result_val = 0;
    for (auto _ : state) {
        batch_update3(&result_val, arrayx.data(), arrayx.size());
        benchmark::DoNotOptimize(result_val);
    }
}
BENCHMARK(BatchUpdateRestrict);

static void BatchUpdateSIMD(benchmark::State& state) {
    std::vector<int> arrayx(N);
    initarray(arrayx.data(), arrayx.size());
    int result_val = 0;
    for (auto _ : state) {
        batch_update4(&result_val, arrayx.data(), arrayx.size());
        benchmark::DoNotOptimize(result_val);
    }
}
BENCHMARK(BatchUpdateSIMD);

__attribute__((noinline)) void batch_update1(int* res, int col[], int size) {
    int tmp{};
    for (int i = 0; i < size; ++i) {
        tmp += col[i];
    }
    *res += tmp;
}

__attribute__((noinline)) void batch_update2(int* res, int col[], int size) {
    for (int i = 0; i < size; ++i) {
        *res += col[i];
    }
}

__attribute__((noinline)) void batch_update3(int* __restrict__ res, int* col, int size) {
    for (int i = 0; i < size; ++i) {
        *res += col[i];
    }
}

// __attribute__((noinline)) void batch_update4(int* res, int* col, int size) {
//     assert(size % 16 == 0);
//     int tmp[8] = {0, 0, 0, 0, 0, 0, 0, 0};
//     __m256i a = _mm256_loadu_si256((const __m256i_u*)tmp);
//     for (int i = 0; i < size; i += 16) {
//         __m256i b = _mm256_loadu_si256((const __m256i_u*)(col + i));
//         __m256i c = _mm256_loadu_si256((const __m256i_u*)(col + i + 8));
//         a = _mm256_add_epi32(a, b);
//         a = _mm256_add_epi32(a, c);
//     }
//     _mm256_storeu_si256((__m256i_u*)tmp, a);
//     for (int i = 0; i < 8; i++) {
//         *res += tmp[i];
//     }
// }

__attribute__((noinline)) void batch_update4(int* res, int* col, int size) {
    assert(size % 32 == 0);
    __m512i t0 = _mm512_setzero_epi32();
    __m512i t1 = _mm512_setzero_epi32();
    for (int i = 0; i < size; i += 32) {
        __m512i a = _mm512_loadu_epi32(col + i);
        __m512i b = _mm512_loadu_epi32(col + i + 16);
        t0 = _mm512_add_epi32(t0, a);
        t1 = _mm512_add_epi32(t1, b);
    }
    t0 = _mm512_add_epi32(t0, t1);
    *res = _mm512_reduce_add_epi32(t0);
}
