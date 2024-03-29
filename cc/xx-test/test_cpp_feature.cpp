/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <atomic>
#include <filesystem>
#include <thread>

#include "Common.h"
using namespace std;

#define HEADER() std::cout << "==========" << __func__ << "==========\n"

void use_filesystem() {
    HEADER();
    std::filesystem::path p("hdfs://127.0.0.1:9000/hello/world/data");
    std::cout << "full path = " << p << "\n";
    std::cout << "filename = " << p.filename() << "\n";
    auto pp = p.parent_path();
    std::cout << "parent filename = " << pp.filename() << "\n";
    std::cout << "/root exists or not: " << std::filesystem::exists("/root") << "\n";
    p.append("fuck").append("yeak");
    std::cout << p << "\n";
}

template <typename T, typename A = std::allocator<T>>
class RawAllocator : public A {
    static_assert(std::is_trivially_destructible_v<T>, "not trivially destructible type");
    typedef std::allocator_traits<A> a_t;

public:
    template <typename U>
    struct rebind {
        using other = RawAllocator<U, typename a_t::template rebind_alloc<U>>;
    };

    // using A::A;

    T* allocate(size_t n, const void* hint = 0) {
        fprintf(stderr, "allocate %zu bytes\n", n);
        return (T*)malloc(sizeof(T) * n);
    }

    void deallocate(T* p, size_t n) {
        fprintf(stderr, "deallocate %zu bytes\n", n);
        free(p);
    }

    // do not initialized allocated.
    template <typename U>
    void construct(U* ptr) noexcept(std::is_nothrow_default_constructible<U>::value) {
        ::new (static_cast<void*>(ptr)) U;
    }
    template <typename U, typename... Args>
    void construct(U* ptr, Args&&... args) {
        a_t::construct(static_cast<A&>(*this), ptr, std::forward<Args>(args)...);
    }
};

template <typename T>
using MyVector = std::vector<T, RawAllocator<T>>;

void use_custom_allocator() {
    HEADER();
    MyVector<int> rs;
    for (int i = 0; i < 10000; i++) {
        rs.push_back(i);
    }
}

#ifdef __linux__
void test_lock_free_op() {
    HEADER();
    std::atomic<double> d;
    std::cout << "std::atomic<double> is_lock_free = " << d.is_lock_free() << "\n";
    std::cout << "std::atomic<double> is_always_lock_free = " << std::atomic<double>::is_always_lock_free << "\n";

    struct X {
        int x;
        int y;
        int z;
    };
    std::atomic<X> xz;
    std::cout << "std::atomic<X> is_lock_free = " << xz.is_lock_free() << "\n";
    std::cout << "std::atomic<X> is_always_lock_free = " << std::atomic<X>::is_always_lock_free << "\n";

    struct Y {
        int x;
        int y;
        int z;
        int m;
    };
    std::atomic<Y> yz;
    std::cout << "std::atomic<Y> is_lock_free = " << yz.is_lock_free() << "\n";
    std::cout << "std::atomic<Y> is_always_lock_free = " << std::atomic<Y>::is_always_lock_free << "\n";
}
#endif

void test_hardward_concurrency() {
    HEADER();
#ifdef __cpp_lib_jthread
    unsigned int n = std::jthread::hardware_concurrency();
    std::cout << n << " concurrent threads are supported.\n";
#endif
}

// https://gcc.gnu.org/onlinedocs/gcc/x86-Built-in-Functions.html
#define CHECK_CPUID(x)                                                         \
    do {                                                                       \
        int ok = __builtin_cpu_supports(x);                                    \
        cout << "support '" << x << "' = " << (ok ? "true" : "false") << "\n"; \
    } while (0)

void test_cpu_supports() {
    HEADER();
    CHECK_CPUID("sse");
    CHECK_CPUID("sse2");
    CHECK_CPUID("avx");
    CHECK_CPUID("avx2");
    CHECK_CPUID("avx512f");
    CHECK_CPUID("avx512vbmi");
    CHECK_CPUID("avx512vbmi2");
}

void test_vector_resize_uninitialized() {
    HEADER();
    std::vector<int> v;
    starrocks::raw::stl_vector_resize_uninitialized(&v, 10);
    printf("new vector size = %zu\n", v.size());
}

#ifdef __x86_64__
void test_pointer_mark() {
    HEADER();
    int a = 10;
    int* p = &a;
    POINTER_SET_BIT(p, POINTER_LOWEST_UNUSED_BIT);
    printf("p = %p\n", p);
    POINTER_CLR_BIT(p, POINTER_LOWEST_UNUSED_BIT);
    printf("p = %p, *p = %d\n", p, *p);
}
#endif

int main() {
    use_filesystem();
    use_custom_allocator();
#ifdef __linux__
    test_lock_free_op();
#endif
    test_hardward_concurrency();
    test_cpu_supports();
    test_vector_resize_uninitialized();
#ifdef __x86_64__
    test_pointer_mark();
#endif
}
