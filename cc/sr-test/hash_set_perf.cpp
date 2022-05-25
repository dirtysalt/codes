#include <benchmark/benchmark.h>
#include <emmintrin.h>
#include <immintrin.h>

#include <cmath>
#include <cstdlib>
#include <functional>
#include <iostream>

//#define PHMAP_LINEAR_PROBE
#include "Common/HashTable/HashSet.h"
#include "column/column_hash.h"
#include "column/hash_set.h"
#include "ska_flat_hash_map.hpp"
#include "util/phmap/phmap.h"

using namespace std;
using namespace starrocks::vectorized;
static constexpr size_t BLOCK = 4096;

void ConstructRandomSet(size_t size, size_t range, std::vector<int>& rs) {
    rs.resize(size);
    std::srand(42);
    for (size_t i = 0; i < size; i++) {
        rs[i] = std::rand() % range;
    }
}

class LogBuffer {
public:
    std::ostringstream& buf() { return oss; }
    ~LogBuffer() { std::cerr << oss.str(); }

private:
    std::ostringstream oss;
};

LogBuffer _log_buffer;

#define HSINFO(name)                                                                                         \
    _log_buffer.buf() << name << ": hash set size = " << hs.size() << ", load factor = " << hs.load_factor() \
                      << std::endl

static void run_insert_random(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<int> a;
    ConstructRandomSet(state.range(0), state.range(1), a);
    for (auto _ : state) {
        HashSet<int> hs;
        // state.PauseTiming();
        // state.ResumeTiming();
        for (size_t i = 0; i < a.size(); i++) {
            hs.insert(a[i]);
        }
        HSINFO(__func__);
    }
}

static void run_insert_random_ska(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<int> a;
    ConstructRandomSet(state.range(0), state.range(1), a);

    for (auto _ : state) {
        ska::flat_hash_set<int, StdHash<int>> hs;
        // state.PauseTiming();
        // state.ResumeTiming();
        for (size_t i = 0; i < a.size(); i++) {
            hs.insert(a[i]);
        }
        HSINFO(__func__);
    }
}

static void run_insert_sorted(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<int> a;
    ConstructRandomSet(state.range(0), state.range(1), a);
    std::sort(a.begin(), a.end());

    for (auto _ : state) {
        HashSet<int> hs;
        for (size_t i = 0; i < a.size(); i++) {
            hs.insert(a[i]);
        }
        HSINFO(__func__);
    }
}

static void run_insert_precompute(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<int> a;
    ConstructRandomSet(state.range(0), state.range(1), a);

    static constexpr size_t PREFETCH = 16;
    std::vector<size_t> hash_values(BLOCK);

    for (auto _ : state) {
        HashSet<int> hs;
        const auto* data = a.data();
        const size_t size = a.size();

        for (size_t i = 0; i < size; i += BLOCK) {
            for (size_t j = 0; j < BLOCK; j++) {
                size_t hashval = hs.hash_function()(data[i + j]);
                hash_values[j] = hashval;
            }

            for (size_t j = 0, k = PREFETCH; j < BLOCK; j++, k++) {
                if (k < BLOCK) {
                    hs.prefetch_hash(hash_values[k]);
                }
                hs.emplace_with_hash(hash_values[j], data[i + j]);
            }
        }
        HSINFO(__func__);
    }
}

static void run_insert_random_ck(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<int> a;
    ConstructRandomSet(state.range(0), state.range(1), a);
    size_t set_size = 0;

    for (auto _ : state) {
        CK::HashSet<int> hs;
        // state.PauseTiming();
        // state.ResumeTiming();
        for (size_t i = 0; i < a.size(); i++) {
            hs.insert(a[i]);
        }
        HSINFO(__func__);
    }
}

static const int FACTOR = 16;
static const int N = 4096000 * FACTOR;
static const int M0 = 60 * FACTOR;
static const int M1 = 6000 * FACTOR;
static const int M2 = 600000 * FACTOR;
static const int M3 = 60000000 * FACTOR;

static_assert(N % BLOCK == 0);

BENCHMARK(run_insert_random)->Args({N, M0});
BENCHMARK(run_insert_random_ska)->Args({N, M0});
BENCHMARK(run_insert_precompute)->Args({N, M0});
BENCHMARK(run_insert_random_ck)->Args({N, M0});

BENCHMARK(run_insert_random)->Args({N, M1});
BENCHMARK(run_insert_random_ska)->Args({N, M1});
BENCHMARK(run_insert_precompute)->Args({N, M1});
BENCHMARK(run_insert_random_ck)->Args({N, M1});

BENCHMARK(run_insert_random)->Args({N, M2});
BENCHMARK(run_insert_random_ska)->Args({N, M2});
BENCHMARK(run_insert_precompute)->Args({N, M2});
BENCHMARK(run_insert_random_ck)->Args({N, M2});

BENCHMARK(run_insert_random)->Args({N, M3});
BENCHMARK(run_insert_random_ska)->Args({N, M3});
BENCHMARK(run_insert_precompute)->Args({N, M3});
BENCHMARK(run_insert_random_ck)->Args({N, M3});