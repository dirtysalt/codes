
#include <benchmark/benchmark.h>
#include <emmintrin.h>
#include <immintrin.h>
#include <pmmintrin.h>

std::vector<uint8_t> ConstructRandomSet(int64_t size) {
    std::vector<uint8_t> a;
    a.reserve(size);
    for (size_t i = 0; i < size; ++i) {
        a.emplace_back(i);
    }
    return a;
}

inline uint8_t max(uint8_t a, uint8_t b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

static const int N = 100000000;

static void stdmax(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<uint8_t> a;
    std::vector<uint8_t> b;
    for (auto _ : state) {
        state.PauseTiming();
        a = ConstructRandomSet(state.range(0));
        b = ConstructRandomSet(state.range(0));
        state.ResumeTiming();
        for (size_t i = 0; i < state.range(0); ++i) {
            a[i] = std::max(a[i], b[i]);
        }
    }
}
// Register the function as a benchmark
BENCHMARK(stdmax)->Arg(N);

static void stdmaxptr(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<uint8_t> a;
    std::vector<uint8_t> b;
    for (auto _ : state) {
        state.PauseTiming();
        a = ConstructRandomSet(state.range(0));
        b = ConstructRandomSet(state.range(0));
        state.ResumeTiming();
        uint8_t* dst = a.data();
        uint8_t* src = b.data();
        for (size_t i = 0; i < state.range(0); ++i) {
            dst[i] = std::max(dst[i], src[i]);
        }
    }
}
BENCHMARK(stdmaxptr)->Arg(N);

static void ifmax(benchmark::State& state) {
    // Code before the loop is not measured
    std::vector<uint8_t> a;
    std::vector<uint8_t> b;
    for (auto _ : state) {
        state.PauseTiming();
        a = ConstructRandomSet(state.range(0));
        b = ConstructRandomSet(state.range(0));
        state.ResumeTiming();
        for (size_t i = 0; i < state.range(0); ++i) {
            a[i] = max(a[i], b[i]);
        }
    }
}
BENCHMARK(ifmax)->Arg(N);

static void simdmax(benchmark::State& state) {
    // Code before the loop is not measured
    std::vector<uint8_t> a;
    std::vector<uint8_t> b;
    for (auto _ : state) {
        state.PauseTiming();
        a = ConstructRandomSet(state.range(0));
        b = ConstructRandomSet(state.range(0));
        state.ResumeTiming();

        size_t size = state.range(0);
        uint8_t* dst = a.data();
        uint8_t* src = b.data();

        int _loop = size / 32;
        for (int i = 0; i < _loop; i++) {
            __m256i xa = _mm256_lddqu_si256((const __m256i*)dst);
            __m256i xb = _mm256_lddqu_si256((const __m256i*)src);
            src += 32;
            __m256i xc = _mm256_max_epu8(xa, xb);
            _mm256_storeu_si256((__m256i*)dst, xc);
            dst += 32;
        }

        int _rem = size % 32;
        for (int i = 0; i < _rem; i++) {
            dst[i] = std::max(dst[i], src[i]);
        }
    }
}
BENCHMARK(simdmax)->Arg(N);
