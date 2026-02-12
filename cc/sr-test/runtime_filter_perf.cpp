#include <benchmark/benchmark.h>

#include <iostream>
#include <random>
#include <sstream>

#include "binaryfusefilter.h"
#include "simdblockfilter.h"
#include "starrocks_deps.h"
// #include "xorfilter.h"

class BinaryFuse {
public:
    explicit BinaryFuse(const size_t size) {
        if (!binary_fuse8_allocate(size, &filter)) {
            throw ::std::runtime_error("Allocation failed.");
        }
    }
    ~BinaryFuse() { binary_fuse8_free(&filter); }

    bool AddAll(const uint64_t* data, const size_t start, const size_t end) {
        return binary_fuse8_populate(data + start, end - start, &filter);
    }
    bool insert_hash(const uint64_t data) {
        // if (test_hash(data)) return false;
        return AddAll(&data, 0, 1);
    }
    inline bool Contains(const uint64_t& item) const { return binary_fuse8_contain(item, &filter); }
    inline bool test_hash(const uint64_t& item) const { return binary_fuse8_contain(item, &filter); }
    inline size_t SizeInBytes() const { return binary_fuse8_size_in_bytes(&filter); }
    BinaryFuse(BinaryFuse&& o) : filter(o.filter) {
        o.filter.Fingerprints = nullptr; // we take ownership for the data
    }
    binary_fuse8_t filter;

private:
    BinaryFuse(const BinaryFuse& o) = delete;
};

static int constexpr BATCH_SIZE = 4096;
static int MOD = 3;
struct Logger {
    std::string ss;
    ~Logger() { std::cerr << ss << "\n"; }
};
Logger logger;

#define CHECK()                                                                                               \
    do {                                                                                                      \
        int true_pos = 0, false_pos = 0, true_neg = 0, false_neg = 0;                                         \
        for (size_t i = 0; i < size * MOD; i++) {                                                             \
            if (i % MOD == 0) {                                                                               \
                if (sel[i])                                                                                   \
                    true_pos += 1;                                                                            \
                else                                                                                          \
                    false_pos += 1;                                                                           \
            } else {                                                                                          \
                if (sel[i])                                                                                   \
                    false_neg += 1;                                                                           \
                else                                                                                          \
                    true_neg += 1;                                                                            \
            }                                                                                                 \
        }                                                                                                     \
        char buf[256];                                                                                        \
        snprintf(buf, sizeof(buf), "%s/%d: tp=%d, tn=%d, fn=%d, fp=%d\n", __func__, size, true_pos, true_neg, \
                 false_neg, false_pos);                                                                       \
        logger.ss += buf;                                                                                     \
    } while (0)

static void test_simdblock_filter_normal(benchmark::State& state) {
    size_t size = state.range(0);
    SimdBlockFilter filter;
    filter.init(size);
    for (size_t i = 0; i < size * MOD; i++) {
        if (i % MOD == 0) {
            filter.insert_hash(starrocks::vectorized::StdHash<size_t>()(i));
        }
    }
    std::vector<uint8_t> selection((size * MOD + BATCH_SIZE));
    uint8_t* sel = selection.data();
    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        for (size_t i = 0; i < size * MOD; i += BATCH_SIZE) {
            for (size_t j = 0; j < BATCH_SIZE; j++) {
                int idx = i + j;
                uint64_t hash = starrocks::vectorized::StdHash<size_t>()(idx);
                sel[idx] = filter.test_hash(hash);
            }
        }
    }
    CHECK();
}

static void test_simdblock_filter_prefetch(benchmark::State& state) {
    size_t size = state.range(0);
    SimdBlockFilter filter;
    filter.init(size);
    for (size_t i = 0; i < size * MOD; i++) {
        if (i % MOD == 0) {
            filter.insert_hash(starrocks::vectorized::StdHash<size_t>()(i));
        }
    }
    std::vector<uint8_t> selection((size * MOD + BATCH_SIZE));
    std::vector<uint64_t> hash_values(BATCH_SIZE);
    uint8_t* sel = selection.data();
    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        for (size_t i = 0; i < size * MOD; i += BATCH_SIZE) {
            for (size_t j = 0; j < BATCH_SIZE; j++) {
                size_t idx = i + j;
                uint64_t hash = starrocks::vectorized::StdHash<size_t>()(idx);
                hash_values[j] = hash;
            }
            static int constexpr STEP = 4;
            for (size_t j = 0; j < BATCH_SIZE; j++) {
                // NOTE(yan): has multiple CPU instructions.
                /*
                  2.32 │    │  mov    (%r12,%rax,8),%rdx                                                                                                                                                                                                                                                                                                                          ▒
                  0.73 │    │  and    %r14,%rdx                                                                                                                                                                                                                                                                                                                                   ▒
                  1.13 │    │  shl    $0x5,%rdx
                  2.64 │    │  prefetchnta (%r15,%rdx,1)
                */
                if ((j + STEP) < BATCH_SIZE) {
                    filter.prefetch_hash(hash_values[j + STEP]);
                }
                size_t idx = i + j;
                uint64_t hash = hash_values[j];
                sel[idx] = filter.test_hash(hash);
            }
        }
    }
    CHECK();
}

static void test_binaryfuse_filter_normal(benchmark::State& state) {
    size_t size = state.range(0);
    BinaryFuse filter(size);
    for (size_t i = 0; i < size * MOD; i++) {
        if (i % MOD == 0) {
            // NOTE(yan): extremely slow.
            filter.insert_hash(starrocks::vectorized::StdHash<size_t>()(i));
        }
    }
    std::vector<uint8_t> selection((size * MOD + BATCH_SIZE));
    uint8_t* sel = selection.data();
    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        for (size_t i = 0; i < size * MOD; i += BATCH_SIZE) {
            for (size_t j = 0; j < BATCH_SIZE; j++) {
                int idx = i + j;
                uint64_t hash = starrocks::vectorized::StdHash<size_t>()(idx);
                sel[idx] = filter.test_hash(hash);
            }
        }
    }
    CHECK();
}

static constexpr size_t N = 10'000;      // 10K
static constexpr size_t N2 = 10'000'000; // 10M
BENCHMARK(test_simdblock_filter_normal)->RangeMultiplier(10)->Range(N, N2);
// BENCHMARK(test_simdblock_filter_prefetch)->RangeMultiplier(10)->Range(N, N2);
// BENCHMARK(test_binaryfuse_filter_normal)->RangeMultiplier(10)->Range(N, N2);
