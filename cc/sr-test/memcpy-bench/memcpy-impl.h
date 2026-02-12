#include <emmintrin.h>
#include <immintrin.h>

#include <cstddef>
#include <cstdint>
#include <cstring>

#include "FastMemcpy.h"
#include "FastMemcpy_Avx.h"

using memcpy_type = void* (*)(const void* __restrict, void* __restrict, size_t);

static void* memcpy_erms(void* dst, const void* src, size_t size) {
    asm volatile("rep movsb" : "=D"(dst), "=S"(src), "=c"(size) : "0"(dst), "1"(src), "2"(size) : "memory");
    return dst;
}

static void* memcpy_trivial(void* __restrict dst_, const void* __restrict src_, size_t size) {
    char* __restrict dst = reinterpret_cast<char* __restrict>(dst_);
    const char* __restrict src = reinterpret_cast<const char* __restrict>(src_);
    void* ret = dst;

    while (size > 0) {
        *dst = *src;
        ++dst;
        ++src;
        --size;
    }

    return ret;
}

extern "C" void* memcpy_jart(void* dst, const void* src, size_t size);
extern "C" void MemCpy(void* dst, const void* src, size_t size);

extern void* memcpy_fast_sse(void* dst, const void* src, size_t size);
extern void* memcpy_fast_avx(void* dst, const void* src, size_t size);
void* memcpy_tiny(void* dst, const void* src, size_t size);

static void* memcpySSE2(void* __restrict destination, const void* __restrict source, size_t size) {
    unsigned char* dst = reinterpret_cast<unsigned char*>(destination);
    const unsigned char* src = reinterpret_cast<const unsigned char*>(source);
    size_t padding;

    // small memory copy
    if (size <= 16) return memcpy_tiny(dst, src, size);

    // align destination to 16 bytes boundary
    padding = (16 - (reinterpret_cast<size_t>(dst) & 15)) & 15;

    if (padding > 0) {
        __m128i head = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src));
        _mm_storeu_si128(reinterpret_cast<__m128i*>(dst), head);
        dst += padding;
        src += padding;
        size -= padding;
    }

    // medium size copy
    __m128i c0;

    for (; size >= 16; size -= 16) {
        c0 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src));
        src += 16;
        _mm_store_si128((reinterpret_cast<__m128i*>(dst)), c0);
        dst += 16;
    }

    memcpy_tiny(dst, src, size);
    return destination;
}

static void* memcpyAVX2(void* __restrict destination, const void* __restrict source, size_t size) {
    unsigned char* dst = reinterpret_cast<unsigned char*>(destination);
    const unsigned char* src = reinterpret_cast<const unsigned char*>(source);
    size_t padding;

    // small memory copy
    if (size <= 32) return memcpy_tiny(dst, src, size);

    // align destination to 16 bytes boundary
    padding = (32 - (reinterpret_cast<size_t>(dst) & 31)) & 31;

    if (padding > 0) {
        __m256i head = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src));
        _mm256_storeu_si256(reinterpret_cast<__m256i*>(dst), head);
        dst += padding;
        src += padding;
        size -= padding;
    }

    // medium size copy
    __m256i c0;

    for (; size >= 32; size -= 32) {
        c0 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src));
        src += 32;
        _mm256_store_si256((reinterpret_cast<__m256i*>(dst)), c0);
        dst += 32;
    }

    memcpy_tiny(dst, src, size);
    return destination;
}

static void* memcpySSE2Unrolled2(void* __restrict destination, const void* __restrict source, size_t size) {
    unsigned char* dst = reinterpret_cast<unsigned char*>(destination);
    const unsigned char* src = reinterpret_cast<const unsigned char*>(source);
    size_t padding;

    // small memory copy
    if (size <= 32) return memcpy_tiny(dst, src, size);

    // align destination to 16 bytes boundary
    padding = (16 - (reinterpret_cast<size_t>(dst) & 15)) & 15;

    if (padding > 0) {
        __m128i head = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src));
        _mm_storeu_si128(reinterpret_cast<__m128i*>(dst), head);
        dst += padding;
        src += padding;
        size -= padding;
    }

    // medium size copy
    __m128i c0, c1;

    for (; size >= 32; size -= 32) {
        c0 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 0);
        c1 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 1);
        src += 32;
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 0), c0);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 1), c1);
        dst += 32;
    }

    memcpy_tiny(dst, src, size);
    return destination;
}

static void* memcpySSE2Unrolled4(void* __restrict destination, const void* __restrict source, size_t size) {
    unsigned char* dst = reinterpret_cast<unsigned char*>(destination);
    const unsigned char* src = reinterpret_cast<const unsigned char*>(source);
    size_t padding;

    // small memory copy
    if (size <= 64) return memcpy_tiny(dst, src, size);

    // align destination to 16 bytes boundary
    padding = (16 - (reinterpret_cast<size_t>(dst) & 15)) & 15;

    if (padding > 0) {
        __m128i head = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src));
        _mm_storeu_si128(reinterpret_cast<__m128i*>(dst), head);
        dst += padding;
        src += padding;
        size -= padding;
    }

    // medium size copy
    __m128i c0, c1, c2, c3;

    for (; size >= 64; size -= 64) {
        c0 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 0);
        c1 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 1);
        c2 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 2);
        c3 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 3);
        src += 64;
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 0), c0);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 1), c1);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 2), c2);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 3), c3);
        dst += 64;
    }

    memcpy_tiny(dst, src, size);
    return destination;
}

static void* memcpySSE2Unrolled8(void* __restrict destination, const void* __restrict source, size_t size) {
    unsigned char* dst = reinterpret_cast<unsigned char*>(destination);
    const unsigned char* src = reinterpret_cast<const unsigned char*>(source);
    size_t padding;

    // small memory copy
    if (size <= 128) return memcpy_tiny(dst, src, size);

    // align destination to 16 bytes boundary
    padding = (16 - (reinterpret_cast<size_t>(dst) & 15)) & 15;

    if (padding > 0) {
        __m128i head = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src));
        _mm_storeu_si128(reinterpret_cast<__m128i*>(dst), head);
        dst += padding;
        src += padding;
        size -= padding;
    }

    // medium size copy
    __m128i c0, c1, c2, c3, c4, c5, c6, c7;

    for (; size >= 128; size -= 128) {
        c0 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 0);
        c1 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 1);
        c2 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 2);
        c3 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 3);
        c4 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 4);
        c5 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 5);
        c6 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 6);
        c7 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 7);
        src += 128;
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 0), c0);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 1), c1);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 2), c2);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 3), c3);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 4), c4);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 5), c5);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 6), c6);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 7), c7);
        dst += 128;
    }

    memcpy_tiny(dst, src, size);
    return destination;
}

//static __attribute__((__always_inline__, __target__("sse2")))
__attribute__((__always_inline__)) inline void memcpy_my_medium_sse(uint8_t* __restrict& dst,
                                                                    const uint8_t* __restrict& src, size_t& size) {
    /// Align destination to 16 bytes boundary.
    size_t padding = (16 - (reinterpret_cast<size_t>(dst) & 15)) & 15;

    if (padding > 0) {
        __m128i head = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src));
        _mm_storeu_si128(reinterpret_cast<__m128i*>(dst), head);
        dst += padding;
        src += padding;
        size -= padding;
    }

    /// Aligned unrolled copy.
    __m128i c0, c1, c2, c3, c4, c5, c6, c7;

    while (size >= 128) {
        c0 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 0);
        c1 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 1);
        c2 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 2);
        c3 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 3);
        c4 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 4);
        c5 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 5);
        c6 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 6);
        c7 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 7);
        src += 128;
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 0), c0);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 1), c1);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 2), c2);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 3), c3);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 4), c4);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 5), c5);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 6), c6);
        _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 7), c7);
        dst += 128;

        size -= 128;
    }
}

__attribute__((__target__("avx"))) void memcpy_my_medium_avx(uint8_t* __restrict& __restrict dst,
                                                             const uint8_t* __restrict& __restrict src,
                                                             size_t& __restrict size) {
    size_t padding = (32 - (reinterpret_cast<size_t>(dst) & 31)) & 31;

    if (padding > 0) {
        __m256i head = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src));
        _mm256_storeu_si256(reinterpret_cast<__m256i*>(dst), head);
        dst += padding;
        src += padding;
        size -= padding;
    }

    __m256i c0, c1, c2, c3, c4, c5, c6, c7;

    while (size >= 256) {
        c0 = _mm256_loadu_si256((reinterpret_cast<const __m256i*>(src)) + 0);
        c1 = _mm256_loadu_si256((reinterpret_cast<const __m256i*>(src)) + 1);
        c2 = _mm256_loadu_si256((reinterpret_cast<const __m256i*>(src)) + 2);
        c3 = _mm256_loadu_si256((reinterpret_cast<const __m256i*>(src)) + 3);
        c4 = _mm256_loadu_si256((reinterpret_cast<const __m256i*>(src)) + 4);
        c5 = _mm256_loadu_si256((reinterpret_cast<const __m256i*>(src)) + 5);
        c6 = _mm256_loadu_si256((reinterpret_cast<const __m256i*>(src)) + 6);
        c7 = _mm256_loadu_si256((reinterpret_cast<const __m256i*>(src)) + 7);
        src += 256;
        _mm256_store_si256(((reinterpret_cast<__m256i*>(dst)) + 0), c0);
        _mm256_store_si256(((reinterpret_cast<__m256i*>(dst)) + 1), c1);
        _mm256_store_si256(((reinterpret_cast<__m256i*>(dst)) + 2), c2);
        _mm256_store_si256(((reinterpret_cast<__m256i*>(dst)) + 3), c3);
        _mm256_store_si256(((reinterpret_cast<__m256i*>(dst)) + 4), c4);
        _mm256_store_si256(((reinterpret_cast<__m256i*>(dst)) + 5), c5);
        _mm256_store_si256(((reinterpret_cast<__m256i*>(dst)) + 6), c6);
        _mm256_store_si256(((reinterpret_cast<__m256i*>(dst)) + 7), c7);
        dst += 256;

        size -= 256;
    }
}

// Unfortunately avx version does not work correctly.
// bool have_avx = true;
bool have_avx = false;

static uint8_t* memcpy_my(uint8_t* __restrict dst, const uint8_t* __restrict src, size_t size) {
    uint8_t* ret = dst;

tail:
    if (size <= 16) {
        if (size >= 8) {
            __builtin_memcpy(dst + size - 8, src + size - 8, 8);
            __builtin_memcpy(dst, src, 8);
        } else if (size >= 4) {
            __builtin_memcpy(dst + size - 4, src + size - 4, 4);
            __builtin_memcpy(dst, src, 4);
        } else if (size >= 2) {
            __builtin_memcpy(dst + size - 2, src + size - 2, 2);
            __builtin_memcpy(dst, src, 2);
        } else if (size >= 1) {
            *dst = *src;
        }
    } else if (have_avx) {
        if (size <= 32) {
            __builtin_memcpy(dst, src, 8);
            __builtin_memcpy(dst + 8, src + 8, 8);

            dst += 16;
            src += 16;
            size -= 16;

            goto tail;
        }

        if (size <= 256) {
            __asm__ volatile(
                    "vmovups    -0x20(%[s],%[size],1), %%ymm0\n"
                    "vmovups    %%ymm0, -0x20(%[d],%[size],1)\n"
                    : [d] "+r"(dst), [s] "+r"(src)
                    : [size] "r"(size)
                    : "ymm0", "memory");

            while (size > 32) {
                __asm__ volatile(
                        "vmovups    (%[s]), %%ymm0\n"
                        "vmovups    %%ymm0, (%[d])\n"
                        : [d] "+r"(dst), [s] "+r"(src)
                        :
                        : "ymm0", "memory");

                dst += 32;
                src += 32;
                size -= 32;
            }
        } else {
            size_t padding = (32 - (reinterpret_cast<size_t>(dst) & 31)) & 31;

            if (padding > 0) {
                __asm__ volatile(
                        "vmovups    (%[s]), %%ymm0\n"
                        "vmovups    %%ymm0, (%[d])\n"
                        : [d] "+r"(dst), [s] "+r"(src)
                        :
                        : "ymm0", "memory");

                dst += padding;
                src += padding;
                size -= padding;
            }

            while (size >= 256) {
                __asm__ volatile(
                        "vmovups    (%[s]), %%ymm0\n"
                        "vmovups    0x20(%[s]), %%ymm1\n"
                        "vmovups    0x40(%[s]), %%ymm2\n"
                        "vmovups    0x60(%[s]), %%ymm3\n"
                        "vmovups    0x80(%[s]), %%ymm4\n"
                        "vmovups    0xa0(%[s]), %%ymm5\n"
                        "vmovups    0xc0(%[s]), %%ymm6\n"
                        "vmovups    0xe0(%[s]), %%ymm7\n"
                        "add        $0x100,%[s]\n"
                        "vmovaps    %%ymm0, (%[d])\n"
                        "vmovaps    %%ymm1, 0x20(%[d])\n"
                        "vmovaps    %%ymm2, 0x40(%[d])\n"
                        "vmovaps    %%ymm3, 0x60(%[d])\n"
                        "vmovaps    %%ymm4, 0x80(%[d])\n"
                        "vmovaps    %%ymm5, 0xa0(%[d])\n"
                        "vmovaps    %%ymm6, 0xc0(%[d])\n"
                        "vmovaps    %%ymm7, 0xe0(%[d])\n"
                        "add        $0x100, %[d]\n"
                        : [d] "+r"(dst), [s] "+r"(src)
                        :
                        : "ymm0", "ymm1", "ymm2", "ymm3", "ymm4", "ymm5", "ymm6", "ymm7", "memory");

                size -= 256;
            }

            goto tail;
        }
    } else {
        if (size <= 128) {
            _mm_storeu_si128(reinterpret_cast<__m128i*>(dst + size - 16),
                             _mm_loadu_si128(reinterpret_cast<const __m128i*>(src + size - 16)));

            while (size > 16) {
                _mm_storeu_si128(reinterpret_cast<__m128i*>(dst),
                                 _mm_loadu_si128(reinterpret_cast<const __m128i*>(src)));
                dst += 16;
                src += 16;
                size -= 16;
            }
        } else {
            /// Align destination to 16 bytes boundary.
            size_t padding = (16 - (reinterpret_cast<size_t>(dst) & 15)) & 15;

            if (padding > 0) {
                __m128i head = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src));
                _mm_storeu_si128(reinterpret_cast<__m128i*>(dst), head);
                dst += padding;
                src += padding;
                size -= padding;
            }

            /// Aligned unrolled copy.
            __m128i c0, c1, c2, c3, c4, c5, c6, c7;

            while (size >= 128) {
                c0 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 0);
                c1 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 1);
                c2 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 2);
                c3 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 3);
                c4 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 4);
                c5 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 5);
                c6 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 6);
                c7 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 7);
                src += 128;
                _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 0), c0);
                _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 1), c1);
                _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 2), c2);
                _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 3), c3);
                _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 4), c4);
                _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 5), c5);
                _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 6), c6);
                _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 7), c7);
                dst += 128;

                size -= 128;
            }

            goto tail;
        }
    }

    return ret;
}

static uint8_t* memcpy_my2(uint8_t* __restrict dst, const uint8_t* __restrict src, size_t size) {
    uint8_t* ret = dst;

    if (size <= 16) {
        if (size >= 8) {
            __builtin_memcpy(dst + size - 8, src + size - 8, 8);
            __builtin_memcpy(dst, src, 8);
        } else if (size >= 4) {
            __builtin_memcpy(dst + size - 4, src + size - 4, 4);
            __builtin_memcpy(dst, src, 4);
        } else if (size >= 2) {
            __builtin_memcpy(dst + size - 2, src + size - 2, 2);
            __builtin_memcpy(dst, src, 2);
        } else if (size >= 1) {
            *dst = *src;
        }
    } else if (size <= 128) {
        _mm_storeu_si128(reinterpret_cast<__m128i*>(dst + size - 16),
                         _mm_loadu_si128(reinterpret_cast<const __m128i*>(src + size - 16)));

        while (size > 16) {
            _mm_storeu_si128(reinterpret_cast<__m128i*>(dst), _mm_loadu_si128(reinterpret_cast<const __m128i*>(src)));
            dst += 16;
            src += 16;
            size -= 16;
        }
    } else if (size < 30000 || !have_avx) {
        /// Align destination to 16 bytes boundary.
        size_t padding = (16 - (reinterpret_cast<size_t>(dst) & 15)) & 15;

        if (padding > 0) {
            __m128i head = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src));
            _mm_storeu_si128(reinterpret_cast<__m128i*>(dst), head);
            dst += padding;
            src += padding;
            size -= padding;
        }

        /// Aligned unrolled copy.
        __m128i c0, c1, c2, c3, c4, c5, c6, c7;

        while (size >= 128) {
            c0 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 0);
            c1 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 1);
            c2 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 2);
            c3 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 3);
            c4 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 4);
            c5 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 5);
            c6 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 6);
            c7 = _mm_loadu_si128(reinterpret_cast<const __m128i*>(src) + 7);
            src += 128;
            _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 0), c0);
            _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 1), c1);
            _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 2), c2);
            _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 3), c3);
            _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 4), c4);
            _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 5), c5);
            _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 6), c6);
            _mm_store_si128((reinterpret_cast<__m128i*>(dst) + 7), c7);
            dst += 128;

            size -= 128;
        }

        _mm_storeu_si128(reinterpret_cast<__m128i*>(dst + size - 16),
                         _mm_loadu_si128(reinterpret_cast<const __m128i*>(src + size - 16)));

        while (size > 16) {
            _mm_storeu_si128(reinterpret_cast<__m128i*>(dst), _mm_loadu_si128(reinterpret_cast<const __m128i*>(src)));
            dst += 16;
            src += 16;
            size -= 16;
        }
    } else {
        size_t padding = (32 - (reinterpret_cast<size_t>(dst) & 31)) & 31;

        if (padding > 0) {
            __asm__ volatile(
                    "vmovups    (%[s]), %%ymm0\n"
                    "vmovups    %%ymm0, (%[d])\n"
                    : [d] "+r"(dst), [s] "+r"(src)
                    :
                    : "ymm0", "memory");

            dst += padding;
            src += padding;
            size -= padding;
        }

        while (size >= 512) /// NOLINT
        {
            __asm__ volatile(
                    "vmovups    (%[s]), %%ymm0\n"
                    "vmovups    0x20(%[s]), %%ymm1\n"
                    "vmovups    0x40(%[s]), %%ymm2\n"
                    "vmovups    0x60(%[s]), %%ymm3\n"
                    "vmovups    0x80(%[s]), %%ymm4\n"
                    "vmovups    0xa0(%[s]), %%ymm5\n"
                    "vmovups    0xc0(%[s]), %%ymm6\n"
                    "vmovups    0xe0(%[s]), %%ymm7\n"
                    "vmovups    0x100(%[s]), %%ymm8\n"
                    "vmovups    0x120(%[s]), %%ymm9\n"
                    "vmovups    0x140(%[s]), %%ymm10\n"
                    "vmovups    0x160(%[s]), %%ymm11\n"
                    "vmovups    0x180(%[s]), %%ymm12\n"
                    "vmovups    0x1a0(%[s]), %%ymm13\n"
                    "vmovups    0x1c0(%[s]), %%ymm14\n"
                    "vmovups    0x1e0(%[s]), %%ymm15\n"
                    "add        $0x200, %[s]\n"
                    "sub        $0x200, %[size]\n"
                    "vmovaps    %%ymm0, (%[d])\n"
                    "vmovaps    %%ymm1, 0x20(%[d])\n"
                    "vmovaps    %%ymm2, 0x40(%[d])\n"
                    "vmovaps    %%ymm3, 0x60(%[d])\n"
                    "vmovaps    %%ymm4, 0x80(%[d])\n"
                    "vmovaps    %%ymm5, 0xa0(%[d])\n"
                    "vmovaps    %%ymm6, 0xc0(%[d])\n"
                    "vmovaps    %%ymm7, 0xe0(%[d])\n"
                    "vmovaps    %%ymm8, 0x100(%[d])\n"
                    "vmovaps    %%ymm9, 0x120(%[d])\n"
                    "vmovaps    %%ymm10, 0x140(%[d])\n"
                    "vmovaps    %%ymm11, 0x160(%[d])\n"
                    "vmovaps    %%ymm12, 0x180(%[d])\n"
                    "vmovaps    %%ymm13, 0x1a0(%[d])\n"
                    "vmovaps    %%ymm14, 0x1c0(%[d])\n"
                    "vmovaps    %%ymm15, 0x1e0(%[d])\n"
                    "add        $0x200, %[d]\n"
                    : [d] "+r"(dst), [s] "+r"(src), [size] "+r"(size)
                    :
                    : "ymm0", "ymm1", "ymm2", "ymm3", "ymm4", "ymm5", "ymm6", "ymm7", "ymm8", "ymm9", "ymm10", "ymm11",
                      "ymm12", "ymm13", "ymm14", "ymm15", "memory");
        }

        /*while (size >= 256)
        {
            __asm__(
                "vmovups    (%[s]), %%ymm0\n"
                "vmovups    0x20(%[s]), %%ymm1\n"
                "vmovups    0x40(%[s]), %%ymm2\n"
                "vmovups    0x60(%[s]), %%ymm3\n"
                "vmovups    0x80(%[s]), %%ymm4\n"
                "vmovups    0xa0(%[s]), %%ymm5\n"
                "vmovups    0xc0(%[s]), %%ymm6\n"
                "vmovups    0xe0(%[s]), %%ymm7\n"
                "add        $0x100,%[s]\n"
                "vmovaps    %%ymm0, (%[d])\n"
                "vmovaps    %%ymm1, 0x20(%[d])\n"
                "vmovaps    %%ymm2, 0x40(%[d])\n"
                "vmovaps    %%ymm3, 0x60(%[d])\n"
                "vmovaps    %%ymm4, 0x80(%[d])\n"
                "vmovaps    %%ymm5, 0xa0(%[d])\n"
                "vmovaps    %%ymm6, 0xc0(%[d])\n"
                "vmovaps    %%ymm7, 0xe0(%[d])\n"
                "add        $0x100, %[d]\n"
                : [d]"+r"(dst), [s]"+r"(src)
                :
                : "ymm0", "ymm1", "ymm2", "ymm3", "ymm4", "ymm5", "ymm6", "ymm7", "memory");

            size -= 256;
        }*/

        /*while (size > 128)
        {
            __asm__(
                "vmovups    (%[s]), %%ymm0\n"
                "vmovups    0x20(%[s]), %%ymm1\n"
                "vmovups    0x40(%[s]), %%ymm2\n"
                "vmovups    0x60(%[s]), %%ymm3\n"
                "add        $0x80, %[s]\n"
                "sub        $0x80, %[size]\n"
                "vmovaps    %%ymm0, (%[d])\n"
                "vmovaps    %%ymm1, 0x20(%[d])\n"
                "vmovaps    %%ymm2, 0x40(%[d])\n"
                "vmovaps    %%ymm3, 0x60(%[d])\n"
                "add        $0x80, %[d]\n"
                : [d]"+r"(dst), [s]"+r"(src), [size]"+r"(size)
                :
                : "ymm0", "ymm1", "ymm2", "ymm3", "memory");
        }*/

        __asm__ volatile(
                "vmovups    -0x20(%[s],%[size],1), %%ymm0\n"
                "vmovups    %%ymm0, -0x20(%[d],%[size],1)\n"
                : [d] "+r"(dst), [s] "+r"(src)
                : [size] "r"(size)
                : "ymm0", "memory");

        while (size > 32) {
            __asm__ volatile(
                    "vmovups    (%[s]), %%ymm0\n"
                    "vmovups    %%ymm0, (%[d])\n"
                    : [d] "+r"(dst), [s] "+r"(src)
                    :
                    : "ymm0", "memory");

            dst += 32;
            src += 32;
            size -= 32;
        }

        __asm__ __volatile__("vzeroupper" ::
                                     : "ymm0", "ymm1", "ymm2", "ymm3", "ymm4", "ymm5", "ymm6", "ymm7", "ymm8", "ymm9",
                                       "ymm10", "ymm11", "ymm12", "ymm13", "ymm14", "ymm15");
    }

    return ret;
}

extern "C" void* __memcpy_erms(void* __restrict destination, const void* __restrict source, size_t size); /// NOLINT
extern "C" void* __memcpy_sse2_unaligned(void* __restrict destination, const void* __restrict source,
                                         size_t size);                                                     /// NOLINT
extern "C" void* __memcpy_ssse3(void* __restrict destination, const void* __restrict source, size_t size); /// NOLINT
extern "C" void* __memcpy_ssse3_back(void* __restrict destination, const void* __restrict source,
                                     size_t size); /// NOLINT
extern "C" void* __memcpy_avx_unaligned(void* __restrict destination, const void* __restrict source,
                                        size_t size); /// NOLINT
extern "C" void* __memcpy_avx_unaligned_erms(void* __restrict destination, const void* __restrict source,
                                             size_t size); /// NOLINT
extern "C" void* __memcpy_avx512_unaligned(void* __restrict destination, const void* __restrict source,
                                           size_t size); /// NOLINT
extern "C" void* __memcpy_avx512_unaligned_erms(void* __restrict destination, const void* __restrict source,
                                                size_t size); /// NOLINT
extern "C" void* __memcpy_avx512_no_vzeroupper(void* __restrict destination, const void* __restrict source,
                                               size_t size); /// NOLINT

// The standard memcpy operation is slow for variable small sizes.
// This implementation inlines the optimal realization for sizes 1 to 16.
// To avoid code bloat don't use it in case of not performance-critical spots,
// nor when you don't expect very frequent values of size <= 16.
inline void* memcpy_gutil(void* dst, const void* src, size_t size) {
    // Compiler inlines code with minimal amount of data movement when third
    // parameter of memcpy is a constant.
    switch (size) {
    case 0:
        break;
    case 1:
        __builtin_memcpy(dst, src, 1);
        break;
    case 2:
        __builtin_memcpy(dst, src, 2);
        break;
    case 3:
        __builtin_memcpy(dst, src, 3);
        break;
    case 4:
        __builtin_memcpy(dst, src, 4);
        break;
    case 5:
        __builtin_memcpy(dst, src, 5);
        break;
    case 6:
        __builtin_memcpy(dst, src, 6);
        break;
    case 7:
        __builtin_memcpy(dst, src, 7);
        break;
    case 8:
        __builtin_memcpy(dst, src, 8);
        break;
    case 9:
        __builtin_memcpy(dst, src, 9);
        break;
    case 10:
        __builtin_memcpy(dst, src, 10);
        break;
    case 11:
        __builtin_memcpy(dst, src, 11);
        break;
    case 12:
        __builtin_memcpy(dst, src, 12);
        break;
    case 13:
        __builtin_memcpy(dst, src, 13);
        break;
    case 14:
        __builtin_memcpy(dst, src, 14);
        break;
    case 15:
        __builtin_memcpy(dst, src, 15);
        break;
    case 16:
        __builtin_memcpy(dst, src, 16);
        break;
    default:
        std::memcpy(dst, src, size);
        break;
    }
    return dst;
}

static inline uint8_t* memcpy_sr(uint8_t* __restrict dst, const uint8_t* __restrict src, size_t size) {
    uint8_t* ret = dst;

    [[maybe_unused]] tail : if (size <= 16) {
        if (size >= 8) {
            __builtin_memcpy(dst + size - 8, src + size - 8, 8);
            __builtin_memcpy(dst, src, 8);
        } else if (size >= 4) {
            __builtin_memcpy(dst + size - 4, src + size - 4, 4);
            __builtin_memcpy(dst, src, 4);
        } else if (size >= 2) {
            __builtin_memcpy(dst + size - 2, src + size - 2, 2);
            __builtin_memcpy(dst, src, 2);
        } else if (size >= 1) {
            *dst = *src;
        }
    }
    else {
#ifdef __AVX2__
        if (size <= 256) {
            if (size <= 32) {
                __builtin_memcpy(dst, src, 8);
                __builtin_memcpy(dst + 8, src + 8, 8);
                size -= 16;
                dst += 16;
                src += 16;
                goto tail;
            }

            while (size > 32) {
                _mm256_storeu_si256(reinterpret_cast<__m256i*>(dst),
                                    _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src)));
                dst += 32;
                src += 32;
                size -= 32;
            }

            _mm256_storeu_si256(reinterpret_cast<__m256i*>(dst + size - 32),
                                _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + size - 32)));
        } else {
            static constexpr size_t KB = 1024;
            if (size >= 512 * KB && size <= 2048 * KB) {
                // erms(enhanced repeat movsv/stosb) version works well in this region.
                asm volatile("rep movsb" : "=D"(dst), "=S"(src), "=c"(size) : "0"(dst), "1"(src), "2"(size) : "memory");
            } else {
                size_t padding = (32 - (reinterpret_cast<size_t>(dst) & 31)) & 31;

                if (padding > 0) {
                    __m256i head = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src));
                    _mm256_storeu_si256(reinterpret_cast<__m256i*>(dst), head);
                    dst += padding;
                    src += padding;
                    size -= padding;
                }

                while (size >= 256) {
                    __m256i c0 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src));
                    __m256i c1 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 32));
                    __m256i c2 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 64));
                    __m256i c3 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 96));
                    __m256i c4 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 128));
                    __m256i c5 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 160));
                    __m256i c6 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 192));
                    __m256i c7 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 224));
                    src += 256;

                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst)), c0);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 32)), c1);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 64)), c2);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 96)), c3);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 128)), c4);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 160)), c5);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 192)), c6);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 224)), c7);
                    dst += 256;

                    size -= 256;
                }

                goto tail;
            }
        }
#else
        std::memcpy(dst, src, size);
#endif
    }
    return ret;
}

static inline uint8_t* memcpy_sr2(uint8_t* __restrict dst, const uint8_t* __restrict src, size_t size) {
    uint8_t* ret = dst;
    [[maybe_unused]] tail : if (size <= 16) {
        switch (size) {
        case 0:
            break;
        case 1:
            __builtin_memcpy(dst, src, 1);
            break;
        case 2:
            __builtin_memcpy(dst, src, 2);
            break;
        case 3:
            __builtin_memcpy(dst, src, 3);
            break;
        case 4:
            __builtin_memcpy(dst, src, 4);
            break;
        case 5:
            __builtin_memcpy(dst, src, 5);
            break;
        case 6:
            __builtin_memcpy(dst, src, 6);
            break;
        case 7:
            __builtin_memcpy(dst, src, 7);
            break;
        case 8:
            __builtin_memcpy(dst, src, 8);
            break;
        case 9:
            __builtin_memcpy(dst, src, 9);
            break;
        case 10:
            __builtin_memcpy(dst, src, 10);
            break;
        case 11:
            __builtin_memcpy(dst, src, 11);
            break;
        case 12:
            __builtin_memcpy(dst, src, 12);
            break;
        case 13:
            __builtin_memcpy(dst, src, 13);
            break;
        case 14:
            __builtin_memcpy(dst, src, 14);
            break;
        case 15:
            __builtin_memcpy(dst, src, 15);
            break;
        case 16:
            __builtin_memcpy(dst, src, 16);
            break;
        }
    }
    else {
#ifdef __AVX2__
        if (size <= 256) {
            if (size <= 32) {
                __builtin_memcpy(dst, src, 8);
                __builtin_memcpy(dst + 8, src + 8, 8);
                size -= 16;
                dst += 16;
                src += 16;
                goto tail;
            }

            while (size > 32) {
                _mm256_storeu_si256(reinterpret_cast<__m256i*>(dst),
                                    _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src)));
                dst += 32;
                src += 32;
                size -= 32;
            }

            _mm256_storeu_si256(reinterpret_cast<__m256i*>(dst + size - 32),
                                _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + size - 32)));
        } else {
            static constexpr size_t KB = 1024;
            if (size >= 512 * KB && size <= 2048 * KB) {
                // erms(enhanced repeat movsv/stosb) version works well in this region.
                asm volatile("rep movsb" : "=D"(dst), "=S"(src), "=c"(size) : "0"(dst), "1"(src), "2"(size) : "memory");
            } else {
                size_t padding = (32 - (reinterpret_cast<size_t>(dst) & 31)) & 31;

                if (padding > 0) {
                    __m256i head = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src));
                    _mm256_storeu_si256(reinterpret_cast<__m256i*>(dst), head);
                    dst += padding;
                    src += padding;
                    size -= padding;
                }

                while (size >= 256) {
                    __m256i c0 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src));
                    __m256i c1 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 32));
                    __m256i c2 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 64));
                    __m256i c3 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 96));
                    __m256i c4 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 128));
                    __m256i c5 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 160));
                    __m256i c6 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 192));
                    __m256i c7 = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(src + 224));
                    src += 256;

                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst)), c0);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 32)), c1);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 64)), c2);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 96)), c3);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 128)), c4);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 160)), c5);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 192)), c6);
                    _mm256_store_si256((reinterpret_cast<__m256i*>(dst + 224)), c7);
                    dst += 256;

                    size -= 256;
                }

                goto tail;
            }
        }
#else
        std::memcpy(dst, src, size);
#endif
    }
    return ret;
}
