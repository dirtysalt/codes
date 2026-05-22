#include <benchmark/benchmark.h>
#include <fcntl.h>
#include <zlib.h>

#include <cstring>

#include "Common.h"

const int REP = 100;

static void test_checksum_disk_data_crc32(benchmark::State& state) {
    size_t n = state.range(0);
    std::vector<uint8_t> data(n);
    uint8_t* buf = data.data();
    memset(buf, 'X', n);

    const char* fname = "./checksum.data";
    int fd = open(fname, O_RDWR | O_TRUNC | O_CREAT, 0666);
    (void)write(fd, buf, n);

    // Code inside this loop is measured repeatedly
    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        for (int i = 0; i < REP; i++) {
            (void)read(fd, buf, n);
            uint32_t c = crc32(0, buf, n);
            benchmark::DoNotOptimize(c);
        }
    }

    close(fd);
    unlink(fname);
}

static void test_checksum_mem_data_crc32(benchmark::State& state) {
    size_t n = state.range(0);
    std::vector<uint8_t> data(n);
    uint8_t* buf = data.data();
    memset(buf, 'X', n);

    // Code inside this loop is measured repeatedly
    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        for (int i = 0; i < REP; i++) {
            uint32_t c = crc32(0, buf, n);
            benchmark::DoNotOptimize(c);
        }
    }
}

static void test_checksum_mem_data_mmh(benchmark::State& state) {
    size_t n = state.range(0);
    std::vector<uint8_t> data(n);
    uint8_t* buf = data.data();
    memset(buf, 'X', n);

    // Code inside this loop is measured repeatedly
    for (auto _ : state) {
        // state.PauseTiming();
        // state.ResumeTiming();
        for (int i = 0; i < REP; i++) {
            uint64_t c = 0;
            inline_murmur_hash3_x64_64(buf, n, 0, &c);
            benchmark::DoNotOptimize(c);
        }
    }
}

// Register the function as a benchmark
static const int N0 = 4096;
static const int N1 = 1048576;
static const int N2 = 8388608;

BENCHMARK(test_checksum_disk_data_crc32)->Arg(N0)->Arg(N1)->Arg(N2);
BENCHMARK(test_checksum_mem_data_crc32)->Arg(N0)->Arg(N1)->Arg(N2);
BENCHMARK(test_checksum_mem_data_mmh)->Arg(N0)->Arg(N1)->Arg(N2);
