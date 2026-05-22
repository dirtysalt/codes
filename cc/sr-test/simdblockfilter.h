/* coding:utf-8
 * Copyright (C) dirlt
 */

#pragma once
#include <emmintrin.h>
#include <immintrin.h>

#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <functional>

// Modify from https://github.com/FastFilter/fastfilter_cpp/blob/master/src/bloom/simd-block.h
// This is avx2 simd implementation for paper <<Cache-, Hash- and Space-Efficient Bloom Filters>>
class SimdBlockFilter {
public:
    // The filter is divided up into Buckets:
    static constexpr int BITS_SET_PER_BLOCK = 8;
    using Bucket = uint32_t[BITS_SET_PER_BLOCK];

    SimdBlockFilter() = default;

    ~SimdBlockFilter() noexcept { free(_directory); }

    SimdBlockFilter(const SimdBlockFilter& bf) = delete;
    SimdBlockFilter(SimdBlockFilter&& bf) noexcept;

    void init(size_t nums);

    void insert_hash(const uint64_t hash) noexcept {
        const uint32_t bucket_idx = hash & _directory_mask;
#ifdef __AVX2__
        const __m256i mask = make_mask(hash >> _log_num_buckets);
        __m256i* const bucket = &reinterpret_cast<__m256i*>(_directory)[bucket_idx];
        _mm256_store_si256(bucket, _mm256_or_si256(*bucket, mask));
#else
        uint32_t masks[BITS_SET_PER_BLOCK];
        make_mask(hash >> _log_num_buckets, masks);
        for (int i = 0; i < BITS_SET_PER_BLOCK; ++i) {
            _directory[bucket_idx][i] |= masks[i];
        }
#endif
    }

    void prefetch_hash(const uint64_t hash) {
        _mm_prefetch(reinterpret_cast<__m256i*>(_directory) + (hash & _directory_mask), _MM_HINT_NTA);
    }
    void prefetch_bucket(const uint32_t bucket) {
        _mm_prefetch(reinterpret_cast<__m256i*>(_directory) + bucket, _MM_HINT_NTA);
    }

    bool test_hash(const uint64_t hash) const noexcept {
        const uint32_t bucket_idx = hash & _directory_mask;
#ifdef __AVX2__
        const __m256i mask = make_mask(hash >> _log_num_buckets);
        const __m256i bucket = reinterpret_cast<__m256i*>(_directory)[bucket_idx];
        // We should return true if 'bucket' has a one wherever 'mask' does. _mm256_testc_si256
        // takes the negation of its first argument and ands that with its second argument. In
        // our case, the result is zero everywhere iff there is a one in 'bucket' wherever
        // 'mask' is one. testc returns 1 if the result is 0 everywhere and returns 0 otherwise.
        return _mm256_testc_si256(bucket, mask);
#else
        uint32_t masks[BITS_SET_PER_BLOCK];
        make_mask(hash >> _log_num_buckets, masks);
        for (int i = 0; i < BITS_SET_PER_BLOCK; ++i) {
            if ((_directory[bucket_idx][i] & masks[i]) == 0) {
                return false;
            }
        }
        return true;
#endif
    }
    uint32_t directory_mask() const { return _directory_mask; }

private:
    // The number of bits to set in a tiny Bloom filter block

    // For scalar version:
    void make_mask(uint32_t key, uint32_t* masks) const;

#ifdef __AVX2__
    // For simd version:
    __m256i make_mask(const uint32_t hash) const noexcept {
        // Load hash into a YMM register, repeated eight times
        __m256i hash_data = _mm256_set1_epi32(hash);
        // Multiply-shift hashing ala Dietzfelbinger et al.: multiply 'hash' by eight different
        // odd constants, then keep the 5 most significant bits from each product.
        const __m256i rehash = _mm256_setr_epi32(0x47b6137bU, 0x44974d91U, 0x8824ad5bU, 0xa2b7289dU, 0x705495c7U,
                                                 0x2df1424bU, 0x9efc4947U, 0x5c6bfb31U);
        hash_data = _mm256_mullo_epi32(rehash, hash_data);
        hash_data = _mm256_srli_epi32(hash_data, 27);
        const __m256i ones = _mm256_set1_epi32(1);
        // Use these 5 bits to shift a single bit to a location in each 32-bit lane
        return _mm256_sllv_epi32(ones, hash_data);
    }
#endif
    // log2(number of bytes in a bucket):
    static constexpr int LOG_BUCKET_BYTE_SIZE = 5;

    size_t get_alloc_size() const { return 1ull << (_log_num_buckets + LOG_BUCKET_BYTE_SIZE); }

    // Common:
    // log_num_buckets_ is the log (base 2) of the number of buckets in the directory:
    int _log_num_buckets;
    // directory_mask_ is (1 << log_num_buckets_) - 1
    uint32_t _directory_mask;
    Bucket* _directory = nullptr;
};

void SimdBlockFilter::init(size_t nums) {
    nums = std::max(1UL, nums);
    int log_heap_space = std::ceil(std::log2(nums));
    _log_num_buckets = std::max(1, log_heap_space - LOG_BUCKET_BYTE_SIZE);
    _directory_mask = (1ull << std::min(63, _log_num_buckets)) - 1;
    const size_t alloc_size = get_alloc_size();
    const int malloc_failed = posix_memalign(reinterpret_cast<void**>(&_directory), 64, alloc_size);
    if (malloc_failed) throw ::std::bad_alloc();
    memset(_directory, 0, alloc_size);
}

SimdBlockFilter::SimdBlockFilter(SimdBlockFilter&& bf) noexcept {
    _log_num_buckets = bf._log_num_buckets;
    _directory_mask = bf._directory_mask;
    _directory = bf._directory;
    bf._directory = nullptr;
}