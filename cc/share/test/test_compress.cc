/*
 * Copyright (C) dirlt
 */

#include <cassert>
#include "share/compress.h"
using namespace share;

int main() {
    char* buf = new char[10];
    const int range = 1;
    int64_t n = 0;

    // --------------------
    n = -(N_ONES_(int64_t, 63)) - 1;
    for(int i = 0; i < range; i++, n++) {
        int x = compress_int64(buf, 10, n);
        assert(x);
        int64_t expect;
        int y = decompress_int64(buf, 10, &expect);
        assert(expect == n);
        assert(x == y);
    }

    // --------------------
    n = -range;
    for(int i = 0; i < range; i++, n++) {
        int x = compress_int64(buf, 10, n);
        assert(x);
        int64_t expect;
        int y = decompress_int64(buf, 10, &expect);
        assert(expect == n);
        assert(x == y);
    }

    // --------------------
    n = 0;
    for(int i = 0; i < range; i++, n++) {
        int x = compress_int64(buf, 10, n);
        assert(x);
        int64_t expect;
        int y = decompress_int64(buf, 10, &expect);
        assert(expect == n);
        assert(x == y);
    }

    // --------------------
    n = N_ONES_(int64_t, 63) - range;
    for(int i = 0; i < range; i++, n++) {
        int x = compress_int64(buf, 10, n);
        assert(x);
        int64_t expect;
        int y = decompress_int64(buf, 10, &expect);
        assert(expect == n);
        assert(x == y);
    }

    delete [] buf;
}
