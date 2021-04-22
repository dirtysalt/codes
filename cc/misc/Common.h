/* coding:utf-8
 * Copyright (C) dirlt
 */

#pragma once

#include <cstdio>
#include <emmintrin.h>
#include <immintrin.h>
#include <chrono>

void p128_hex_u8(__m128i in) {
    alignas(16) uint8_t v[16];
    _mm_store_si128((__m128i*)v, in);
    printf("v16_u8: | %x %x %x %x | %x %x %x %x | %x %x %x %x | %x %x %x %x |\n",
           v[0], v[1],  v[2],  v[3],  v[4],  v[5],  v[6],  v[7],
           v[8], v[9], v[10], v[11], v[12], v[13], v[14], v[15]);
}

void p128_hex_u16(__m128i in) {
    alignas(16) uint16_t v[8];
    _mm_store_si128((__m128i*)v, in);
    printf("v8_u16: %x %x %x %x,  %x %x %x %x\n", v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]);
}

void p128_hex_u32(__m128i in) {
    alignas(16) uint32_t v[4];
    _mm_store_si128((__m128i*)v, in);
    printf("v4_u32: %x %x %x %x\n", v[0], v[1], v[2], v[3]);
}

void p128_hex_u64(__m128i in) {
    alignas(16) unsigned long long v[2];
    _mm_store_si128((__m128i*)v, in);
    printf("v2_u64: %llx %llx\n", v[0], v[1]);
}

void p256_hex_u8(__m256i in) {
    alignas(32) unsigned char v[32];
    _mm256_store_si256((__m256i*)v, in);
    printf("v32_u8: ");
    for(int i=0;i<32;i++) {
        if(i % 8 == 0) printf("|");
        printf("%x ", v[i]);
    }
    printf("|\n");
}

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
