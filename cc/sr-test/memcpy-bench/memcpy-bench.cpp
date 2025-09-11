#ifdef HAS_RESERVED_IDENTIFIER
#pragma clang diagnostic ignored "-Wreserved-identifier"
#endif

#include <benchmark/benchmark.h>

#include <cstring>
#include <memory>
#include <random>

#include "memcpy-impl.h"

#define BM(IMPL)                                                                                \
    void BM##IMPL(benchmark::State& state) {                                                    \
        size_t size = state.range(0);                                                           \
        std::vector<uint8_t> vec_dst(size), vec_src(size);                                      \
        uint8_t* dst = vec_dst.data();                                                          \
        uint8_t* src = vec_src.data();                                                          \
        memset(src, 0x3f, size);                                                                \
        std::mt19937 gen32(0);                                                                  \
        for (auto _ : state) {                                                                  \
            /* (1-(x)/2048) * size. x in [0, 256] */                                            \
            size_t copy_size = (1 - (gen32() & 0x0ff) * 0.000488281) * size;                    \
            IMPL(dst, src, size);                                                               \
            /* /// Execute at least one SSE instruction as a penalty after running AVX code. */ \
            /* __asm__ __volatile__("pxor %%xmm15, %%xmm15" ::: "xmm15");   */                  \
        }                                                                                       \
    }

static constexpr size_t N = 1000000;
static constexpr size_t KB = 1024;
static constexpr size_t MB = 1024 * 1024;

#define VARIANT(N, NAME) \
    BM(NAME)             \
    BENCHMARK(BM##NAME)->Name(#NAME)->DenseRange(1, 16, 1)->Threads(1); // ->Threads(8);

// BENCHMARK(BM##NAME)->Name(#NAME)->DenseRange(32*KB, 2*MB, 32*KB)->Threads(1)->Threads(8);
// BENCHMARK(BM##NAME)->Name(#NAME)->DenseRange(1*KB, 64*KB, 1*KB)->Threads(1)->Threads(8);
// BENCHMARK(BM##NAME)->Name(#NAME)->DenseRange(32*KB, 2*MB, 32*KB)->Threads(1)->Threads(8);
// BENCHMARK(BM##NAME)->Name(#NAME)->DenseRange(2 * MB, 64 * MB, 1 * MB)->Threads(1)->Threads(8);
// BENCHMARK(BM##NAME)->Name(#NAME)->RangeMultiplier(4)->Range(16, 128 * MB)->Threads(1)->Threads(8);

// #define BENCH_ALL

#ifdef BENCH_ALL

VARIANT(1, memcpy)
VARIANT(2, memcpy_trivial)
// erms = enhanced repeat movsb & stosb
VARIANT(4, memcpy_erms)
VARIANT(5, memcpy_jart)
VARIANT(6, memcpySSE2)
// VARIANT(7, memcpySSE2Unrolled2)
// VARIANT(8, memcpySSE2Unrolled4)
// VARIANT(9, memcpySSE2Unrolled8)
VARIANT(9, memcpyAVX2)
VARIANT(10, memcpy_fast_sse)
VARIANT(11, memcpy_fast_avx)
VARIANT(12, memcpy_my)
VARIANT(13, memcpy_my2)
VARIANT(21, __memcpy_erms)
// VARIANT(22, __memcpy_sse2_unaligned)
VARIANT(23, __memcpy_ssse3)
VARIANT(24, __memcpy_ssse3_back)
VARIANT(25, __memcpy_avx_unaligned)
VARIANT(26, __memcpy_avx_unaligned_erms)
// VARIANT(27, __memcpy_avx512_unaligned)
// VARIANT(28, __memcpy_avx512_unaligned_erms)
// VARIANT(29, __memcpy_avx512_no_vzeroupper)

#else

// VARIANT(1, memcpy)
// VARIANT(1, __memcpy_avx_unaligned)
// VARIANT(1, __memcpy_avx_unaligned_erms)
// VARIANT(4, memcpy_erms)
// VARIANT(6, memcpySSE2)
// VARIANT(9, memcpyAVX2)
// VARIANT(10, memcpy_fast_sse)
// VARIANT(11, memcpy_fast_avx)
// VARIANT(12, memcpy_my)
// VARIANT(13, memcpy_my2)
// VARIANT(21, __memcpy_erms)
// VARIANT(24, __memcpy_ssse3_back)
// VARIANT(30, memcpy_sr)
VARIANT(31, memcpy_gutil)
VARIANT(32, memcpy_sr2)

#endif
