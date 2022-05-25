/* coding:utf-8
 * Copyright (C) dirlt
 */

// CppApp.cpp : This file contains the 'main' function. Program execution begins
// and ends there.
//

#include <cassert>
#include <chrono>
#include <iostream>

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

class Matrix {
   public:
    int N;
    int** data;
    int* mem;

    Matrix(int n) {
        N = n;
        mem = new int[N * N];

        data = new int*[N];
        for (int i = 0; i < N; i++) {
            data[i] = mem + i * N;
        }
    }
    ~Matrix() {
        delete[] mem;
        delete[] data;
    }

    void Init() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                data[i][j] = i * N + j;
            }
        }
    }
    bool Validate() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (data[i][j] != (j * N + i)) {
                    return false;
                }
            }
        }
        return true;
    }
    void Trans() {
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < i; j++) {
                int x = data[i][j];
                data[i][j] = data[j][i];
                data[j][i] = x;
            }
        }
    }

    void FastTrans(const int stride) {
        for (int i = 1; i < N; i += stride) {
            int toi = min(N, i + stride);
            for (int j = 0; j < i; j += stride) {
                for (int ii = i; ii < toi; ii++) {
                    int toj = min(ii, j + stride);
                    for (int jj = j; jj < toj; jj++) {
                        int x = data[ii][jj];
                        data[ii][jj] = data[jj][ii];
                        data[jj][ii] = x;
                    }
                }
            }
        }
    }

    void Print() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                printf("%d ", data[i][j]);
            }
            printf("\n");
        }
    }
};

void Bench(const int N, bool fast, const int stride) {
    auto t = Timer();
    const int times = 3001;

    auto m = Matrix(N);
    m.Init();
    t.start();
    std::string name;
    if (fast) {
        name = "FAST";
        for (int i = 0; i < times; i++) {
            m.FastTrans(stride);
        }
    } else {
        name = "SLOW";
        for (int i = 0; i < times; i++) {
            m.Trans();
        }
    }
    t.stop();
    auto total = t.elapsedMilliseconds();
    std::cout << "[" << name << ", S=" << stride << "] N = " << N
              << ", took: " << total << "ms, avg " << (total * 1e6) / (N * N)
              << "ns/N \n";
    assert(m.Validate());
}

void Test() {
    auto m = Matrix(10);
    m.Init();
    // m.Print();
    m.FastTrans(6);
    // m.Print();
    assert(m.Validate());
}

int main() {
    Test();
    const int stride = 9;
    int sizes[] = {1010, 1024, 1030, 0};
    for (int i = 0; sizes[i]; i++) {
        Bench(sizes[i], false, stride);
        Bench(sizes[i], true, stride);
    }
    return 0;
}
