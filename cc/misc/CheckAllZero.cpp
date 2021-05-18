/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <immintrin.h>

#include <condition_variable>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <mutex>
#include <string>
#include <thread>
#include <vector>

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

static bool all_zero_128b(const char* data, size_t size) {
    // assume 128bits.
    __m256i q = _mm256_set1_epi8(0x0);
    const char* i = data;
    const char* ee = data + size;
    for (; i < ee; i += 128) {
        __m256i x0 = _mm256_lddqu_si256(reinterpret_cast<const __m256i*>(i));
        __m256i x1 =
            _mm256_lddqu_si256(reinterpret_cast<const __m256i*>(i + 32));
        __m256i x2 =
            _mm256_lddqu_si256(reinterpret_cast<const __m256i*>(i + 64));
        __m256i x3 =
            _mm256_lddqu_si256(reinterpret_cast<const __m256i*>(i + 96));

        __m256i y0 = _mm256_cmpeq_epi8(x0, q);
        __m256i y1 = _mm256_cmpeq_epi8(x1, q);
        __m256i y2 = _mm256_cmpeq_epi8(x2, q);
        __m256i y3 = _mm256_cmpeq_epi8(x3, q);

        int r0 = _mm256_movemask_epi8(y0);
        int r1 = _mm256_movemask_epi8(y1);
        int r2 = _mm256_movemask_epi8(y2);
        int r3 = _mm256_movemask_epi8(y3);
        int z = r0 & r1 & r2 & r3;
        if (z != 0xffffffff) {
            return false;
        }
    }
    return true;
}

static bool all_zero_32b(const char* data, size_t size) {
    // assume 32b
    __m256i q = _mm256_set1_epi8(0x0);
    const char* i = data;
    const char* ee = data + size;
    for (; i < ee; i += 32) {
        __m256i x0 = _mm256_lddqu_si256(reinterpret_cast<const __m256i*>(i));
        __m256i y0 = _mm256_cmpeq_epi8(x0, q);
        int r0 = _mm256_movemask_epi8(y0);
        if (r0 != 0xffffffff) {
            return false;
        }
    }
    return true;
}

static bool all_zero(const char* data, size_t size) {
    const char* end = data + size;
    const char* aligned_end = data + (size / 16) * 16;
    for (; data < aligned_end; data += 16) {
        const __int128 value = *reinterpret_cast<const __int128*>(data);
        if (value != 0) {
            return false;
        }
    }
    if ((data + 8) < end) {
        const int64_t value = *reinterpret_cast<const int64_t*>(data);
        if (value != 0) {
            return false;
        }
        data += 8;
    }
    for (; data < end; data++) {
        if (*data != 0) {
            return false;
        }
    }
    return true;
}

static bool all_zero2(const char* data, size_t size) {
    if (size >= 1024) {
        size_t az = size / 1024 * 1024;
        if (!all_zero_128b(data, az)) return false;
        data += az;
        size -= az;
    }

    if (size >= 256) {
        size_t az = size / 256 * 256;
        if (!all_zero_32b(data, az)) return false;
        data += az;
        size -= az;
    }

    return all_zero(data, size);
}

void test(char* data, size_t size) {
    const int N = 1024 * 1024;
    int mem = 0;
    Timer timer;
    memset(data, 0, size);

    cout << "========== "
         << "size = " << size << " ==========" << endl;
    timer.start();
    mem = 0;
    for (int i = 0; i < N; i++) {
        data[size - 1] = 0;
        bool res = all_zero(data, size);
        mem += res;
    }
    for (int i = 0; i < N; i++) {
        data[size - 1] = 1;
        bool res = all_zero(data, size);
        mem += res;
    }
    timer.stop();
    cout << "all_zero: time = " << timer.elapsedMilliseconds()
         << "ms, mem = " << mem << endl;

    timer.start();
    mem = 0;
    for (int i = 0; i < N; i++) {
        data[size - 1] = 0;
        bool res = all_zero2(data, size);
        mem += res;
    }
    for (int i = 0; i < N; i++) {
        data[size - 1] = 1;
        bool res = all_zero2(data, size);
        mem += res;
    }
    timer.stop();
    cout << "all_zero2: time = " << timer.elapsedMilliseconds()
         << "ms, mem = " << mem << endl;

    mem = 0;
    timer.start();
    for (int i = 0; i < N; i++) {
        data[size - 1] = 0;
        bool res = (memchr(data, 0x1, size) != NULL);
        mem += res;
    }
    for (int i = 0; i < N; i++) {
        data[size - 1] = 1;
        bool res = (memchr(data, 0x1, size) != NULL);
        mem += res;
    }
    timer.stop();
    cout << "memchr: time = " << timer.elapsedMilliseconds()
         << "ms, mem = " << mem << endl;
}

int main() {
    const int size = 1024 * 1024;
    char* data = new char[size];

    test(data, 15);
    test(data, 128);
    test(data, 1024);
    test(data, 4096);
    test(data, 10240);

    delete[] data;
    return 0;
}
