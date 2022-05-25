/* coding:utf-8
 * Copyright (C) dirlt
 */

#include "Common.h"
using namespace std;

#if AVX512
void convert_i64toi8_avx512(int64_t* src, int8_t* dst, size_t size) {
    static uint8_t mask_data[64] = {
            0x00, 0x08, 0x10, 0x18, 0x20, 0x28, 0x30, 0x38,
    };
    size_t offset = 0;
    int64_t* end = src + size;
    size_t loop = size / 8;
    __m512i mask = _mm512_loadu_epi8(mask_data);
    for (size_t i = 0; i < loop; i++) {
        __m512i a = _mm512_loadu_epi8(src);
        __m512i b = _mm512_permutex2var_epi8(a, mask, a);
        __m128i x = _mm512_castsi512_si128(b);
        _mm_storeu_si64(dst, x);
        dst += 8;
        src += 8;
    }
    while (src < end) {
        int8_t a = (int8_t)(*src & 0xff);
        *dst = a;
        dst++;
        src++;
    }
}
#endif

// convert_i64toi8_simd 展开版本
void convert_i64toi8_simd2(int64_t* src, int8_t* dst, size_t size) {
    size_t offset = 0;
    int64_t* end = src + size;
    size_t loop = size / 16;
    static uint8_t mask_data[16] = {0x00, 0x08};
    __m128i mask = _mm_loadu_si128((__m128i const*)mask_data);
    for (size_t i = 0; i < loop; i++) {
        __m128i a = _mm_loadu_si128((__m128i const*)src);
        __m128i b = _mm_loadu_si128((__m128i const*)(src + 2));
        __m128i c = _mm_loadu_si128((__m128i const*)(src + 4));
        __m128i d = _mm_loadu_si128((__m128i const*)(src + 6));
        a = _mm_shuffle_epi8(a, mask);
        b = _mm_shuffle_epi8(b, mask);
        c = _mm_shuffle_epi8(c, mask);
        d = _mm_shuffle_epi8(d, mask);
        a = _mm_unpacklo_epi16(a, b);
        c = _mm_unpacklo_epi16(c, d);
        __m128i x = _mm_unpacklo_epi32(a, c);
        src += 8;

        a = _mm_loadu_si128((__m128i const*)src);
        b = _mm_loadu_si128((__m128i const*)(src + 2));
        c = _mm_loadu_si128((__m128i const*)(src + 4));
        d = _mm_loadu_si128((__m128i const*)(src + 6));
        a = _mm_shuffle_epi8(a, mask);
        b = _mm_shuffle_epi8(b, mask);
        c = _mm_shuffle_epi8(c, mask);
        d = _mm_shuffle_epi8(d, mask);
        a = _mm_unpacklo_epi16(a, b);
        c = _mm_unpacklo_epi16(c, d);
        __m128i y = _mm_unpacklo_epi32(a, c);
        src += 8;

        x = _mm_unpacklo_epi64(x, y);
        _mm_storeu_si128((__m128i*)(dst), x);
        dst += 16;
    }
    while (src < end) {
        int8_t a = (int8_t)(*src & 0xff);
        *dst = a;
        dst++;
        src++;
    }
}

void convert_i64toi8_simd(int64_t* src, int8_t* dst, size_t size) {
    size_t offset = 0;
    int64_t* end = src + size;
    size_t loop = size / 8;
    static uint8_t mask_data[16] = {0x00, 0x08};
    __m128i mask = _mm_loadu_si128((__m128i const*)mask_data);
    for (size_t i = 0; i < loop; i++) {
        __m128i a = _mm_loadu_si128((__m128i const*)src);
        __m128i b = _mm_loadu_si128((__m128i const*)(src + 2));
        __m128i c = _mm_loadu_si128((__m128i const*)(src + 4));
        __m128i d = _mm_loadu_si128((__m128i const*)(src + 6));
        a = _mm_shuffle_epi8(a, mask);
        b = _mm_shuffle_epi8(b, mask);
        c = _mm_shuffle_epi8(c, mask);
        d = _mm_shuffle_epi8(d, mask);
        a = _mm_unpacklo_epi16(a, b);
        c = _mm_unpacklo_epi16(c, d);
        __m128i x = _mm_unpacklo_epi32(a, c);
        _mm_storeu_si64(dst, x);
        src += 8;
        dst += 8;
    }
    while (src < end) {
        int8_t a = (int8_t)(*src & 0xff);
        *dst = a;
        dst++;
        src++;
    }
}

void convert_i64toi8_pack(int64_t* src, int8_t* dst, size_t size) {
    size_t offset = 0;
    int64_t* end = src + size;
    size_t loop = size / 8;
    for (size_t i = 0; i < loop; i++) {
#define REP(x, o) int64_t x = ((*(src + o)) & 0xff) << (o * 8)
        REP(a, 0);
        REP(b, 1);
        REP(c, 2);
        REP(d, 3);
        REP(e, 4);
        REP(f, 5);
        REP(g, 6);
        REP(h, 7);
        int64_t x = a | b | c | d;
        int64_t y = e | f | g | h;
        *((int64_t*)dst) = x | y;
        dst += 8;
        src += 8;
    }
    while (src < end) {
        int8_t a = (int8_t)(*src & 0xff);
        *dst = a;
        dst++;
        src++;
    }
}

const int N = 256;
int64_t* src = nullptr;
int8_t* dst = nullptr;

void make() {
    for (int i = 0; i < N; i++) {
        src[i] = i - 128;
        dst[i] = 0xff;
    }
}
bool check(string name) {
    bool ok = true;
    for (int i = 0; i < N; i++) {
        if (dst[i] != (i - 128)) {
            ok = false;
            break;
        }
    }
    if (!ok) {
        cout << "FAILED: " << name << endl;
    } else {
        cout << "PASSED: " << name << endl;
    }
    return true;
}
int main() {
    src = new int64_t[N];
    dst = new int8_t[N];

    make();
    convert_i64toi8_simd(src, dst, N);
    check("simd");

    make();
    convert_i64toi8_simd2(src, dst, N);
    check("simd2");

    make();
    convert_i64toi8_pack(src, dst, N);
    check("pack");

#if AVX512
    make();
    convert_i64toi8_avx512(src, dst, N);
    check("avx512");
#endif

    delete[] src;
    delete[] dst;
    return 0;
}
