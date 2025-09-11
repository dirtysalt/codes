
#include <benchmark/benchmark.h>
#include <emmintrin.h>
#include <immintrin.h>

#include "phmap/phmap.h"

struct Column {
    struct Filter {
        const uint8_t* data() const { return _data.data(); }
        std::vector<uint8_t> _data;
    };
};

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
#define AVX512_COPY(SHIFT, MASK, WIDTH)                                         \
    {                                                                           \
        auto m = (mask >> SHIFT) & MASK;                                        \
        if (m) {                                                                \
            __m512i dst;                                                        \
            __m512i src = _mm512_loadu_epi##WIDTH(data + start_offset + SHIFT); \
            dst = _mm512_mask_compress_epi##WIDTH(dst, m, src);                 \
            _mm512_storeu_epi##WIDTH(data + result_offset, dst);                \
            result_offset += __builtin_popcount(m);                             \
        }                                                                       \
    }

#define AVX512_ASM_COPY(SHIFT, MASK, WIDTH, WIDTHX)               \
    {                                                             \
        auto m = (mask >> SHIFT) & MASK;                          \
        if (m) {                                                  \
            T* src = data + start_offset + SHIFT;                 \
            T* dst = data + result_offset;                        \
            __asm__ volatile("vmovdqu" #WIDTH                     \
                             " (%[s]), %%zmm1\n"                  \
                             "kmovw %[mask], %%k1\n"              \
                             "vpcompress" #WIDTHX                 \
                             " %%zmm1, %%zmm0%{%%k1%}%{z%}\n"     \
                             "vmovdqu" #WIDTH " %%zmm0, (%[d])\n" \
                             : [s] "+r"(src), [d] "+r"(dst)       \
                             : [mask] "r"(m)                      \
                             : "zmm0", "zmm1", "memory");         \
            result_offset += __builtin_popcount(m);               \
        }                                                         \
    }
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
                    BITMASK_COPY(mask);
                }
            }
            // branchless copy
            if constexpr (mode == 2) {
                BRANCHLESS_COPY();
            }

            // hybrid
            if constexpr (mode == 3) {
                if constexpr (sizeof(T) == 4) {
                    AVX512_ASM_COPY(0, 0xffff, 32, d);
                    AVX512_ASM_COPY(16, 0xffff, 32, d);
                } else if constexpr (sizeof(T) == 8) {
                    AVX512_ASM_COPY(0, 0xff, 64, q);
                    AVX512_ASM_COPY(8, 0xff, 64, q);
                    AVX512_ASM_COPY(16, 0xff, 64, q);
                    AVX512_ASM_COPY(24, 0xff, 64, q);
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

template <typename TYPE, int mode>
int test_type_mode() {
    printf("mode = %d, size = %d: ", mode, sizeof(TYPE));
    std::vector<TYPE> source;
    Column::Filter f;
    int n = 20000;
    int rem = 3;
    f._data.resize(n);
    int end = 0;
    for (int i = 0; i < n; i++) {
        f._data[i] = (i % rem) != 0;
        if (f._data[i]) {
            end += 1;
        }
    }
    source.resize(n);
    for (int i = 0; i < n; i++) {
        source[i] = i & 0xff;
    }
    // int end2 = compress_filter_range_int(f, source.data(), 0, n);
    int end2 = filter_range<TYPE, mode>(f, source.data(), 0, n);
    if (end != end2) {
        printf("end = %d, end2 = %d\n", end, end2);
    }
    assert(end == end2);
    int j = 0;
    for (int i = 0; i < n; i++) {
        if (f._data[i]) {
            if (source[j] != (i & 0xff)) {
                printf("i = %d, j = %d, source[j] = %d\n", i, j, source[j]);
                return 0;
            }
            j += 1;
        }
    }
    printf("PASSED\n");
    return 0;
}

int main() {
#define M(mode)                       \
    test_type_mode<uint8_t, mode>();  \
    test_type_mode<uint16_t, mode>(); \
    test_type_mode<uint32_t, mode>(); \
    test_type_mode<uint64_t, mode>();

    M(0);
    M(1);
    M(2);
    M(3);
    return 0;
}