/* coding:utf-8
 * Copyright (C) dirlt
 */

// 对比几种线性搜索的效率
// 这个问题来自于编程珠玑

#include <cassert>
#include <chrono>
#include <cstdio>
#include <cstdlib>
#include <iostream>

int search1(int* x, int n, int t) {
    for (int i = 0; i < n; i++) {
        if (x[i] == t) {
            return i;
        }
    }
    return -1;
}

int search11(int* x, int n, int t) {
    for (int i = 0;; i += 8) {
#define COMP(d)                             \
    if (((i + d) < n) && (x[i + d] == t)) { \
        i += d;                             \
        return i;                           \
    }
        COMP(0);
        COMP(1);
        COMP(2);
        COMP(3);
        COMP(4);
        COMP(5);
        COMP(6);
        COMP(7);
#undef COMP
    }
    return -1;
}

// 相比search1而言，增加sentinel. 因为我们确定最终肯定会匹配上
// 所以每次循环期间都可以少一次比较
int search2(int* x, int n, int t) {
    int tmp = x[n];
    x[n] = t;
    int i = 0;
    for (i = 0;; i++) {
        if (x[i] == t) {
            break;
        }
    }
    x[n] = tmp;
    if (i == n) {
        return -1;
    }
    return i;
}

// 和search2相比就是把循环展开，但是从指令数量上看并没有减少
// 这里不好解释为什么循环展开要效率更高。可能是因为CPU可以进行推测执行来提高并行度或者是数据依赖被解开了（数组里面8个内容是可以并行访问的）。
// 这种展开没有减少指令数，分支对比数，对分支预测似乎也没有改善。
// 要是想继续什么了解指令优化，还是需要有相应的CPU工具，而不能只是胡乱猜测。

int search21(int* x, int n, int t) {
    int tmp = x[n];
    x[n] = t;
    int i = 0;
    for (i = 0;; i += 8) {
#define COMP(d)          \
    if (x[i + d] == t) { \
        i += d;          \
        break;           \
    }
        COMP(0);
        COMP(1);
        COMP(2);
        COMP(3);
        COMP(4);
        COMP(5);
        COMP(6);
        COMP(7);
    }
#undef COMP
    x[n] = tmp;
    if (i == n) {
        return -1;
    }
    return i;
}

int search22(int* x, int n, int t) {
    int tmp = x[n];
    x[n] = t;
    int i = 0;
    for (i = 0;; i += 16) {
#define COMP(d)          \
    if (x[i + d] == t) { \
        i += d;          \
        break;           \
    }
        COMP(0);
        COMP(1);
        COMP(2);
        COMP(3);
        COMP(4);
        COMP(5);
        COMP(6);
        COMP(7);
        COMP(8);
        COMP(9);
        COMP(10);
        COMP(11);
        COMP(12);
        COMP(13);
        COMP(14);
        COMP(15);
#undef COMP
    }
    x[n] = tmp;
    if (i == n) {
        return -1;
    }
    return i;
}

void measure(int* x, int n, int t, int (*fn)(int*, int, int), const char* fn_name) {
    auto t_start = std::chrono::high_resolution_clock::now();
    int res = 0;
    for (int i = 0; i < 100; i++) {
        int v = fn(x, n, t);
        res += v; // 确保-O2不会被优化掉
    }
    auto t_end = std::chrono::high_resolution_clock::now();

    std::cout << "[" << fn_name
              << "]Wall clock time passed: " << std::chrono::duration<double, std::milli>(t_end - t_start).count()
              << " ms\n";
    assert(res == (n - 1) * 100);
}

int main() {
    int n = 1000000;
    int* x = new int[n + 1];
    int t = 0x1234567;
    for (int i = 0; i < n; i++) {
        while (1) {
            int value = rand();
            if (value != t) {
                x[i] = value;
                break;
            }
        }
    }
    x[n - 1] = t;

    measure(x, n, t, search1, "  search1");
    measure(x, n, t, search11, " search11");
    measure(x, n, t, search2, "  search2");
    measure(x, n, t, search21, " search21");
    measure(x, n, t, search22, " search22");

    delete[] x;
    return 0;
}
