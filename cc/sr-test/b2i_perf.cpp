#include <benchmark/benchmark.h>
#include <emmintrin.h>
#include <immintrin.h>

#include <cmath>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <random>

typedef __int128 int128_t;

struct Slice {
    const char* data;
    size_t size;
};
static constexpr int BYTE_SIZE = 11;
static constexpr int GAP_SIZE = 0;
static constexpr bool verify = false;

#define bswap_64(x) __bswap_64(x)

inline unsigned __int128 bswap_128(unsigned __int128 host_int) {
    return static_cast<unsigned __int128>(bswap_64(static_cast<uint64_t>(host_int >> 64))) |
           (static_cast<unsigned __int128>(bswap_64(static_cast<uint64_t>(host_int))) << 64);
}

static unsigned __int128 ToHost128(unsigned __int128 x) {
    return bswap_128(x);
}

static uint64_t ToHost64(uint64_t x) {
    return __bswap_64(x);
}

void make_src_data(size_t size, std::string* blob, std::vector<Slice>* src_data) {
    // assume each data is 7 bytes
    // and bewteen each data there is 4 bytes.

    // add some extra padding bytes.
    size_t bytes = (BYTE_SIZE + GAP_SIZE) * (size) + 16;
    std::mt19937_64 gen64;
    blob->resize(bytes);
    for (size_t i = 0; i < bytes; i++) {
        (*blob)[i] = gen64() & 0xff;
    }

    // construct src data.
    const char* p = blob->data();
    for (size_t i = 0; i < size; i++) {
        src_data->emplace_back(Slice{.data = p, .size = BYTE_SIZE});
        p += (BYTE_SIZE + GAP_SIZE);
    }
}

void binary_to_int128(const std::vector<Slice>& src_data, std::vector<int128_t>& dst_data) {
    size_t size = src_data.size();
    for (size_t i = 0; i < size; i++) {
        const Slice& s = src_data[i];
        int128_t value = s.data[0] & 0x80 ? -1 : 0;
        memcpy(reinterpret_cast<char*>(&value) + sizeof(value) - s.size, s.data, s.size);
        value = ToHost128(value);
        dst_data[i] = value;
    }
    return;
}

static void run_binary_to_int128(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::string blob;
    size_t size = state.range(0);
    std::vector<Slice> src_data;
    std::vector<int128_t> dst_data(size);
    make_src_data(size, &blob, &src_data);

    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        binary_to_int128(src_data, dst_data);
    }
}

void binary_to_int128_fixed(const std::vector<Slice>& src_data, std::vector<int128_t>& dst_data) {
    size_t size = src_data.size();
    for (size_t i = 0; i < size; i++) {
        const Slice& s = src_data[i];
        int128_t value = s.data[0] & 0x80 ? -1 : 0;
        memcpy(reinterpret_cast<char*>(&value) + sizeof(value) - 7, s.data, 7);
        value = ToHost128(value);
        dst_data[i] = value;
    }
    return;
}

static void run_binary_to_int128_fixed(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::string blob;
    size_t size = state.range(0);
    std::vector<Slice> src_data;
    std::vector<int128_t> dst_data(size);
    make_src_data(size, &blob, &src_data);

    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        binary_to_int128_fixed(src_data, dst_data);
    }
}

template <typename TYPE>
void binary_to_int128_ex(const std::vector<Slice>& src_data, std::vector<int128_t>& dst_data) {
    size_t size = src_data.size();
    for (size_t i = 0; i < size; i++) {
        const Slice& s = src_data[i];

        TYPE value = 0;
        memcpy((char*)&value, s.data, sizeof(TYPE));
        if constexpr (std::is_same_v<TYPE, int64_t>) {
            value = ToHost64(value);
        } else {
            value = ToHost128(value);
        }
        value = value >> ((sizeof(TYPE) - BYTE_SIZE) * 8);

        if constexpr ((BYTE_SIZE <= sizeof(TYPE)) && verify) {
            TYPE value2 = s.data[0] & 0x80 ? -1 : 0;
            memcpy(reinterpret_cast<char*>(&value2) + sizeof(value2) - BYTE_SIZE, s.data, BYTE_SIZE);
            if constexpr (std::is_same_v<TYPE, int64_t>) {
                value2 = ToHost64(value2);
            } else {
                value2 = ToHost128(value2);
            }
            if (value != value2) {
                printf("FAILED at %s. v = %p, v2 = %p, raw = ", __func__, value, value2);
                for (int j = 0; j < BYTE_SIZE; j++) {
                    printf("%x ", s.data[j]);
                }
                printf("\n");
                exit(-1);
            }
        }
        dst_data[i] = value;
    }
    return;
}

static void run_binary_to_int128_ex(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::string blob;
    size_t size = state.range(0);
    std::vector<Slice> src_data;
    std::vector<int128_t> dst_data(size);
    make_src_data(size, &blob, &src_data);

    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        binary_to_int128_ex<int64_t>(src_data, dst_data);
    }
}

static void run_binary_to_int128_ex_128(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::string blob;
    size_t size = state.range(0);
    std::vector<Slice> src_data;
    std::vector<int128_t> dst_data(size);
    make_src_data(size, &blob, &src_data);

    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        binary_to_int128_ex<int128_t>(src_data, dst_data);
    }
}

static constexpr size_t N = 1000000;
BENCHMARK(run_binary_to_int128)->Args({N});
BENCHMARK(run_binary_to_int128_fixed)->Args({N});
BENCHMARK(run_binary_to_int128_ex)->Args({N});
BENCHMARK(run_binary_to_int128_ex_128)->Args({N});
