#ifdef HAS_RESERVED_IDENTIFIER
#pragma clang diagnostic ignored "-Wreserved-identifier"
#endif

#include <Common/Stopwatch.h>
#include <base/defines.h>
#include <dlfcn.h>

#include <boost/program_options.hpp>
#include <iomanip>
#include <iostream>
#include <memory>
#include <pcg_random.hpp>
#include <random>
#include <string>
#include <thread>

#include "memcpy-impl.h"

template <typename F, typename MemcpyImpl>
void NO_INLINE loop(uint8_t* dst, uint8_t* src, size_t size, F&& chunk_size_distribution, MemcpyImpl&& impl) {
    while (size) {
        size_t bytes_to_copy = std::min<size_t>(size, chunk_size_distribution());

        impl(dst, src, bytes_to_copy);

        dst += bytes_to_copy;
        src += bytes_to_copy;
        size -= bytes_to_copy;

        /// Execute at least one SSE instruction as a penalty after running AVX code.
        __asm__ __volatile__("pxor %%xmm15, %%xmm15" ::: "xmm15");
    }
}

using RNG = pcg32_fast;

template <size_t N>
size_t generatorUniform(RNG& rng) {
    return rng() % N;
};

template <typename F, typename MemcpyImpl>
uint64_t test(uint8_t* dst, uint8_t* src, size_t size, size_t iterations, size_t num_threads, F&& generator,
              MemcpyImpl&& impl, const char* name) {
    Stopwatch watch;

    std::vector<std::thread> threads;
    threads.reserve(num_threads);

    for (size_t thread_num = 0; thread_num < num_threads; ++thread_num) {
        size_t begin = size * thread_num / num_threads;
        size_t end = size * (thread_num + 1) / num_threads;

        threads.emplace_back([begin, end, iterations, &src, &dst, &generator, &impl] {
            for (size_t iteration = 0; iteration < iterations; ++iteration) {
                loop(
                        iteration % 2 ? &src[begin] : &dst[begin], iteration % 2 ? &dst[begin] : &src[begin],
                        end - begin, [rng = RNG(), &generator]() mutable { return generator(rng); },
                        std::forward<MemcpyImpl>(impl));
            }
        });
    }

    for (auto& thread : threads) thread.join();

    uint64_t elapsed_ns = watch.elapsed();

    /// Validation
    for (size_t i = 0; i < size; ++i)
        if (dst[i] != uint8_t(i)) throw std::logic_error("Incorrect result");

    std::cout << name;
    return elapsed_ns;
}

#define VARIANT(N, NAME)       \
    if (memcpy_variant == (N)) \
        return test(dst, src, size, iterations, num_threads, std::forward<F>(generator), NAME, #NAME);

template <typename F>
uint64_t dispatchMemcpyVariants(size_t memcpy_variant, uint8_t* dst, uint8_t* src, size_t size, size_t iterations,
                                size_t num_threads, F&& generator) {
    memcpy_type memcpy_libc_old = reinterpret_cast<memcpy_type>(dlsym(RTLD_NEXT, "memcpy"));

    VARIANT(1, memcpy)
    VARIANT(2, memcpy_trivial)
    VARIANT(3, memcpy_libc_old)
    VARIANT(4, memcpy_erms)
    VARIANT(5, memcpy_jart)
    VARIANT(6, memcpySSE2)
    VARIANT(7, memcpySSE2Unrolled2)
    VARIANT(8, memcpySSE2Unrolled4)
    VARIANT(9, memcpySSE2Unrolled8)
    VARIANT(10, memcpy_fast_sse)
    VARIANT(11, memcpy_fast_avx)
    VARIANT(12, memcpy_my)
    VARIANT(13, memcpy_my2)

    VARIANT(21, __memcpy_erms)
    VARIANT(22, __memcpy_sse2_unaligned)
    VARIANT(23, __memcpy_ssse3)
    VARIANT(24, __memcpy_ssse3_back)
    VARIANT(25, __memcpy_avx_unaligned)
    VARIANT(26, __memcpy_avx_unaligned_erms)
    VARIANT(27, __memcpy_avx512_unaligned)
    VARIANT(28, __memcpy_avx512_unaligned_erms)
    VARIANT(29, __memcpy_avx512_no_vzeroupper)

    return 0;
}

uint64_t dispatchVariants(size_t memcpy_variant, size_t generator_variant, uint8_t* dst, uint8_t* src, size_t size,
                          size_t iterations, size_t num_threads) {
    if (generator_variant == 1)
        return dispatchMemcpyVariants(memcpy_variant, dst, src, size, iterations, num_threads, generatorUniform<16>);
    if (generator_variant == 2)
        return dispatchMemcpyVariants(memcpy_variant, dst, src, size, iterations, num_threads, generatorUniform<256>);
    if (generator_variant == 3)
        return dispatchMemcpyVariants(memcpy_variant, dst, src, size, iterations, num_threads, generatorUniform<4096>);
    if (generator_variant == 4)
        return dispatchMemcpyVariants(memcpy_variant, dst, src, size, iterations, num_threads, generatorUniform<65536>);
    if (generator_variant == 5)
        return dispatchMemcpyVariants(memcpy_variant, dst, src, size, iterations, num_threads,
                                      generatorUniform<1048576>);

    return 0;
}

int main(int argc, char** argv) {
    boost::program_options::options_description desc("Allowed options");
    desc.add_options()("help,h", "produce help message")(
            "size", boost::program_options::value<size_t>()->default_value(1000000),
            "Bytes to copy on every iteration")("iterations", boost::program_options::value<size_t>(),
                                                "Number of iterations")(
            "threads", boost::program_options::value<size_t>()->default_value(1), "Number of copying threads")(
            "distribution", boost::program_options::value<size_t>()->default_value(4),
            "Distribution of chunk sizes to perform copy")("variant", boost::program_options::value<size_t>(),
                                                           "Variant of memcpy implementation")(
            "tsv", "Print result in tab-separated format");

    boost::program_options::variables_map options;
    boost::program_options::store(boost::program_options::parse_command_line(argc, argv, desc), options);

    if (options.count("help") || !options.count("variant")) {
        std::cout << R"(Usage:

for size in 4096 16384 50000 65536 100000 1000000 10000000 100000000; do
    for threads in 1 2 4 $(($(nproc) / 2)) $(nproc); do
        for distribution in 1 2 3 4 5; do
            for variant in {1..13} {21..29}; do
                for i in {1..10}; do
                    ./ck-memcpy-bench.exe --tsv --size $size --variant $variant --threads $threads --distribution $distribution;
                done;
            done;
        done;
    done;
done | tee result.tsv

clickhouse-local --structure '
    name String,
    size UInt64,
    iterations UInt64,
    threads UInt16,
    generator UInt8,
    memcpy UInt8,
    elapsed UInt64
' --query "
    SELECT
        size, name,
        avg(1000 * elapsed / size / iterations) AS s,
        count() AS c
    FROM table
    GROUP BY size, name
    ORDER BY size ASC, s DESC
" --output-format PrettyCompact < result.tsv

)" << std::endl;
        std::cout << desc << std::endl;
        return 1;
    }

    size_t size = options["size"].as<size_t>();
    size_t num_threads = options["threads"].as<size_t>();
    size_t memcpy_variant = options["variant"].as<size_t>();
    size_t generator_variant = options["distribution"].as<size_t>();

    size_t iterations;
    if (options.count("iterations")) {
        iterations = options["iterations"].as<size_t>();
    } else {
        iterations = 10000000000ULL / size;

        if (generator_variant == 1) iterations /= 10;
    }

    std::unique_ptr<uint8_t[]> src(new uint8_t[size]);
    std::unique_ptr<uint8_t[]> dst(new uint8_t[size]);

    /// Fill src with some pattern for validation.
    for (size_t i = 0; i < size; ++i) src[i] = i;

    /// Fill dst to avoid page faults.
    memset(dst.get(), 0, size);

    uint64_t elapsed_ns =
            dispatchVariants(memcpy_variant, generator_variant, dst.get(), src.get(), size, iterations, num_threads);

    std::cout << std::fixed << std::setprecision(3);

    if (options.count("tsv")) {
        std::cout << '\t' << size << '\t' << iterations << '\t' << num_threads << '\t' << generator_variant << '\t'
                  << memcpy_variant << '\t' << elapsed_ns << '\n';
    } else {
        std::cout << ": " << num_threads << " threads, "
                  << "size: " << size << ", distribution " << generator_variant << ", processed in "
                  << (elapsed_ns / 1e9) << " sec, " << (size * iterations * 1.0 / elapsed_ns) << " GB/sec\n";
    }

    return 0;
}
