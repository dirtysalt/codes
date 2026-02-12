#include <benchmark/benchmark.h>
#include <emmintrin.h>
#include <immintrin.h>

#include <cmath>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <random>

#include "phmap/phmap.h"

struct Column {
    struct Filter {
        const uint8_t* data() const { return _data.data(); }
        std::vector<uint8_t> _data;
    };
};

void make_random_filter_data(Column::Filter* filter, size_t size, int mode) {
    filter->_data.resize(size);
    std::mt19937_64 gen64;

    for (size_t i = 0; i < size; i++) {
        if (mode == 0) {
            filter->_data[i] = 0;
        } else {
            filter->_data[i] = (gen64() % (32 / mode)) == 0;
        }
    }
}

template <typename T, int mode>
static size_t filter_range(const Column::Filter& filter, T* data, size_t from, size_t to) {
    auto start_offset = from;
    auto result_offset = from;

#ifndef __AVX2__
#define __AVX2__
#endif

    const uint8_t* f_data = filter.data();
    constexpr size_t data_type_size = sizeof(T);

#ifdef __AVX2__

    constexpr size_t kBatchNums = 256 / (8 * sizeof(uint8_t));
    const __m256i all0 = _mm256_setzero_si256();

    // batch nums is kBatchNums
    // we will process filter at start_offset, start_offset + 1, ..., start_offset + kBatchNums - 1 in one batch
    while (start_offset + kBatchNums <= to) {
        __m256i f = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(f_data + start_offset));
        uint32_t mask = _mm256_movemask_epi8(_mm256_cmpgt_epi8(f, all0));

        if (mask == 0) {
            // all no hit, pass
        } else if (mask == 0xffffffff) {
            // all hit, copy all
            memmove(data + result_offset, data + start_offset, kBatchNums * data_type_size);
            result_offset += kBatchNums;
        } else {
            // #define AVX512_COPY(SHIFT, MASK, WIDTH)                                         \
//     {                                                                           \
//         auto m = (mask >> SHIFT) & MASK;                                        \
//         if (m) {                                                                \
//             __m512i dst;                                                        \
//             __m512i src = _mm512_loadu_epi##WIDTH(data + start_offset + SHIFT); \
//             dst = _mm512_mask_compress_epi##WIDTH(dst, m, src);                 \
//             _mm512_storeu_epi##WIDTH(data + result_offset, dst);                \
//             result_offset += __builtin_popcount(m);                             \
//         }                                                                       \
//     }

#define AVX512_ASM_COPY(SHIFT, MASK, WIDTH)                              \
    {                                                                    \
        auto m = (mask >> SHIFT) & MASK;                                 \
        if (m) {                                                         \
            T* src = data + start_offset + SHIFT;                        \
            T* dst = data + result_offset;                               \
            __asm__ volatile("vmovdqu" #WIDTH                            \
                             " (%[s]), %%zmm1\n"                         \
                             "kmovw %[mask], %%k1\n"                     \
                             "vpcompressd %%zmm1, %%zmm0%{%%k1%}%{z%}\n" \
                             "vmovdqu" #WIDTH " %%zmm0, (%[d])\n"        \
                             : [s] "+r"(src), [d] "+r"(dst)              \
                             : [mask] "r"(m)                             \
                             : "zmm0", "zmm1", "k1", "memory");          \
            result_offset += __builtin_popcount(m);                      \
        }                                                                \
    }

#define AVX512_COPY AVX512_ASM_COPY

#define BITMASK_COPY(mask)                                            \
    {                                                                 \
        phmap::priv::BitMask<uint32_t, 32> bitmask(mask);             \
        for (auto idx : bitmask) {                                    \
            *(data + result_offset++) = *(data + start_offset + idx); \
        }                                                             \
    }

#define BITMASK_COPY2(mask)                                           \
    {                                                                 \
        while (mask) {                                                \
            int idx = __builtin_ctz(mask);                            \
            mask = mask & (mask - 1);                                 \
            *(data + result_offset++) = *(data + start_offset + idx); \
        }                                                             \
    }

#define BRANCHLESS_COPY()                  \
    {                                      \
        int j = start_offset;              \
        for (int i = 0; i < 32; i++) {     \
            data[result_offset] = data[j]; \
            result_offset += f_data[j];    \
            j += 1;                        \
        }                                  \
    }
            // bitmask copy
            if constexpr (mode == 0) {
                BITMASK_COPY(mask);
            }
            // avx512 + bitmask copy
            if constexpr (mode == 1) {
                if constexpr (sizeof(T) == 4) {
                    AVX512_COPY(0, 0xffff, 32);
                    AVX512_COPY(16, 0xffff, 32);
                } else if constexpr (sizeof(T) == 8) {
                    AVX512_COPY(0, 0xff, 64);
                    AVX512_COPY(8, 0xff, 64);
                    AVX512_COPY(16, 0xff, 64);
                    AVX512_COPY(24, 0xff, 64);
                } else {
                    BITMASK_COPY2(mask);
                }
            }
            // branchless copy
            if constexpr (mode == 2) {
                BRANCHLESS_COPY();
            }

            // hybrid
            if constexpr (mode == 3) {
                if constexpr (sizeof(T) == 4) {
                    AVX512_COPY(0, 0xffff, 32);
                    AVX512_COPY(16, 0xffff, 32);
                } else {
                    BITMASK_COPY2(mask);
                }
            }
        }

        start_offset += kBatchNums;
    }
#elif defined(__ARM_NEON__) || defined(__aarch64__)

    constexpr size_t kBatchNums = 128 / (8 * sizeof(uint8_t));
    while (start_offset + kBatchNums < to) {
        uint8x16_t filter = vld1q_u8(f_data);
        if (vmaxvq_u8(filter) == 0) {
            // skip
        } else if (vminvq_u8(filter)) {
            memmove(data + result_offset, data + start_offset, kBatchNums * data_type_size);
            result_offset += kBatchNums;
        } else {
            for (int i = 0; i < kBatchNums; ++i) {
                // the index for vgetq_lane_u8 should be a literal integer
                // but in ASAN/DEBUG the loop is unrolled. so we won't call vgetq_lane_u8
                // in ASAN/DEBUG
#ifndef NDEBUG
                if (vgetq_lane_u8(filter, i)) {
#else
                if (f_data[i]) {
#endif
                    *(data + result_offset++) = *(data + start_offset + i);
                }
            }
        }

        start_offset += kBatchNums;
        f_data += kBatchNums;
    }
#endif
    for (auto i = start_offset; i < to; ++i) {
        if (f_data[i]) {
            *(data + result_offset) = *(data + i);
            result_offset++;
        }
    }

    return result_offset;
}

template <typename T>
static size_t plain_filter_range(const Column::Filter& filter, T* data, size_t from, size_t to) {
    auto start_offset = from;
    auto result_offset = from;
    const uint8_t* f_data = filter.data();
    constexpr size_t data_type_size = sizeof(T);

    for (auto i = start_offset; i < to; ++i) {
        if (f_data[i]) {
            *(data + result_offset) = *(data + i);
            result_offset++;
        }
    }
    return result_offset;
}

static size_t compress_filter_range_int(const Column::Filter& filter, int* data, size_t from, size_t to) {
    auto start_offset = from;
    auto result_offset = from;
    const uint8_t* f_data = filter.data();
    const __m128i all0 = _mm_setzero_si128();
    const int kBatchNums = 16;

    while ((start_offset + kBatchNums) < to) {
        __m128i f = _mm_loadu_si128((const __m128i*)(f_data + start_offset));
        __mmask16 mask = _mm_cmpgt_epi8_mask(f, all0);
        if (mask == 0) {
            ;
        } else if (mask == 1) {
            _mm512_storeu_si512(data + result_offset, _mm512_load_si512(data + start_offset));
        } else {
            __m512i dst;
            __m512i src = _mm512_loadu_epi32(data + start_offset);
            dst = _mm512_mask_compress_epi32(dst, mask, src);
            _mm512_storeu_epi32(data + result_offset, dst);
            result_offset += __builtin_popcount(mask);
        }
        start_offset += kBatchNums;
    }

    for (auto i = start_offset; i < to; ++i) {
        if (f_data[i]) {
            *(data + result_offset) = *(data + i);
            result_offset++;
        }
    }
    return result_offset;
}

static constexpr size_t N = 10'000'000;

template <typename T>
static void run_bitmask_filter(benchmark::State& state) {
    size_t size = N;
    int mode = state.range(0);
    std::vector<T> source(size);
    memset(source.data(), 0x3f, size * sizeof(T));
    Column::Filter filter;
    make_random_filter_data(&filter, size, mode);

    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        filter_range<T, 0>(filter, source.data(), 0, size);
    }
}

template <typename T>
static void run_plain_filter(benchmark::State& state) {
    size_t size = N;
    int mode = state.range(0);
    std::vector<T> source(size);
    memset(source.data(), 0x3f, size * sizeof(T));
    Column::Filter filter;
    make_random_filter_data(&filter, size, mode);

    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        plain_filter_range(filter, source.data(), 0, size);
    }
}

template <typename T>
static void run_compress_filter(benchmark::State& state) {
    size_t size = N;
    int mode = state.range(0);
    std::vector<T> source(size);
    memset(source.data(), 0x3f, size * sizeof(T));
    Column::Filter filter;
    make_random_filter_data(&filter, size, mode);

    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        filter_range<T, 1>(filter, source.data(), 0, size);
    }
}

template <typename T>
static void run_branchless_filter(benchmark::State& state) {
    size_t size = N;
    int mode = state.range(0);
    std::vector<T> source(size);
    memset(source.data(), 0x3f, size * sizeof(T));
    Column::Filter filter;
    make_random_filter_data(&filter, size, mode);

    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        filter_range<T, 2>(filter, source.data(), 0, size);
    }
}

template <typename T>
static void run_hybrid_filter(benchmark::State& state) {
    size_t size = N;
    int mode = state.range(0);
    std::vector<T> source(size);
    memset(source.data(), 0x3f, size * sizeof(T));
    Column::Filter filter;
    make_random_filter_data(&filter, size, mode);

    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        filter_range<T, 3>(filter, source.data(), 0, size);
    }
}

#define MODE 0, 1, 2, 4, 8, 16, 32

#define M(type, width)                                                                    \
    BENCHMARK(run_bitmask_filter<type>)->Name("bitmask" #width)->ArgsProduct({{MODE}});   \
    BENCHMARK(run_compress_filter<type>)->Name("compress" #width)->ArgsProduct({{MODE}}); \
    BENCHMARK(run_branchless_filter<type>)->Name("branchless" #width)->ArgsProduct({{MODE}});

M(char, 8);
M(int16_t, 16);
M(int32_t, 32);
M(int64_t, 64);
