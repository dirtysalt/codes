/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <memory>
#include <vector>
#include <functional>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <chrono>
#include <emmintrin.h>
#include <immintrin.h>

using namespace std;

class Timer {
   public:
    void start() {
        m_StartTime = std::chrono::system_clock::now();
        m_bRunning = true;
    }

    void stop() {
        m_EndTime = std::chrono::system_clock::now();
        m_bRunning = false;
    }

    long long elapsedMilliseconds() {
        std::chrono::time_point<std::chrono::system_clock> endTime;

        if (m_bRunning) {
            endTime = std::chrono::system_clock::now();
        } else {
            endTime = m_EndTime;
        }

        return std::chrono::duration_cast<std::chrono::milliseconds>(
                   endTime - m_StartTime)
            .count();
    }

    double elapsedSeconds() { return elapsedMilliseconds() / 1000.0; }

   private:
    std::chrono::time_point<std::chrono::system_clock> m_StartTime;
    std::chrono::time_point<std::chrono::system_clock> m_EndTime;
    bool m_bRunning = false;
};

#define RE __restrict__

#ifdef AVX512
void convert_i64toi8_simd_avx512(int64_t* RE src, int8_t * RE dst, size_t size) {
    static uint8_t mask_data[64] = {
        0x00, 0x08, 0x10, 0x18, 0x20, 0x28, 0x30, 0x38,
    };
    size_t offset = 0;
    int64_t* end = src + size;
    size_t loop = size / 8;
    __m512i mask = _mm512_loadu_epi8(mask_data);
    for(size_t i = 0; i < loop ; i++) {
        __m512i a = _mm512_loadu_epi8(src);
        __m512i b = _mm512_permutex2var_epi8(a, mask, a);
        __m128i x = _mm512_castsi512_si128(b);
        _mm_storeu_si64(dst, x);
        dst += 8;
        src += 8;
    }
    while(src < end) {
        int8_t a = (int8_t)(*src & 0xff);
        *dst = a;
        dst++;
        src++;
    }
}
#endif

void convert_i64toi8_simd(int64_t* RE src, int8_t * RE dst, size_t size) {
    size_t offset = 0;
    int64_t* end = src + size;
    size_t loop = size / 8;
    static uint8_t mask_data[16] = {
        0x00, 0x08
    };
    __m128i mask = _mm_loadu_si128((__m128i const*)mask_data);
    for(size_t i = 0; i < loop ; i++) {
        __m128i a = _mm_lddqu_si128((__m128i const*)src);
        __m128i b = _mm_lddqu_si128((__m128i const*)(src+2));
        __m128i c = _mm_lddqu_si128((__m128i const*)(src+4));
        __m128i d = _mm_lddqu_si128((__m128i const*)(src+6));
        a = _mm_shuffle_epi8(a, mask);
        b = _mm_shuffle_epi8(b, mask);
        c = _mm_shuffle_epi8(c, mask);
        d = _mm_shuffle_epi8(d, mask);
        __m128i e = _mm_unpacklo_epi16(a, b);
        __m128i f = _mm_unpacklo_epi16(c, d);
        __m128i g = _mm_unpacklo_epi32(e, f);
        _mm_storeu_si64(dst, g);
        dst += 8;
        src += 8;
    }
    while(src < end) {
        int8_t a = (int8_t)(*src & 0xff);
        *dst = a;
        dst++;
        src++;
    }
}

void convert_i64toi8_simd2(int64_t* RE src, int8_t * RE dst, size_t size) {
    size_t offset = 0;
    int64_t* end = src + size;
    size_t loop = size / 16;
    static uint8_t mask_data[16] = {
        0x00, 0x08
    };
    __m128i mask = _mm_loadu_si128((__m128i const*)mask_data);
    for(size_t i = 0; i < loop ; i++) {
        __m128i a = _mm_loadu_si128((__m128i const*)src);
        __m128i b = _mm_loadu_si128((__m128i const*)(src+2));
        __m128i c = _mm_loadu_si128((__m128i const*)(src+4));
        __m128i d = _mm_loadu_si128((__m128i const*)(src+6));
        a = _mm_shuffle_epi8(a, mask);
        b = _mm_shuffle_epi8(b, mask);
        c = _mm_shuffle_epi8(c, mask);
        d = _mm_shuffle_epi8(d, mask);
        a = _mm_unpacklo_epi16(a, b);
        c = _mm_unpacklo_epi16(c, d);
        __m128i x = _mm_unpacklo_epi32(a, c);
        src += 8;

        a = _mm_loadu_si128((__m128i const*)src);
        b = _mm_loadu_si128((__m128i const*)(src+2));
        c = _mm_loadu_si128((__m128i const*)(src+4));
        d = _mm_loadu_si128((__m128i const*)(src+6));
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
    while(src < end) {
        int8_t a = (int8_t)(*src & 0xff);
        *dst = a;
        dst++;
        src++;
    }
}

void convert_i64toi8_pack(int64_t* RE src, int8_t * RE dst, size_t size) {
    size_t offset = 0;
    int64_t* end = src + size;
    size_t loop = size / 8;
    for(size_t i = 0; i < loop ; i++) {
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
    while(src < end) {
        int8_t a = (int8_t)(*src & 0xff);
        *dst = a;
        dst++;
        src++;
    }
}

void convert_i64toi8_native(int64_t* RE src, int8_t * RE dst, size_t size) {
    for(size_t i = 0; i < size ; i++) {
        dst[i] = static_cast<int8_t>(src[i]);
    }
}

void Bench() {
    const int times = 3001;
    const int N = 1024000;
    int64_t* src = new int64_t[N];
    int8_t* dst = new int8_t[N];
    for(int i=0;i<N;i++) {
        src[i] = (i+1) * 100;
    }

    auto t = Timer();
    long long ms = 0;

    // warmup.
    for(int i=0;i<10;i++) {
        convert_i64toi8_native(src, dst,N);
    }

    t.start();
    for(int i=0;i<times;i++) {
        convert_i64toi8_native(src, dst,N);
    }
    t.stop();
    ms = t.elapsedMilliseconds();
    cout << "native version: N = " << N << ", total = " << ms << ", avg = " << (ms * 1e6) / N / times << "ns(per item)" << endl;

#ifdef AVX512
    t.start();
    for(int i=0;i<times;i++) {
        convert_i64toi8_simd_avx512(src, dst,N);
    }
    t.stop();
    ms = t.elapsedMilliseconds();
    cout << "simd avx512 version: N = " << N << ", total = " << ms << ", avg = " << (ms * 1e6) / N / times << "ns(per item)" << endl;
#endif

    t.start();
    for(int i=0;i<times;i++) {
        convert_i64toi8_simd(src, dst,N);
    }
    t.stop();
    ms = t.elapsedMilliseconds();
    cout << "simd version: N = " << N << ", total = " << ms << ", avg = " << (ms * 1e6) / N / times << "ns(per item)" << endl;

    t.start();
    for(int i=0;i<times;i++) {
        convert_i64toi8_simd2(src, dst,N);
    }
    t.stop();
    ms = t.elapsedMilliseconds();
    cout << "simd2 version: N = " << N << ", total = " << ms << ", avg = " << (ms * 1e6) / N / times << "ns(per item)" << endl;

    t.start();
    for(int i=0;i<times;i++) {
        convert_i64toi8_pack(src, dst,N);
    }
    t.stop();
    ms = t.elapsedMilliseconds();
    cout << "pack version: N = " << N << ", total = " << ms << ", avg = " << (ms * 1e6) / N / times << "ns(per item)" << endl;
}

int main() {
    Bench();
    return 0;
}
