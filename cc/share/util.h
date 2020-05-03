/*
 * Copyright (C) dirlt
 */

#ifndef __CC_SHARE_UTIL_H__
#define __CC_SHARE_UTIL_H__

#include <sys/time.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdint.h>
#include <unistd.h>
#include <linux/unistd.h>
#include <sched.h>
#include <fcntl.h>
#include <string>
#include <cerrno>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#ifndef BEGIN_CDECLS
#ifdef __cplusplus
#define BEGIN_CDECLS extern "C" {
#define END_CDELS }
#else
#define BEGIN_CDECLS
#define END_CDELS
#endif
#endif

#ifndef OFFSET_OF
#define OFFSET_OF(type, member) ((unsigned long)(&((type *)0)->member))
#endif

#ifndef CONTAINER_OF
#define CONTAINER_OF(ptr, type, member) (((type *)(((char *)ptr) - OFFSET_OF(type, member))))
#endif

#define nop() __asm__ ("pause" )
#define mfence_c() __asm__ __volatile__ ("": : :"memory")
// #define mfence_c()
#define mfence_x86() __asm__ __volatile__ ("mfence": : :"memory")

// (dirlt): google protobuf code.
// Return a mutable char* pointing to a string's internal buffer,
// which may not be null-terminated. Writing through this pointer will
// modify the string.
//
// string_as_array(&str)[i] is valid for 0 <= i < str.size() until the
// next call to a string method that invalidates iterators.
//
// As of 2006-04, there is no standard-blessed way of getting a
// mutable reference to a string's internal buffer. However, issue 530
// (http://www.open-std.org/JTC1/SC22/WG21/docs/lwg-active.html#530)
// proposes this as the method. According to Matt Austern, this should
// already work on all current implementations.
static inline char* string_as_array(std::string* str) {
    // DO NOT USE const_cast<char*>(str->data())! See the unittest for why.
    return str->empty() ? NULL : &*str->begin();
}

static inline uint32_t reverse_endian(uint32_t p) {
    return (((p & 0x000000ff) << 24) + ((p & 0x0000ff00) << 8) + ((p & 0x00ff0000) >> 8) + ((p & 0xff000000) >> 24));
}

// (dirlt): google tcmalloc code.
// A safe way of doing "(1 << n) - 1" -- without worrying about overflow
// Note this will all be resolved to a constant expression at compile-time
#define N_ONES_(IntType, N)                                     \
    ( (N) == 0 ? 0 : ((static_cast<IntType>(1) << ((N)-1))-1 +    \
                      (static_cast<IntType>(1) << ((N)-1))) )
static inline bool is_exp2(uint64_t x) {
    return (x & (x - 1)) ? false : true;
}

static inline uint32_t reverse_uint32(uint32_t x) {
    x = (x & 0x55555555) << 1 | (x & 0xAAAAAAAA) >> 1;
    x = (x & 0x33333333) << 2 | (x & 0xCCCCCCCC) >> 2;
    x = (x & 0x0F0F0F0F) << 4 | (x & 0xF0F0F0F0) >> 4;
    x = (x & 0x00FF00FF) << 8 | (x & 0xFF00FF00) >> 8;
    x = (x & 0x0000FFFF) << 16 | (x & 0xFFFF0000) >> 16;
    return x;
}

static inline void set_nonblock(int fd) {
    int x = fcntl(fd, F_GETFL);
    x |= O_NONBLOCK;
    fcntl(fd, F_SETFL, x);
}

static inline pid_t get_tid() {
    return syscall(__NR_gettid);
}

// not portable!!!
// static inline pid_t asm_get_tid() {
//   // http://dirlt.com/APUE.html
//   pid_t pid=0;
//   __asm__ __volatile__(
//     "movl %%fs:%c1,%0\n\t"
//     :"=r"(pid)
//     :"i"(144));
//   return pid;
// }

#ifdef __x86_64__
static inline uint64_t rdtsc() {
    uint32_t hi, lo;
    __asm__ volatile("rdtsc"
                     :"=a"(lo), "=d"(hi)
                     ::);
    return static_cast<uint64_t>(lo) |
           (static_cast<uint64_t>(hi) << 32);
}
#endif

static inline void thread_yield() {
    sched_yield();
}

static inline double gettime_ms() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec * 1000.0 + tv.tv_usec * 0.001;
}

static inline void sleep_ms(double ms) {
    unsigned long ms2 = static_cast< unsigned long >(ms * 1000);
    usleep(ms2);
}

static inline void gettime_timespec(struct timespec* tp) {
    clock_gettime(CLOCK_REALTIME, tp);
    //struct timeval tv;
    //gettimeofday(&tv,NULL);
    //TIMEVAL_TO_TIMESPEC(&tv,tp);
}

static inline void addtime_timespec(struct timespec* tp, int ms) {
    // a little anonying.
    if(ms >= 1000) {
        tp->tv_sec += ms / 1000;
        ms %= 1000;
        tp->tv_nsec += (ms) * 1000 * 1000;
    }
    static const int m = 1000 * 1000 * 1000;
    tp->tv_sec += tp->tv_nsec / m;
    tp->tv_nsec %= m;
}

static inline void string_append_number(std::string* s, ssize_t number) {
    static const int kSize = 64;
    char txt[kSize]; // I think it's enough.
    snprintf(txt, sizeof(txt), "%zd", number);
    s->append(txt);
}

static inline std::string number_to_string(ssize_t number) {
    static const int kSize = 64;
    char txt[kSize]; // I think it's enough.
    snprintf(txt, sizeof(txt), "%zd", number);
    return txt;
}

// (dirlt): murmur hash 2A.
static inline unsigned long long murmur_hash ( const void* key, int len, unsigned int seed = 0) {
    const unsigned long long m = 0xc6a4a7935bd1e995ULL;
    const int r = 47;

    unsigned long long h = seed ^ (len * m);

    const unsigned long long* data = (const unsigned long long*)key;
    const unsigned long long* end = data + (len / 8);

    while(data != end) {
        unsigned long long k = *data++;

        k *= m;
        k ^= k >> r;
        k *= m;

        h ^= k;
        h *= m;
    }

    const unsigned char* data2 = (const unsigned char*)data;

    switch(len & 7) {
        case 7:
            h ^= (unsigned long long)(data2[6]) << 48;
        case 6:
            h ^= (unsigned long long)(data2[5]) << 40;
        case 5:
            h ^= (unsigned long long)(data2[4]) << 32;
        case 4:
            h ^= (unsigned long long)(data2[3]) << 24;
        case 3:
            h ^= (unsigned long long)(data2[2]) << 16;
        case 2:
            h ^= (unsigned long long)(data2[1]) << 8;
        case 1:
            h ^= (unsigned long long)(data2[0]);
            h *= m;
        default:
            ;
    };

    h ^= h >> r;
    h *= m;
    h ^= h >> r;

    return h;
}

static inline std::string get_hostname() {
    static const int kSize = 1024;
    char buf[kSize]; // I think it's enough.
    gethostname(buf, sizeof(buf));
    return buf;
}

// (dirlt): google leveldb code.
static inline int LockOrUnlock(int fd, bool lock) {
    errno = 0;
    struct flock f;
    memset(&f, 0, sizeof(f));
    f.l_type = (lock ? F_WRLCK : F_UNLCK);
    f.l_whence = SEEK_SET;
    f.l_start = 0;
    f.l_len = 0;        // Lock/unlock entire file
    return fcntl(fd, F_SETLK, &f);
}

static inline int lock_fd(int fd) {
    return LockOrUnlock(fd, true);
}

static inline int unlock_fd(int fd) {
    return LockOrUnlock(fd, 0);
}

static inline int support_mmx() {
    int code = 0;
    __asm__ __volatile__(
        "movl $1,%%eax\n\t"
        "cpuid\n\t"
        "test $0x800000,%%edx\n\t"
        "jz 1f\n\t"
        "movl $1,%0\n\t"
        "1:\n\t"
        :"=m"(code)
        ::"eax", "edx");
    return code;
}

static inline int support_sse() {
    int code = 0;
    __asm__ __volatile__(
        "movl $1,%%eax\n\t"
        "cpuid\n\t"
        "test $0x02000000,%%edx\n\t"
        "jz 1f\n\t"
        "movl $1,%0\n\t"
        "1:\n\t"
        :"=m"(code)
        ::"eax", "edx");
    return code;
}

static inline int support_sse2() {
    int code = 0;
    __asm__ __volatile__(
        "movl $1,%%eax\n\t"
        "cpuid\n\t"
        "test $0x04000000,%%edx\n\t"
        "jz 1f\n\t"
        "movl $1,%0\n\t"
        "1:\n\t"
        :"=m"(code)
        ::"eax", "edx");
    return code;
}

static inline int support_sse3() {
    int code = 0;
    __asm__ __volatile__(
        "movl $1,%%eax\n\t"
        "cpuid\n\t"
        "test $0x1,%%ecx\n\t"
        "jz 1f\n\t"
        "movl $1,%0\n\t"
        "1:\n\t"
        :"=m"(code)
        ::"eax", "edx");
    return code;
}

static inline int support_ssse3() {
    int code = 0;
    __asm__ __volatile__(
        "movl $1,%%eax\n\t"
        "cpuid\n\t"
        "test $0x0200,%%ecx\n\t"
        "jz 1f\n\t"
        "movl $1,%0\n\t"
        "1:\n\t"
        :"=m"(code)
        ::"eax", "edx");
    return code;
}

static inline int support_sse4_1() {
    int code = 0;
    __asm__ __volatile__(
        "movl $1,%%eax\n\t"
        "cpuid\n\t"
        "test $0x80000,%%ecx\n\t"
        "jz 1f\n\t"
        "movl $1,%0\n\t"
        "1:\n\t"
        :"=m"(code)
        ::"eax", "edx");
    return code;
}

static inline int support_sse4_2() {
    int code = 0;
    __asm__ __volatile__(
        "movl $1,%%eax\n\t"
        "cpuid\n\t"
        "test $0x0100000,%%ecx\n\t"
        "jz 1f\n\t"
        "movl $1,%0\n\t"
        "1:\n\t"
        :"=m"(code)
        ::"eax", "edx");
    return code;
}

static inline void string_replace(
    std::string& s, const std::string& src,
    const std::string& dst) {
    size_t n = s.find(src, 0);
    while(n != s.npos) {
        s = s.substr(0, n) + dst + s.substr(n + src.size());
        n = s.find(src, 0);
    }
}

#endif // __CC_SHARE_UTIL_H__
