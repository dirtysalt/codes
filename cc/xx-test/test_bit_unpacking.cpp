/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cassert>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <thread>
#include <vector>

using namespace std;

void bit_unpack_tail(const uint8_t* in, int fb, int64_t* data, int nums) {
    if (nums == 0) return;
    int64_t t = 0;
    uint8_t c = 0;
    int cb = 0;
    for (int i = 0; i < nums; i++) {
        int bits = fb;
        t = 0;
        while (bits) {
            if (cb == 0) {
                c = (*in++);
                cb = 8;
            }
            int lb = std::min(cb, bits);
            t = (t << lb) | ((c >> (cb - lb)) & ((1 << lb) - 1));
            bits -= lb;
            cb -= lb;
        }
        *data = t;
        data++;
    }
}

#include "bit_unpack_gen.inc"

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

        return std::chrono::duration_cast<std::chrono::milliseconds>(endTime - m_StartTime).count();
    }

    double elapsedSeconds() { return elapsedMilliseconds() / 1000.0; }

private:
    std::chrono::time_point<std::chrono::system_clock> m_StartTime;
    std::chrono::time_point<std::chrono::system_clock> m_EndTime;
    bool m_bRunning = false;
};

void test(int fb, const uint8_t* input, int64_t* output, int num) {
    Timer t;
    const int T = 100;

    int64_t* temp = new int64_t[num];
    // warmup cache?
    bit_unpack(input, fb, output, num);
    bit_unpack_tail(input, fb, temp, num);
    for (int i = 0; i < num; i++) {
        assert(output[i] == temp[i]);
    }
    delete[] temp;

    t.start();
    for (int i = 0; i < T; i++) {
        bit_unpack(input, fb, output, num);
    }
    t.stop();
    double ms1 = t.elapsedMilliseconds();

    t.start();
    for (int i = 0; i < T; i++) {
        bit_unpack_tail(input, fb, output, num);
    }
    t.stop();
    double ms2 = t.elapsedMilliseconds();

    // 处理单个元素的平均时间
    cout << "unpack fb: " << fb << ". fast = " << ms1 << " ms, avg = " << (ms1 * 1000000) / (T * num) << " ns. "
         << "tail = " << ms2 << " ms, avg = " << (ms2 * 1000000) / (T * num) << " ns. speedup = " << ms2 * 1.0 / ms1
         << endl;
}

int main() {
    Timer t;
    const int T = 100;
    const int N = 1024 * 1024;

    uint8_t* input = new uint8_t[N * 64];
    int64_t* output = new int64_t[N * 64];
    memset(input, 0x73, N * 64);

    vector<int> fbs = {1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16,
                       17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 30, 32, 40, 48, 56, 64};
    for (int fb : fbs) {
        test(fb, input, output, N);
    }
    delete[] input;
    delete[] output;
    return 0;
}
