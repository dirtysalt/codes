/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <sys/mman.h>
#include <unistd.h>

#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

// #define _GNU_SOURCE /* See feature_test_macros(7) */
#include <fcntl.h>

#ifdef __AVX2__
#include <immintrin.h>
#include <xmmintrin.h>
#endif

// ssize_t vmsplice(int fd, const struct iovec* iov, size_t nr_segs, unsigned int flags);

inline int itoa(char* end, int x) {
    char* p = end;
    while (x) {
        *p = x % 10 + '0';
        p--;
        x /= 10;
    }
    return end - p;
}

void naive_fizzbuzz(const uint64_t n) {
    for (uint64_t i = 1; i < n; i += 1) {
        if ((i % 3 == 0) && (i % 5 == 0)) {
            printf("FizzBuzz\n");
        } else if (i % 3 == 0) {
            printf("Fizz\n");
        } else if (i % 5 == 0) {
            printf("Buzz\n");
        } else {
            printf("%llu\n", i);
        }
    }
}

#define RE __restrict__

template <int c>
char* op(char* RE buf, const char* RE p) {
    if constexpr (c > 8 && c <= 16) {
        memcpy(buf, p, 16);
        buf += c;
        return buf;
    }
    constexpr int x = (c + 3) / 4 * 4;
    memcpy(buf, p, x);
    buf += c;
    return buf;
}

#define MC(x, c) buf = op<c>(buf, x)

inline char* add10(char* end) {
    char* p = end;
    while (*p == '9') {
        *p = '0';
        p--;
    }
    *p = *p + 1;
    return p;
}

inline char* add30(char* end) {
    char* p = end;
    if (*p < '7') {
        *p = *p + 3;
        return p;
    }
    *p -= 7;
    p--;
    while (*p == '9') {
        *p = '0';
        p--;
    }
    *p = *p + 1;
    return p;
}

struct DigitContext {
    static constexpr int MAXDIGIT = 20;
    static constexpr int DIGITBUF = MAXDIGIT + 2;

    char digitbuf[DIGITBUF + 8];
    char* begin;
    char* end;

    void init() {
        memset(digitbuf, '0', sizeof(digitbuf));
        end = digitbuf + DIGITBUF;
        begin = end;
    }

    void initfrom(uint64_t x) {
        x = x / 10;
        while (x) {
            *(begin--) += x % 10;
            x = x / 10;
        }
        begin++;
    }

    inline void next() { begin = std::min(begin, add10(end)); }
    inline void next3() { begin = std::min(begin, add30(end)); }

    inline int digit() { return end - begin + 1; }
};
static_assert(sizeof(DigitContext) <= 64);
alignas(64) DigitContext digitctx[3];

template <int digit>
char* output0(char* RE buf, const char* RE pp) {
    // 11   12   13    14    15        16   17   18   19  20    21
    // 1    fizz  3    4     fizzbuzz  6    7    fizz  9  Buzz Fizz
    MC(pp, digit);
    MC("1\nFizz\n0", 7);

    MC(pp, digit);
    MC("3\n00", 2);
    MC(pp, digit);
    MC("4\nFizzBuzz\n000000", 11);

    MC(pp, digit);
    MC("6\n00", 2);
    MC(pp, digit);
    MC("7\nFizz\n0", 7);

    MC(pp, digit);
    MC("9\nBuzz\nFizz\n00000", 12);
    return buf;
}

template <int digit>
char* output1(char* RE buf, const char* RE pp) {
    //  22   23   24    25    26   27   28   29 30
    //  2  3    fizz   buzz  6    fizz  8   9   FizzBuzz
    MC(pp, digit);
    MC("2\n00", 2);
    MC(pp, digit);
    MC("3\nFizz\nBuzz\n0000", 12);

    MC(pp, digit);
    MC("6\nFizz\n0", 7);

    MC(pp, digit);
    MC("8\n00", 2);
    MC(pp, digit);
    MC("9\nFizzBuzz\n000000", 11);
    return buf;
}

template <int digit>
char* output2(char* RE buf, const char* RE pp) {
    // 1   2    3    4     5     6    7   8   9     10
    // 1   2  fizz   4   buzz  fizz   7   8   fizz  buzz
    MC(pp, digit);
    MC("1\n00", 2);
    MC(pp, digit);
    MC("2\nFizz\n0", 7);

    MC(pp, digit);
    MC("4\nBuzz\nFizz\n0000", 12);

    MC(pp, digit);
    MC("7\n00", 2);
    MC(pp, digit);
    MC("8\nFizz\nBuzz\n0000", 12);
    return buf;
}

// clang-format off
#define REPSIZE() \
    M(1) M(2) M(3) M(4) M(5) M(6) M(7) M(8) M(9) M(10) \
    M(11) M(12)  M(13) M(14) M(15) M(16) M(17) M(18) M(19) M(20) M(21)
// clang-format on

#undef M
#define M(x)  \
    case (x): \
        return output0<x>(buf, p);

char* Output0(char* buf, const char* p, int digit) {
    switch (digit) {
        REPSIZE();
    default:
        break;
    }
    return nullptr;
}

#undef M
#define M(x)  \
    case (x): \
        return output1<x>(buf, p);

char* Output1(char* buf, const char* p, int digit) {
    switch (digit) {
        REPSIZE();
    default:
        break;
    }
    return nullptr;
}

#undef M
#define M(x)  \
    case (x): \
        return output2<x>(buf, p);

char* Output2(char* buf, const char* p, int digit) {
    switch (digit) {
        REPSIZE();
    default:
        break;
    }
    return nullptr;
}

bool use_vmsplice = false;
bool quiet = false;

static inline void os_write(int out, const char* buf, unsigned int n) {
    while (n) {
        ssize_t written = write(out, buf, n);

        if (written >= 0) {
            buf += written;
            n -= written;
        }
    }
}

constexpr int WRITE_SIZE = 64 * 1024;
constexpr int BUFFER_SIZE = 2 * 1024 * 1024;
alignas(64) char buffer[2][BUFFER_SIZE];

#ifdef __linux__
bool fix_pipe_size() {
    int fd = 1;
    int pipe_size = fcntl(fd, F_GETPIPE_SZ);
    if (pipe_size == -1) {
        perror("get pipe size failed.");
        return false;
    }
    fprintf(stderr, "default pipe size: %d\n", pipe_size);

    int ret = fcntl(fd, F_SETPIPE_SZ, BUFFER_SIZE);
    if (ret < 0) {
        perror("set pipe size failed.");
        return false;
    }
    pipe_size = fcntl(fd, F_GETPIPE_SZ);
    if (pipe_size == -1) {
        perror("get pipe size failed.");
        return false;
    }
    fprintf(stderr, "new pipe size: %ld\n", pipe_size);
    return true;
}
#endif

void flush(char*& buf, char*& head, int& count, bool force, int reserve = 0) {
    if (force) {
        if (!quiet) {
            os_write(1, head, buf - head);
            fprintf(stderr, "syscall: %d\n", count);
        }
    }
    constexpr int RESERVE = DigitContext::MAXDIGIT * 30;
    if (reserve == 0) {
        reserve = RESERVE;
    }
    size_t size = buf - head;
#ifdef __linux__
    if (use_vmsplice) {
        if (size > (BUFFER_SIZE - reserve)) {
            count += 1;
            // ssize_t vmsplice(int fd, const struct iovec* iov, size_t nr_segs, unsigned int flags);
            iovec iov[1] = {
                    {.iov_base = head, .iov_len = size},
            };
            if (!quiet) {
                vmsplice(1, iov, 1, 0);
            }
            head = (head == buffer[0]) ? buffer[1] : buffer[0];
            buf = head;
        }
    }
#endif
    if (!use_vmsplice) {
        if (size > (WRITE_SIZE - reserve)) {
            count += 1;
            if (!quiet) {
                os_write(1, head, size);
            }
            buf = head;
        }
    }
}

void unroll_fizzbuzz_v2(const uint64_t n, const uint64_t start) {
#ifdef __linux__
    madvise(buffer, sizeof(buffer), MADV_HUGEPAGE);
#endif
    char* head = buffer[0];
    char* buf = head;

    digitctx[0].init();
    digitctx[0].next();

    digitctx[1].init();
    digitctx[1].next();
    digitctx[1].next();

    digitctx[2].init();
    digitctx[2].next3();

    int count = 0;
    uint64_t i = 0;

    if (start <= 10) {
        buf += snprintf(buf, 256, "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n");
        i = 10;
    } else {
        i = (start - 10) / 30 * 30 - 20;
        digitctx[0].initfrom(i);
        digitctx[1].initfrom(i);
        digitctx[1].next();
        digitctx[2].initfrom(i);
        digitctx[2].next3();
    }

    for (; i < n; i += 30) {
        int size0 = 6 * digitctx[0].digit() + 41;
        int size1 = 5 * digitctx[1].digit() + 34 + size0;
        int size2 = 5 * digitctx[2].digit() + 35 + size1;

        // FIXME: I don't know why it does not work, the pv hangs without any output.
        // flush(buf, head, count, false, size2);

        // 11 - 21
        Output0(buf, digitctx[0].begin, digitctx[0].digit());

        // 22 - 30
        Output1(buf + size0, digitctx[1].begin, digitctx[1].digit());

        // 31 - 40
        Output2(buf + size1, digitctx[2].begin, digitctx[2].digit());

        buf += size2;
        digitctx[0].next3();
        digitctx[1].next3();
        digitctx[2].next3();

        flush(buf, head, count, false);
    }
    flush(buf, head, count, true);
}

#include "fizzbuzz-gen.h"

void unroll_fizzbuzz_v3(const uint64_t n, const uint64_t start) {
#ifdef __linux__
    madvise(buffer, sizeof(buffer), MADV_HUGEPAGE);
#endif
    if (!quiet) {
        os_write(1, GEN_FIRST_1000, strlen(GEN_FIRST_1000));
    }

    char* head = buffer[0];
    char* buf = head;

    digitctx[0].init();
    digitctx[0].next();

    digitctx[1].init();
    digitctx[1].next();
    digitctx[1].next();

    digitctx[2].init();
    digitctx[2].next3();

    int count = 0;
    uint64_t i = GEN_INIT;

    for (; i < n; i += GEN_STEP) {
        int d0 = digitctx[0].digit();
        int d1 = digitctx[1].digit();
        int d2 = digitctx[2].digit();

        GEN_COMPUTE_SIZE;

        flush(buf, head, count, false, size2);
        __builtin_prefetch(buf + size0);
        GEN_OUTPUT_1(buf, digitctx[0].begin, d0);
        __builtin_prefetch(buf + size1);
        GEN_OUTPUT_2(buf + size0, digitctx[1].begin, d1);
        __builtin_prefetch(buf + size2);
        GEN_OUTPUT_3(buf + size1, digitctx[2].begin, d2);

        buf += size2;
        digitctx[0].next3();
        digitctx[1].next3();
        digitctx[2].next3();
    }
    flush(buf, head, count, true);
}

// 10^15.
const uint64_t N = 1000ULL * 1000 * 1000 * 1000 * 1000;
int main(int argc, const char** argv) {
    std::string mode = "opt";
    uint64_t n = N;
    uint64_t start = 1;
    for (int i = 1; i < argc; i++) {
        std::string s = argv[i];
        if (s == "-m") {
            mode = argv[i + 1];
            i += 1;
        } else if (s == "-n") {
            n = atoll(argv[i + 1]);
            i += 1;
        } else if (s == "--vm") {
            use_vmsplice = true;
        } else if (s == "-q") {
            quiet = true;
        } else if (s == "-s") {
            start = atoll(argv[i + 1]);
            i += 1;
        } else {
            fprintf(stderr, "unknown arg: %s\n", s.c_str());
            return -1;
        }
    }
#ifdef __linux__
    if (use_vmsplice) {
        bool ok = fix_pipe_size();
        if (!ok) {
            use_vmsplice = false;
            fprintf(stderr, "use_vmsplice disabled!\n");
        }
    }
#else
    use_vmsplice = false;
#endif
    if (mode == "naive") {
        naive_fizzbuzz(n);
    } else if (mode == "v2") {
        unroll_fizzbuzz_v2(n, start);
    } else if (mode == "v3") {
        unroll_fizzbuzz_v3(n, start);
    } else if (mode == "opt") {
        unroll_fizzbuzz_v3(n, start);
    }
    return 0;
}
