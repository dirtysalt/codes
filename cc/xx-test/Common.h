/* coding:utf-8
 * Copyright (C) dirlt
 */

#pragma once

#ifdef __linux__
#include <asm/unistd.h>
#include <linux/perf_event.h>
#endif // __linux__

#ifdef __AVX2__
// #include <emmintrin.h>
// #include <xmmintrin.h>
// #include <pmmintrin.h>
#include <immintrin.h>
//#include <x86intrin.h>
#endif

#include <sched.h>
#include <sys/ioctl.h>
#include <sys/syscall.h> /* Definition of SYS_* constants */
#include <unistd.h>

#include <cassert>
#include <chrono>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iostream>
#include <memory>
#include <string>
#include <type_traits>
#include <utility>
#include <vector>

#if __cplusplus > 201703L
#define __CXX20__
#endif

// Compiler hint that this branch is likely or unlikely to
// be taken. Take from the "What all programmers should know
// about memory" paper.
// example: if (LIKELY(size > 0)) { ... }
// example: if (UNLIKELY(!status.ok())) { ... }
#define CACHE_LINE_SIZE 64

#ifdef LIKELY
#undef LIKELY
#endif

#ifdef UNLIKELY
#undef UNLIKELY
#endif

#define EXIT_FAILURE 1
#define LIKELY(expr) __builtin_expect(!!(expr), 1)
#define UNLIKELY(expr) __builtin_expect(!!(expr), 0)

#define PREFETCH(addr) __builtin_prefetch(addr)

/// Force inlining. The 'inline' keyword is treated by most compilers as a hint,
/// not a command. This should be used sparingly for cases when either the function
/// needs to be inlined for a specific reason or the compiler's heuristics make a bad
/// decision, e.g. not inlining a small function on a hot path.
#define ALWAYS_INLINE __attribute__((always_inline))
#define FORCE_INLINE inline __attribute__((always_inline))
#define NOINLINE __attribute__((noinline))
#define UNUSED __attribute__((unused))

#define ALIGN_CACHE_LINE __attribute__((aligned(CACHE_LINE_SIZE)))

#ifndef DIAGNOSTIC_PUSH
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
#endif // ifndef DIAGNOSTIC_PUSH

#ifndef DIAGNOSTIC_IGNORE
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
#endif // ifndef DIAGNOSTIC_IGNORE

#ifdef __AVX2__
void p128_hex_u8(__m128i in) {
    alignas(16) uint8_t v[16];
    _mm_store_si128((__m128i*)v, in);
    printf("v16_u8: | %x %x %x %x | %x %x %x %x | %x %x %x %x | %x %x %x %x |\n", v[0], v[1], v[2], v[3], v[4], v[5],
           v[6], v[7], v[8], v[9], v[10], v[11], v[12], v[13], v[14], v[15]);
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
    for (int i = 0; i < 32; i++) {
        if (i % 8 == 0) printf("|");
        printf("%x ", v[i]);
    }
    printf("|\n");
}
#endif

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

// This class is used to defer a function when this object is deconstruct
template <class DeferFunction>
class DeferOp {
public:
    explicit DeferOp(DeferFunction func) : _func(std::move(func)) {}

    ~DeferOp() { _func(); };

private:
    DeferFunction _func;
};

inline uint32_t rotl32(uint32_t x, int8_t r) {
    return (x << r) | (x >> (32 - r));
}

inline uint64_t rotl64(uint64_t x, int8_t r) {
    return (x << r) | (x >> (64 - r));
}

#define ROTL32(x, y) rotl32(x, y)
#define ROTL64(x, y) rotl64(x, y)
#define BIG_CONSTANT(x) (x##LLU)

FORCE_INLINE uint64_t fmix64(uint64_t k) {
    k ^= k >> 33;
    k *= BIG_CONSTANT(0xff51afd7ed558ccd);
    k ^= k >> 33;
    k *= BIG_CONSTANT(0xc4ceb9fe1a85ec53);
    k ^= k >> 33;

    return k;
}

FORCE_INLINE uint64_t getblock64(const uint64_t* p, int i) {
    return p[i];
}

void inline_murmur_hash3_x64_64(const void* key, const int len, const uint64_t seed, void* out) {
    const uint8_t* data = (const uint8_t*)key;
    const int nblocks = len / 8;
    uint64_t h1 = seed;

    const uint64_t c1 = BIG_CONSTANT(0x87c37b91114253d5);
    const uint64_t c2 = BIG_CONSTANT(0x4cf5ad432745937f);

    //----------
    // body

    const uint64_t* blocks = (const uint64_t*)(data);

    for (int i = 0; i < nblocks; i++) {
        uint64_t k1 = getblock64(blocks, i);

        k1 *= c1;
        k1 = ROTL64(k1, 31);
        k1 *= c2;
        h1 ^= k1;

        h1 = ROTL64(h1, 27);
        h1 = h1 * 5 + 0x52dce729;
    }

    //----------
    // tail

    const uint8_t* tail = (const uint8_t*)(data + nblocks * 8);
    uint64_t k1 = 0;

    switch (len & 7) {
    case 7:
        k1 ^= ((uint64_t)tail[6]) << 48;
    case 6:
        k1 ^= ((uint64_t)tail[5]) << 40;
    case 5:
        k1 ^= ((uint64_t)tail[4]) << 32;
    case 4:
        k1 ^= ((uint64_t)tail[3]) << 24;
    case 3:
        k1 ^= ((uint64_t)tail[2]) << 16;
    case 2:
        k1 ^= ((uint64_t)tail[1]) << 8;
    case 1:
        k1 ^= ((uint64_t)tail[0]) << 0;
        k1 *= c1;
        k1 = ROTL64(k1, 31);
        k1 *= c2;
        h1 ^= k1;
    };

    //----------
    // finalization

    h1 ^= len;
    h1 = fmix64(h1);

    ((uint64_t*)out)[0] = h1;
}

#ifdef __linux__
// ======================================================
// https://man7.org/linux/man-pages/man3/CPU_SET.3.html

static void pin_to_cpu(int core_id) {
    cpu_set_t cpu_mask;
    CPU_ZERO(&cpu_mask);
    CPU_SET(core_id, &cpu_mask);
    if (sched_setaffinity(0, sizeof(cpu_mask), &cpu_mask) != 0) {
        fprintf(stderr, "Could not set CPU affinity\n");
        exit(EXIT_FAILURE);
    }
}

// =====================================================

// --------------------------------------------------------------------
// perf instrumentation -- a mixture of man 3 perf_event_open and
// <https://stackoverflow.com/a/42092180>

static long perf_event_open(struct perf_event_attr* hw_event, pid_t pid, int cpu, int group_fd, unsigned long flags) {
    int ret;
    ret = syscall(__NR_perf_event_open, hw_event, pid, cpu, group_fd, flags);
    return ret;
}

static void setup_perf_event(struct perf_event_attr* evt, int* fd, uint64_t* id, uint32_t evt_type, uint64_t evt_config,
                             int group_fd) {
    memset(evt, 0, sizeof(struct perf_event_attr));
    evt->type = evt_type;
    evt->size = sizeof(struct perf_event_attr);
    evt->config = evt_config;
    evt->disabled = 1;
    evt->exclude_kernel = 1;
    evt->exclude_hv = 1;
    evt->read_format = PERF_FORMAT_GROUP | PERF_FORMAT_ID;

    *fd = perf_event_open(evt, 0, -1, group_fd, 0);
    if (*fd == -1) {
        fprintf(stderr, "Error opening leader %llx\n", evt->config);
        exit(EXIT_FAILURE);
    }

    ioctl(*fd, PERF_EVENT_IOC_ID, id);
}

static struct perf_event_attr perf_cycles_evt;
static int perf_cycles_fd;
static uint64_t perf_cycles_id;

static struct perf_event_attr perf_clock_evt;
static int perf_clock_fd;
static uint64_t perf_clock_id;

static struct perf_event_attr perf_instrs_evt;
static int perf_instrs_fd;
static uint64_t perf_instrs_id;

static struct perf_event_attr perf_cache_misses_evt;
static int perf_cache_misses_fd;
static uint64_t perf_cache_misses_id;

static struct perf_event_attr perf_cache_references_evt;
static int perf_cache_references_fd;
static uint64_t perf_cache_references_id;

static struct perf_event_attr perf_branch_misses_evt;
static int perf_branch_misses_fd;
static uint64_t perf_branch_misses_id;

static struct perf_event_attr perf_branch_instructions_evt;
static int perf_branch_instructions_fd;
static uint64_t perf_branch_instructions_id;

static void perf_init(void) {
    // Cycles
    setup_perf_event(&perf_cycles_evt, &perf_cycles_fd, &perf_cycles_id, PERF_TYPE_HARDWARE, PERF_COUNT_HW_CPU_CYCLES,
                     -1);
    // Clock
    setup_perf_event(&perf_clock_evt, &perf_clock_fd, &perf_clock_id, PERF_TYPE_SOFTWARE, PERF_COUNT_SW_TASK_CLOCK,
                     perf_cycles_fd);
    // Instructions
    setup_perf_event(&perf_instrs_evt, &perf_instrs_fd, &perf_instrs_id, PERF_TYPE_HARDWARE, PERF_COUNT_HW_INSTRUCTIONS,
                     perf_cycles_fd);
    // Cache misses
    setup_perf_event(&perf_cache_misses_evt, &perf_cache_misses_fd, &perf_cache_misses_id, PERF_TYPE_HARDWARE,
                     PERF_COUNT_HW_CACHE_MISSES, perf_cycles_fd);
    // Cache references
    setup_perf_event(&perf_cache_references_evt, &perf_cache_references_fd, &perf_cache_references_id,
                     PERF_TYPE_HARDWARE, PERF_COUNT_HW_CACHE_REFERENCES, perf_cycles_fd);
    // Branch misses
    setup_perf_event(&perf_branch_misses_evt, &perf_branch_misses_fd, &perf_branch_misses_id, PERF_TYPE_HARDWARE,
                     PERF_COUNT_HW_BRANCH_MISSES, perf_cycles_fd);
    // Branch instructions
    setup_perf_event(&perf_branch_instructions_evt, &perf_branch_instructions_fd, &perf_branch_instructions_id,
                     PERF_TYPE_HARDWARE, PERF_COUNT_HW_BRANCH_INSTRUCTIONS, perf_cycles_fd);
}

static void perf_close(void) {
    close(perf_clock_fd);
    close(perf_cycles_fd);
    close(perf_instrs_fd);
    close(perf_cache_misses_fd);
    close(perf_cache_references_fd);
    close(perf_branch_misses_fd);
    close(perf_branch_instructions_fd);
}

static void disable_perf_count(void) {
    ioctl(perf_cycles_fd, PERF_EVENT_IOC_DISABLE, PERF_IOC_FLAG_GROUP);
}

static void enable_perf_count(void) {
    ioctl(perf_cycles_fd, PERF_EVENT_IOC_ENABLE, PERF_IOC_FLAG_GROUP);
}

static void reset_perf_count(void) {
    ioctl(perf_cycles_fd, PERF_EVENT_IOC_RESET, PERF_IOC_FLAG_GROUP);
}

struct perf_read_value {
    uint64_t value;
    uint64_t id;
};

struct perf_read_format {
    uint64_t nr;
    struct perf_read_value values[];
};

static char perf_read_buf[4096];

struct perf_count {
    uint64_t cycles;
    double seconds;
    uint64_t instructions;
    uint64_t cache_misses;
    uint64_t cache_references;
    uint64_t branch_misses;
    uint64_t branch_instructions;

    perf_count()
            : cycles(0),
              seconds(0.0),
              instructions(0),
              cache_misses(0),
              cache_references(0),
              branch_misses(0),
              branch_instructions(0) {}
};

static void read_perf_count(struct perf_count* count) {
    if (!read(perf_cycles_fd, perf_read_buf, sizeof(perf_read_buf))) {
        fprintf(stderr, "Could not read cycles from perf\n");
        exit(EXIT_FAILURE);
    }
    struct perf_read_format* rf = (struct perf_read_format*)perf_read_buf;
    if (rf->nr != 7) {
        fprintf(stderr, "Bad number of perf events\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < static_cast<int>(rf->nr); i++) {
        struct perf_read_value* value = &rf->values[i];
        if (value->id == perf_cycles_id) {
            count->cycles = value->value;
        } else if (value->id == perf_clock_id) {
            count->seconds = ((double)(value->value / 1000ull)) / 1000000.0;
        } else if (value->id == perf_instrs_id) {
            count->instructions = value->value;
        } else if (value->id == perf_cache_misses_id) {
            count->cache_misses = value->value;
        } else if (value->id == perf_cache_references_id) {
            count->cache_references = value->value;
        } else if (value->id == perf_branch_misses_id) {
            count->branch_misses = value->value;
        } else if (value->id == perf_branch_instructions_id) {
            count->branch_instructions = value->value;
        } else {
            fprintf(stderr, "Spurious value in perf read (%ld)\n", value->id);
            exit(EXIT_FAILURE);
        }
    }
}
#endif // __linux__

// Only x86 support function multiversion.
// https://gcc.gnu.org/wiki/FunctionMultiVersioning
// TODO(GoHalo) Support aarch64 platform.
#if defined(__GNUC__) && defined(__x86_64__)
#include <x86intrin.h>

#define MFV_IMPL(IMPL, ATTR)                                                               \
    _Pragma("GCC diagnostic push") _Pragma("GCC diagnostic ignored \"-Wunused-function\"") \
            ATTR static inline IMPL _Pragma("GCC diagnostic pop")

#define MFV_SSE42(IMPL) MFV_IMPL(IMPL, __attribute__((target("sse4.2"))))
#define MFV_AVX2(IMPL) MFV_IMPL(IMPL, __attribute__((target("avx2"))))
#define MFV_AVX512F(IMPL) MFV_IMPL(IMPL, __attribute__((target("avx512f"))))
#define MFV_AVX512BW(IMPL) MFV_IMPL(IMPL, __attribute__((target("avx512bw"))))
#define MFV_AVX512VL(IMPL) MFV_IMPL(IMPL, __attribute__((target("avx512vl"))))
#define MFV_DEFAULT(IMPL) MFV_IMPL(IMPL, __attribute__((target("default"))))

#else

#define MFV_SSE42(IMPL)
#define MFV_AVX2(IMPL)
#define MFV_AVX512F(IMPL)
#define MFV_AVX512BW(IMPL)
#define MFV_AVX512VL(IMPL)
#define MFV_DEFAULT(IMPL) IMPL

#endif

namespace starrocks {
namespace raw {

// This file is licensed under the Elastic License 2.0. Copyright 2021-present, StarRocks Inc.
// RawAllocator allocates `trailing` more object(not bytes) than caller required,
// to avoid overflow when the memory is operated with 128-bit aligned instructions,
// such as `_mm_testc_si128`.
//
// Also it does not initiate allocated object to zero-value.
// This behavior is shipped from raw::RawAllocator.
//
// C++ Reference recommend to use this allocator implementation to
// prevent containers resize invocation from initializing the allocated
// memory space unnecessarily.
//
//   https://stackoverflow.com/questions/21028299/is-this-behavior-of-vectorresizesize-type-n-under-c11-and-boost-container/21028912#21028912
//
// Allocator adaptor that interposes construct() calls to
// convert value initialization into default initialization.
template <typename T, size_t trailing = 16, typename A = std::allocator<T>>
class RawAllocator : public A {
    static_assert(std::is_trivially_destructible_v<T>, "not trivially destructible type");
    typedef std::allocator_traits<A> a_t;

public:
    template <typename U>
    struct rebind {
        using other = RawAllocator<U, trailing, typename a_t::template rebind_alloc<U>>;
    };

    using A::A;

    // allocate more than caller required
    T* allocate(size_t n) {
        T* x = A::allocate(n + RawAllocator::_trailing);
        return x;
    }
    T* allocate(size_t n, const void* hint) {
        T* x = A::allocate(n + RawAllocator::_trailing, hint);
        return x;
    }

    // deallocate the storage referenced by the pointer p
    void deallocate(T* p, size_t n) { A::deallocate(p, n + RawAllocator::_trailing); }

    // do not initialized allocated.
    template <typename U>
    void construct(U* ptr) noexcept(std::is_nothrow_default_constructible<U>::value) {
        ::new (static_cast<void*>(ptr)) U;
    }
    template <typename U, typename... Args>
    void construct(U* ptr, Args&&... args) {
        a_t::construct(static_cast<A&>(*this), ptr, std::forward<Args>(args)...);
    }

private:
    static const size_t _trailing = trailing;
};

template <typename T, std::size_t N = 16>
class AlignmentAllocator {
public:
    typedef T value_type;
    typedef std::size_t size_type;
    typedef std::ptrdiff_t difference_type;

    typedef T* pointer;
    typedef const T* const_pointer;

    typedef T& reference;
    typedef const T& const_reference;

public:
    AlignmentAllocator() throw() {}

    template <typename T2>
    AlignmentAllocator(const AlignmentAllocator<T2, N>&) throw() {}

    ~AlignmentAllocator() throw() {}

    pointer adress(reference r) { return &r; }

    const_pointer adress(const_reference r) const { return &r; }

#ifdef __linux__
    pointer allocate(size_type n) {
        if (n * sizeof(value_type) < N) {
            return (pointer)std::aligned_alloc(N, N);
        }
        return (pointer)std::aligned_alloc(N, n * sizeof(value_type));
    }
#endif // __linux__

#ifdef __APPLE__
    pointer allocate(size_type n) {
        if (n * sizeof(value_type) < N) {
            return (pointer)aligned_alloc(N, N);
        }
        return (pointer)aligned_alloc(N, n * sizeof(value_type));
    }
#endif // __APPLE__
    void deallocate(pointer p, size_type) { free(p); }

    void construct(pointer p, const value_type& wert) { new (p) value_type(wert); }

    void destroy(pointer p) { p->~value_type(); }

    size_type max_size() const throw() { return size_type(-1) / sizeof(value_type); }

    template <typename T2>
    struct rebind {
        typedef AlignmentAllocator<T2, N> other;
    };

    bool operator!=(const AlignmentAllocator<T, N>& other) const { return !(*this == other); }

    // Returns true if and only if storage allocated from *this
    // can be deallocated from other, and vice versa.
    // Always returns true for stateless allocators.
    bool operator==(const AlignmentAllocator<T, N>& other) const { return true; }
};

// https://github.com/StarRocks/starrocks/issues/233
// older versions of CXX11 string abi are cow semantic and our optimization to provide raw_string causes crashes.
//
// So we can't use this optimization when we detect a link to an old version of abi,
// and this may affect performance. So we strongly recommend to use the new version of abi
//
#if _GLIBCXX_USE_CXX11_ABI
using RawString = std::basic_string<char, std::char_traits<char>, RawAllocator<char, 0>>;
using RawStringPad16 = std::basic_string<char, std::char_traits<char>, RawAllocator<char, 16>>;
#else
using RawString = std::string;
using RawStringPad16 = std::string;
#endif
// From cpp reference: "A trivial destructor is a destructor that performs no action. Objects with
// trivial destructors don't require a delete-expression and may be disposed of by simply
// deallocating their storage. All data types compatible with the C language (POD types)
// are trivially destructible."
// Types with trivial destructors is safe when when move content from a RawVectorPad16<T> into
// a std::vector<U> and both T and U the same bit width, i.e.
// starrocks::raw::RawVectorPad16<int8_t> a;
// a.resize(100);
// std::vector<uint8_t> b = std::move(reinterpret_cast<std::vector<uint8_t>&>(a));
template <class T>
using RawVector = std::vector<T, RawAllocator<T, 0>>;

template <class T>
using RawVectorPad16 = std::vector<T, RawAllocator<T, 16>>;

template <class T>
inline void make_room(std::vector<T>* v, size_t n) {
    RawVector<T> rv;
    rv.resize(n);
    v->swap(reinterpret_cast<std::vector<T>&>(rv));
}

inline void make_room(std::string* s, size_t n) {
    RawStringPad16 rs;
    rs.resize(n);
    s->swap(reinterpret_cast<std::string&>(rs));
}

template <typename T>
inline void stl_vector_resize_uninitialized(std::vector<T>* vec, size_t new_size) {
    ((RawVector<T>*)vec)->resize(new_size);
}

inline void stl_string_resize_uninitialized(std::string* str, size_t new_size) {
    ((RawString*)str)->resize(new_size);
}

} // namespace raw
} //namespace starrocks

#ifdef __x86_64__
#define POINTER_LOWEST_UNUSED_BIT 48
#define POINTER_SET_BIT(p, b)               \
    do {                                    \
        uint64_t* pp = (uint64_t*)(&p);     \
        (*pp) = (*pp) | ((uint64_t)1 << b); \
    } while (0)

#define POINTER_CHECK_BIT(p, b) (((uint64_t)(&p) >> b) & 0x1)

#define POINTER_CLR_BIT(p, b)                  \
    do {                                       \
        uint64_t* pp = (uint64_t*)(&p);        \
        (*pp) = (*pp) & (~((uint64_t)1 << b)); \
    } while (0)
#endif
