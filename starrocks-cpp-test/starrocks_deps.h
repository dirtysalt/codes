/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdlib>

#include "phmap/phmap.h"

namespace starrocks::vectorized {
template <int n>
struct phmap_mix {
    inline size_t operator()(size_t) const;
};

template <>
class phmap_mix<4> {
public:
    inline size_t operator()(size_t a) const {
        static constexpr uint64_t kmul = 0xcc9e2d51UL;
        uint64_t l = a * kmul;
        return static_cast<size_t>(l ^ (l >> 32u));
    }
};

template <>
class phmap_mix<8> {
public:
    // Very fast mixing (similar to Abseil)
    inline size_t operator()(size_t a) const {
        static constexpr uint64_t k = 0xde5fb9d2630458e9ULL;
        uint64_t h;
        uint64_t l = umul128(a, k, &h);
        return static_cast<size_t>(h + l);
    }
};

template <class T>
class StdHash {
public:
    std::size_t operator()(T value) const { return phmap_mix<sizeof(size_t)>()(std::hash<T>()(value)); }
};

template <typename T>
using HashSet = phmap::flat_hash_set<T, StdHash<T>>;

}; // namespace starrocks::vectorized
