/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cassert>
#include <chrono>
#include <iostream>
#include <immintrin.h>
#include <emmintrin.h>
#include <cstdio>
#include <cstring>

#define min(a, b) ((a) < (b) ? (a) : (b))

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

void Memcopy(char* src, char* dst, size_t sz) {
    // unaligned.
    int i = 0;
    for(;(i+16)<sz;i+=16) {
        __m128i d = _mm_loadu_si128((__m128i*)(src+i));
        _mm_storeu_si128((__m128i*)(dst + i), d);
    }
    for(;i<sz;i++) {
        dst[i] =src[i];
    }
}

char* GenerateRandomString(int sz) {
    char* s = new char[sz+1];
    for(int i=0;i<sz;i++) {
        s[i] = 'a';
    }
    s[sz] = 0;
    return s;
}

void Bench(const int N) {
    auto t = Timer();
    const int times = 300001;

    char *s = NULL;
    const char* mode = "dense";
    s = GenerateRandomString(N);
    char* dst = new char[N+1];
    const int sz = N;

    // warmup cache line.
    for(int i=0;i<10;i++){
        Memcopy(s, dst, sz);
    }

    t.start();
    for(int i=0;i<times;i++){
        Memcopy(s, dst, sz);
    }
    t.stop();
    printf("Memcopy: mode=%s, sz=%d timer=%lldms\n", mode, sz, t.elapsedMilliseconds());


    t.start();
    for(int i=0;i<times;i++){
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
