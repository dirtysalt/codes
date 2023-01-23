/* coding:utf-8
 * Copyright (C) dirlt
 */

#include "Common.h"

void StringUpper0(char* s, size_t sz) {
    for (size_t i = 0; i < sz; i++) {
        if (s[i] >= 97 && s[i] <= 122) {
            s[i] -= 32;
        }
    }
}

void StringLower0(char* s, size_t sz) {
    for (size_t i = 0; i < sz; i++) {
        if (s[i] >= 65 && s[i] <= 90) {
            s[i] += 32;
        }
    }
}

void StringLower1(char* s, size_t sz) {
    size_t i = 0;
    __m128i a = _mm_set1_epi8(64);
    __m128i z = _mm_set1_epi8(91);
    __m128i delta = _mm_set1_epi8(32);
    // unaligned.
    for (; (i + 16) < sz; i += 16) {
        __m128i d = _mm_loadu_si128((__m128i*)(s + i));
        __m128i x = _mm_cmpgt_epi8(d, a);
        __m128i y = _mm_cmpgt_epi8(z, d);
        __m128i z = _mm_and_si128(x, y);
        __m128i z2 = _mm_and_si128(z, delta);
        __m128i res = _mm_add_epi8(d, z2);
        _mm_storeu_si128((__m128i*)(s + i), res);
    }
    for (; i < sz; i++) {
        if (s[i] >= 65 && s[i] <= 90) {
            s[i] += 32;
        }
    }
}

void StringUpper1(char* s, size_t sz) {
    size_t i = 0;
    __m128i a = _mm_set1_epi8(96);
    __m128i z = _mm_set1_epi8(123);
    __m128i delta = _mm_set1_epi8(32);
    // unaligned.
    for (; (i + 16) < sz; i += 16) {
        __m128i d = _mm_loadu_si128((__m128i*)(s + i));
        __m128i x = _mm_cmpgt_epi8(d, a);
        __m128i y = _mm_cmpgt_epi8(z, d);
        __m128i z = _mm_and_si128(x, y);
        __m128i z2 = _mm_and_si128(z, delta);
        __m128i res = _mm_sub_epi8(d, z2);
        _mm_storeu_si128((__m128i*)(s + i), res);
    }
    for (; i < sz; i++) {
        if (s[i] >= 97 && s[i] <= 122) {
            s[i] -= 32;
        }
    }
}

char* GenerateRandomString(int sz) {
    char* s = new char[sz + 1];
    for (int i = 0; i < sz; i++) {
        s[i] = 'a';
    }
    s[sz] = 0;
    return s;
}

void Bench(const int N) {
    auto t = Timer();
    const int times = 30001;

    char* s = NULL;
    const char* mode = "dense";
    s = GenerateRandomString(N);
    const int sz = N;

    StringLower0(s, sz);
    for (int i = 0; i < sz; i++) {
        assert(s[i] == 'a');
    }
    StringUpper0(s, sz);
    for (int i = 0; i < sz; i++) {
        assert(s[i] == 'A');
    }
    StringLower1(s, sz);
    for (int i = 0; i < sz; i++) {
        assert(s[i] == 'a');
    }
    StringUpper1(s, sz);
    for (int i = 0; i < sz; i++) {
        assert(s[i] == 'A');
    }

    t.start();
    for (int i = 0; i < times; i++) {
        StringLower0(s, sz);
        StringUpper0(s, sz);
    }
    t.stop();
    printf("X0: mode=%s, sz=%d timer=%lldms\n", mode, sz, t.elapsedMilliseconds());

    t.start();
    for (int i = 0; i < times; i++) {
        StringLower1(s, sz);
        StringUpper1(s, sz);
    }
    t.stop();
    printf("X1: mode=%s, sz=%d, timer=%lldms\n", mode, sz, t.elapsedMilliseconds());

    delete[] s;
}

int main() {
    int sizes[] = {32, 128, 1024, 10240, 20480, 0};
    for (int i = 0; sizes[i]; i++) {
        Bench(sizes[i]);
    }
    return 0;
}
