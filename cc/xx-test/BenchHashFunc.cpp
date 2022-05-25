#include <benchmark/benchmark.h>
#include <functional>

std::vector<int32_t> ConstructRandomSet(int64_t size) {
    std::vector<int32_t> a;
    a.reserve(size);
    for (size_t i = 0; i < size; ++i) {
        a.emplace_back(i);
    }
    return a;
}

static const int N = 10000;

static void stdhash(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<int32_t> a;
    for (auto _ : state) {
        state.PauseTiming();
        a = ConstructRandomSet(state.range(0));
        int32_t* p = a.data();
        state.ResumeTiming();
        size_t acc = 0;
        for (size_t i = 0; i < state.range(0); ++i) {
            acc += std::hash<int>()(p[i]);
        }
    }
}
// Register the function as a benchmark
BENCHMARK(stdhash)->Arg(N);


#define FORCE_INLINE inline __attribute__((always_inline))

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

void inline_murmur_hash3_x64_64(const void* key, const int len, const uint64_t seed, void* out) {
    const uint8_t* data = (const uint8_t*)key;
    const int nblocks = len / 8;
    uint64_t h1 = seed;

    const uint64_t c1 = BIG_CONSTANT(0x87c37b91114253d5);
    const uint64_t c2 = BIG_CONSTANT(0x4cf5ad432745937f);

    // //----------
    // // body

    // const uint64_t* blocks = (const uint64_t*)(data);

    // for (int i = 0; i < nblocks; i++) {
    //     uint64_t k1 = getblock64(blocks, i);

    //     k1 *= c1;
    //     k1 = ROTL64(k1, 31);
    //     k1 *= c2;
    //     h1 ^= k1;

    //     h1 = ROTL64(h1, 27);
    //     h1 = h1 * 5 + 0x52dce729;
    // }

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

static void inline_murmurhash(benchmark::State& state) {
    // Code inside this loop is measured repeatedly
    std::vector<int32_t> a;
    for (auto _ : state) {
        state.PauseTiming();
        a = ConstructRandomSet(state.range(0));
        int32_t* p = a.data();
        state.ResumeTiming();
        size_t acc = 0;
        for (size_t i = 0; i < state.range(0); ++i) {
            int64_t value = 0;
            inline_murmur_hash3_x64_64(p+i, sizeof(p[i]), 0x42, &value);
            acc += value;
        }
    }
}
// Register the function as a benchmark
BENCHMARK(inline_murmurhash)->Arg(N);
