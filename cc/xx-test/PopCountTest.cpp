/* coding:utf-8
 * Copyright (C) dirlt
 */

#include "Common.h"

std::vector<uint32_t> GenRandomInts(int N) {
    srand(time(NULL)); // Initialization, should only be called once.
    std::vector<uint32_t> ans(N);
    int MOD = 1 << 30;
    for (int i = 0; i < N; i++) {
        int r = rand() % MOD; // Returns a pseudo-random integer between 0 and RAND_MAX.
        ans[i] = (uint32_t)r;
    }
    return ans;
}

/*
data = []
for i in range(0,256,8):
    value = 0
    for j in reversed(range(8)):
        value = (value << 4) | popcount(i+j)
    data.append(value)
*/

uint32_t TABLE[] = {841031952,  1127363105, 1127363105, 1413694258, 1127363105, 1413694258, 1413694258, 1700025411,
                    1127363105, 1413694258, 1413694258, 1700025411, 1413694258, 1700025411, 1700025411, 1986356564,
                    1127363105, 1413694258, 1413694258, 1700025411, 1413694258, 1700025411, 1700025411, 1986356564,
                    1413694258, 1700025411, 1700025411, 1986356564, 1700025411, 1986356564, 1986356564, 2272687717};

inline uint32_t GET8(unsigned char x) {
    return (TABLE[x >> 3] >> ((x & 0x7) << 2)) & 0xf;
}

uint32_t popcount01(uint32_t x) {
    return GET8(x & 0xff) + GET8((x >> 8) & 0xff) + GET8((x >> 16) & 0xff) + GET8((x >> 24) & 0xff);
}

uint32_t popcount11(uint32_t x) {
    uint32_t ans = 0;
    // while (x) {
    //     ans += x & 0x1;
    //     x = x >> 1;
    // }
    while (x) {
        ans += 1;
        x = x & (x - 1);
    }
    return ans;
}

uint32_t popcount21(uint32_t x) {
    x = (x & 0x55555555) + ((x >> 1) & 0x55555555);
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
    x = (x & 0x0f0f0f0f) + ((x >> 4) & 0x0f0f0f0f);
    x = (x & 0x00ff00ff) + ((x >> 8) & 0x00ff00ff);
    x = (x & 0x0000ffff) + ((x >> 16) & 0x0000ffff);
    return x;
}

uint32_t _popcount21(uint32_t x) {
    x = (x & 0x55555555) + ((x & 0xaaaaaaaa) >> 1);
    x = (x & 0x33333333) + ((x & 0xcccccccc) >> 2);
    x = (x & 0x0f0f0f0f) + ((x & 0xf0f0f0f0) >> 4);
    x = (x & 0x00ff00ff) + ((x & 0xff00ff00) >> 8);
    x = (x & 0x0000ffff) + ((x & 0xffff0000) >> 16);
    return x;
}

uint32_t __popcount21(uint32_t x) {
    // 这里可以假设分别是0，1的情况
    // 如果是11的话，那么11-01 = 10 = 2
    // 10 - 01 = 01 = 1
    // 0x 这个就是 x
    x = x - ((x >> 1) & 0x55555555);
    x = (x & 0x33333333) + ((x & 0xcccccccc) >> 2);
    x = (x + (x >> 4)) & 0x0f0f0f0f;
    x = x + (x >> 8);
    x = x + (x >> 16);
    // 最后一次 low bits 最多 16, 就是 10000
    // high bits 最多 16，也是 10000
    // 所以最多就是 100000
    return x & 0x3f;
}

uint32_t popcount22(uint32_t x, uint32_t y) {
    x = (x & 0x55555555) + ((x & 0xaaaaaaaa) >> 1);
    x = (x & 0x33333333) + ((x & 0xcccccccc) >> 2);

    y = (y & 0x55555555) + ((y & 0xaaaaaaaa) >> 1);
    y = (y & 0x33333333) + ((y & 0xcccccccc) >> 2);

    x += y;
    x = (x & 0x0f0f0f0f) + ((x & 0xf0f0f0f0) >> 4);
    x = (x & 0x00ff00ff) + ((x & 0xff00ff00) >> 8);
    x = (x & 0x0000ffff) + ((x & 0xffff0000) >> 16);
    return x;
}

// pop(x) - pop(y) = pop(x) - (32 - pop(~y)) = pop(x) + pop(y) - 32
int popDiff(uint32_t x, uint32_t y) {
    x = x - ((x >> 1) & 0x55555555);
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
    y = ~y;
    y = y - ((y >> 1) & 0x55555555);
    y = (y & 0x33333333) + ((y >> 2) & 0x33333333);

    x += y;
    x = (x + (x >> 4)) & 0x0f0f0f0f;
    x = (x + (x >> 8));
    x = (x + (x >> 16));
    return x & 0x0000007f - 32;
}

int popCompare(uint32_t xp, uint32_t yp) {
    unsigned x, y;
    x = xp & ~yp;
    y = yp & ~xp;
    while (1) {
        // if y == 0 then 0
        // else < 0
        if (x == 0) return y | -y;
        if (y == 0) return 1;
        x = x & (x - 1); // clear lsb
        y = y & (y - 1);
    }
}

uint32_t popcount24(uint32_t x, uint32_t y, uint32_t a, uint32_t b) {
    x = (x & 0x55555555) + ((x & 0xaaaaaaaa) >> 1);
    y = (y & 0x55555555) + ((y & 0xaaaaaaaa) >> 1);
    a = (a & 0x55555555) + ((a & 0xaaaaaaaa) >> 1);
    b = (b & 0x55555555) + ((b & 0xaaaaaaaa) >> 1);
    x = (x & 0x33333333) + ((x & 0xcccccccc) >> 2);
    y = (y & 0x33333333) + ((y & 0xcccccccc) >> 2);
    a = (a & 0x33333333) + ((a & 0xcccccccc) >> 2);
    b = (b & 0x33333333) + ((b & 0xcccccccc) >> 2);

    x += y;
    a += b;

    x = (x & 0x0f0f0f0f) + ((x & 0xf0f0f0f0) >> 4);
    a = (a & 0x0f0f0f0f) + ((a & 0xf0f0f0f0) >> 4);

    x += a;
    x = (x & 0x00ff00ff) + ((x & 0xff00ff00) >> 8);
    x = (x & 0x0000ffff) + ((x & 0xffff0000) >> 16);
    return x;
}

#define FORI(i, t) for (size_t i = 0; i < t; i++)
#define FORV(i, vec, step) for (size_t i = 0; i < vec.size(); i += step)

#ifdef USE_AVX512_POPCNT
// don't use it. I don't have any cpu support avx512 vpopcnt dq.
// https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html
// g++ mm.cpp -g -W -Wall -mavx512f -mavx512vpopcntdq
uint32_t avx512_vpopcnt(const uint32_t* data, size_t size) {
    uint32_t ans = 0;
    uint64_t start = (uint64_t)data;
    if ((start % 64) != 0) {
        size_t rem = (start % 64) / 4;
        start = (start + 63) / 64 * 64;
        size -= rem;
        FORI(i, rem) ans += popcount21(data[i]);
    }

    const uint8_t* ptr = (uint8_t*)start;
    const uint8_t* end = ptr + size;
    const size_t chunks = size / 64;

    // count using AVX512 registers
    __m512i accumulator = _mm512_setzero_si512();
    for (size_t i = 0; i < chunks; i++, ptr += 64) {
        // Note: a short chain of dependencies, likely unrolling will be needed.
        const __m512i v = _mm512_loadu_si512((const __m512i*)ptr);
        const __m512i p = _mm512_popcnt_epi64(v);

        accumulator = _mm512_add_epi64(accumulator, p);
    }

    // horizontal sum of a register
    uint64_t tmp[8] __attribute__((aligned(64)));
    _mm512_store_si512((__m512i*)tmp, accumulator);

    for (size_t i = 0; i < 8; i++) {
        ans += (uint32_t)tmp[i];
    }

    // popcount the tail
    while (ptr + 4 < end) {
        ans += popcount21(*(uint32_t*)(ptr));
        ptr += 4;
    }

    return ans;
}
#endif

void Bench(std::vector<uint32_t> values, int level) {
    Timer t = Timer();
    const int times = 30001;
    const uint32_t N = values.size();
    assert(N % 4 == 0);
    std::string name = "level";
    name += std::to_string(level);

    t.start();
    uint32_t ans = 0;
    if (level == -2) {
        FORI(k, times) {
            FORV(i, values, 1) {
                uint32_t t = __builtin_popcount(values[i]);
                ans += t;
            }
        }
    } else if (level == -1) {
        FORI(k, times) {
            FORV(i, values, 1) {
                uint32_t t = popcount01(values[i]);
                ans += t;
            }
        }
    } else if (level == 0) {
        FORI(k, times) {
            FORV(i, values, 1) {
                uint32_t t = popcount11(values[i]);
                ans += t;
            }
        }
    } else if (level == 1) {
        FORI(k, times) {
            FORV(i, values, 1) {
                uint32_t t = popcount21(values[i]);
                ans += t;
            }
        }
    } else if (level == 2) {
        FORI(k, times) {
            FORV(i, values, 2) {
                uint32_t t = popcount22(values[i], values[i + 1]);
                ans += t;
            }
        }
    } else if (level == 4) {
        FORI(k, times) {
            FORV(i, values, 4) {
                uint32_t t = popcount24(values[i], values[i + 1], values[i + 2], values[i + 3]);
                ans += t;
            }
        }
    }
#ifdef USE_AVX512_POPCNT
    else if (level == 8) {
        const uint32_t* data = values.data();
        FORI(k, times) { ans += avx512_vpopcnt(data, values.size()); }
    }
#endif

    t.stop();
    double total = t.elapsedMilliseconds();
    std::cout << "[" << name << "] N = " << N << ", took: " << total << "ms, avg " << (total * 1e3) / N
              << "ns/N, ans = " << ans << "\n";
}

void Test() {
    std::vector<uint32_t> values = GenRandomInts(100);

    for (size_t i = 0; i < values.size(); i++) {
        uint32_t x = values[i];
        uint32_t a = popcount11(x);
        uint32_t b = popcount21(x);
        printf("x = %u(0x%X), a = %u, b = %u\n", x, x, a, b);
    }

    {
        uint32_t tta = 0, ttb = 0, ttc = 0;
        for (size_t i = 0; i < values.size(); i++) {
            uint32_t x = values[i];
            uint32_t a = popcount21(x);
            tta += a;
        }
        for (size_t i = 0; i < values.size(); i += 2) {
            uint32_t b = popcount22(values[i], values[i + 1]);
            ttb += b;
        }
        for (size_t i = 0; i < values.size(); i += 4) {
            uint32_t c = popcount24(values[i], values[i + 1], values[i + 2], values[i + 3]);
            ttc += c;
        }
        printf("tta = %u, ttb = %u, ttc = %u\n", tta, ttb, ttc);
    }

    return;
}

int main() {
    // Test();
    const int N = 1000;
    std::vector<uint32_t> values = GenRandomInts(N);
    const int levels[] = {-2, -1, 0, 1, 2, 4};
    const int nums = sizeof(levels) / sizeof(levels[0]);
    for (int i = 0; i < nums; i++) {
        Bench(values, levels[i]);
    }
    return 0;
}
