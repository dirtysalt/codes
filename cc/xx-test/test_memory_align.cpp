/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdint>
#include <iostream>
#include <thread>

using namespace std;

#ifdef __clang__
#define DIAGNOSTIC_PUSH _Pragma("clang diagnostic push")
#define DIAGNOSTIC_POP _Pragma("clang diagnostic pop")
#elif defined(__GNUC__)
#define DIAGNOSTIC_PUSH _Pragma("GCC diagnostic push")
#define DIAGNOSTIC_POP _Pragma("GCC diagnostic pop")
#elif defined(_MSC_VER)
#define DIAGNOSTIC_PUSH __pragma(warning(push))
#define DIAGNOSTIC_POP __pragma(warning(pop))
#else
#error("Unknown compiler")
#endif

#define PRAGMA(TXT) _Pragma(#TXT)

#ifdef __clang__
#define DIAGNOSTIC_IGNORE(XXX) PRAGMA(clang diagnostic ignored XXX)
#elif defined(__GNUC__)
#define DIAGNOSTIC_IGNORE(XXX) PRAGMA(GCC diagnostic ignored XXX)
#elif defined(_MSC_VER)
#define DIAGNOSTIC_IGNORE(XXX) __pragma(warning(disable : XXX))
#else
#define DIAGNOSTIC_IGNORE(XXX)
#endif

#define CACHE_LINE_SIZE 64
#define CACHE_LINE_ALIGN alignas(CACHE_LINE_SIZE)

struct CACHE_LINE_ALIGN BookKeeper {
    volatile size_t count;
    volatile int bypass;
};

static const size_t N = 128;
static const size_t LOOP = 1000000000;
BookKeeper worker_data[N];
std::thread workers[N];

DIAGNOSTIC_PUSH
int main() {
    printf("size = %zu\n", sizeof(BookKeeper));

    for (int i = 0; i < N; i++) {
        std::thread t(
                [](BookKeeper* data) {
                    for (size_t j = 0; j < LOOP; j++) {
                        // DIAGNOSTIC_IGNORE("-Wvolatile")
                        data->count += 1;
                    }
                },
                &worker_data[i]);
        workers[i] = std::move(t);
    }
    for (int i = 0; i < N; i++) {
        workers[i].join();
    }

    size_t sum = 0;
    for (int i = 0; i < N; i++) {
        sum += worker_data[i].count;
    }
    printf("sum = %zu, expected = %zu\n", sum, N * LOOP);
    return 0;
}
DIAGNOSTIC_PUSH
