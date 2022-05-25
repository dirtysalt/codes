/* coding:utf-8
 * Copyright (C) dirlt
 */

#include "Common.h"

void Memcopy(char* src, char* dst, size_t sz) {
    // unaligned.
    int i = 0;
    for (; (i + 16) < sz; i += 16) {
        __m128i d = _mm_loadu_si128((__m128i*)(src + i));
        _mm_storeu_si128((__m128i*)(dst + i), d);
    }
    for (; i < sz; i++) {
        dst[i] = src[i];
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
    const int times = 300001;

    char* s = NULL;
    const char* mode = "dense";
    s = GenerateRandomString(N);
    char* dst = new char[N + 1];
    const int sz = N;

    // warmup cache line.
    for (int i = 0; i < 10; i++) {
        Memcopy(s, dst, sz);
    }

    t.start();
    for (int i = 0; i < times; i++) {
        Memcopy(s, dst, sz);
    }
    t.stop();
    printf("Memcopy: mode=%s, sz=%d timer=%lldms\n", mode, sz, t.elapsedMilliseconds());

    t.start();
    for (int i = 0; i < times; i++) {
        std::memcpy(s, dst, sz);
    }
    t.stop();
    printf("std::memcpy: mode=%s, sz=%d, timer=%lldms\n", mode, sz, t.elapsedMilliseconds());

    delete[] s;
    delete[] dst;
}

int main() {
    int sizes[] = {32, 128, 1024, 10240, 20480, 0};
    for (int i = 0; sizes[i]; i++) {
        Bench(sizes[i]);
    }
    return 0;
}
