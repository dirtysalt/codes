#ifdef HAS_RESERVED_IDENTIFIER
#pragma clang diagnostic ignored "-Wreserved-identifier"
#endif

#include <benchmark/benchmark.h>

#include <cstring>
#include <memory>
#include <random>

#include "memcpy-impl.h"

class TestSuite {
public:
    std::string name;
    bool (*fn)();
    void run() {
        printf("%s: ", name.c_str());
        if ((*fn)()) {
            printf("PASSED");
        } else {
            printf("FAILED");
        }
        printf("\n");
    }
};

int main() {
    std::vector<TestSuite> suites;

#define BM(IMPL)                                                                                   \
    auto BM##IMPL = []() {                                                                         \
        size_t max_size = 8 * 1024;                                                                \
        std::vector<uint8_t> _src(max_size), _dst(max_size);                                       \
        uint8_t* src = _src.data();                                                                \
        uint8_t* dst = _dst.data();                                                                \
        for (int i = 0; i < max_size; i++) src[i] = (i & 0xff);                                    \
        for (int size = 1; size <= max_size; size++) {                                             \
            memset(dst, 0, size);                                                                  \
            IMPL(dst, src, size);                                                                  \
            for (int j = 0; j < size; j++) {                                                       \
                if (dst[j] != src[j]) {                                                            \
                    printf("(size = %d, j = %d, src[j]=%d, dst[j]=%d) ", size, j, src[j], dst[j]); \
                    return false;                                                                  \
                }                                                                                  \
            }                                                                                      \
        }                                                                                          \
        return true;                                                                               \
    };                                                                                             \
    suites.emplace_back(TestSuite{.name = #IMPL, .fn = BM##IMPL});

#define VARIANT(N, NAME) BM(NAME)

    VARIANT(1, memcpy)
    VARIANT(2, memcpy_trivial)
    // erms = enhanced repeat movsb & stosb
    VARIANT(4, memcpy_erms)
    VARIANT(5, memcpy_jart)
    VARIANT(6, memcpySSE2)
    VARIANT(7, memcpySSE2Unrolled2)
    VARIANT(8, memcpySSE2Unrolled4)
    VARIANT(9, memcpySSE2Unrolled8)
    VARIANT(9, memcpyAVX2)
    VARIANT(10, memcpy_fast_sse)
    VARIANT(11, memcpy_fast_avx)
    VARIANT(12, memcpy_my)
    VARIANT(13, memcpy_my2)
    VARIANT(21, __memcpy_erms)
    VARIANT(22, __memcpy_sse2_unaligned)
    VARIANT(23, __memcpy_ssse3)
    VARIANT(24, __memcpy_ssse3_back)
    VARIANT(25, __memcpy_avx_unaligned)
    VARIANT(26, __memcpy_avx_unaligned_erms)
    VARIANT(27, __memcpy_avx512_unaligned)
    VARIANT(28, __memcpy_avx512_unaligned_erms)
    VARIANT(29, __memcpy_avx512_no_vzeroupper)
    VARIANT(30, memcpy_sr)
    VARIANT(31, memcpy_gutil)
    VARIANT(32, memcpy_sr2)

    for (auto suite : suites) {
        suite.run();
    }
}