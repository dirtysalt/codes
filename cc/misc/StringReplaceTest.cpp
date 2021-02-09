/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cassert>
#include <chrono>
#include <iostream>
#include <immintrin.h>
#include <emmintrin.h>
#include <cstdio>

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


int StringReplace0(char* s, size_t sz, char x, char y) {
    int ans = 0;
    for(size_t i = 0; i<sz;i++) {
        if(s[i] == x) {
            s[i] = y;
            // ans += 1;
        }
    }
    return ans;
}

int StringReplace1(char* s, size_t sz, char x, char y) {
    int ans = 0;
    size_t i = 0;
    __m128i search = _mm_set1_epi8(x);
    __m128i delta = _mm_set1_epi8(y - x);
    // unaligned.
    for(;(i+16)<sz;i+=16) {
        __m128i d = _mm_loadu_si128((__m128i*)(s+i));
        __m128i mask = _mm_cmpeq_epi8(d, search);
        int ret = _mm_movemask_epi8(mask);
        if (ret) {
            __m128i add = _mm_and_si128(mask, delta);
            __m128i res = _mm_add_epi8(add, d);
            _mm_storeu_si128((__m128i*)(s+i), res);
            //            ans += __builtin_popcount(ret);
        }
    }
    for(;i<sz;i++) {
        if(s[i] == x) {
            s[i] = y;
            // ans += 1;
        }
    }
    return ans;
}

char* GenerateRandomStringSparse(int sz) {
    char* s = new char[sz+1];
    for(int i=0;i<sz;i++) {
        s[i] = 'a' + i % 26;
    }
    s[sz] = 0;
    return s;
}


char* GenerateRandomStringDense(int sz) {
    char* s = new char[sz+1];
    for(int i=0;i<sz;i++) {
        s[i] = 'a';
    }
    s[sz] = 0;
    return s;
}

void Bench(const int N, int sparse) {
    auto t = Timer();
    const int times = 30001;

    char *s = NULL;
    const char* mode = NULL;
    if(sparse) {
        s = GenerateRandomStringSparse(N);
        mode = "sparse";
    } else {
        s = GenerateRandomStringDense(N);
        mode = "dense";
    }
    const int sz = N;

    StringReplace0(s, sz, 'b', 'a');
    for(int i=0;i<sz;i++){
        assert(s[i] != 'b');
    }
    StringReplace1(s, sz, 'a', 'b');
    for(int i=0;i<sz;i++){
        assert(s[i] != 'a');
    }
    StringReplace0(s, sz, 'b', 'a');

    int ans0 = 0;
    int ans1 = 0;

    t.start();
    for(int i=0;i<times;i++){
        ans0 = StringReplace0(s, sz, 'a', 'b');
        ans1 = StringReplace0(s, sz, 'b', 'a');
    }
    t.stop();
    printf("Replace0: mode=%s, sz=%d(%d,%d) timer=%lldms\n", mode, sz, ans0, ans1, t.elapsedMilliseconds());


    t.start();
    for(int i=0;i<times;i++){
        ans0 = StringReplace1(s, sz, 'a', 'b');
        ans1 = StringReplace1(s, sz, 'b', 'a');
    }
    t.stop();
    printf("Replace1: mode=%s, sz=%d(%d,%d), timer=%lldms\n", mode, sz, ans0, ans1, t.elapsedMilliseconds());

    delete[] s;
}

int main() {
    int sizes[] = {32, 128, 1024, 10240, 20480, 0};
    for (int i = 0; sizes[i]; i++) {
        Bench(sizes[i], 1);
    }
    for (int i = 0; sizes[i]; i++) {
        Bench(sizes[i], 0);
    }
    return 0;
}
