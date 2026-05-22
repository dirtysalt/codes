/*
 * Copyright (C) dirlt
 */

#ifndef __CC_SHARE_COMPRESS_H__
#define __CC_SHARE_COMPRESS_H__

#include <cassert>
#include "share/byte_array.h"
#include "share/util.h"
#include "share/fast_memcpy.h"

namespace share {

static inline uint64_t zigzag_encode(int64_t v) {
    return static_cast<uint64_t>((v << 1) ^ (v >> 63));
}

static inline int64_t zigzag_decode(uint64_t v) {
    return -static_cast<int64_t>(v & 1) ^ static_cast<int64_t>(v >> 1);
}

static inline int compress_uint64_size(uint64_t v) {
    if(v < (1ULL << 7)) return 1;
    if(v < (1ULL << 14)) return 2;
    if(v < (1ULL << 21)) return 3;
    if(v < (1ULL << 28)) return 4;
    if(v < (1ULL << 35)) return 5;
    if(v < (1ULL << 42)) return 6;
    if(v < (1ULL << 49)) return 7;
    if(v < (1ULL << 56)) return 8;
    return 9;
}

static inline int decompress_uint64_size(char x) {
    if((x & 0x1) == 0) return 1;
    if((x & 0x2) == 0) return 2;
    if((x & 0x4) == 0) return 3;
    if((x & 0x8) == 0) return 4;
    if((x & 0x10) == 0) return 5;
    if((x & 0x20) == 0) return 6;
    if((x & 0x40) == 0) return 7;
    if((x & 0x80) == 0) return 8;
    return 9;
}

static inline int compress_uint64(char* p, size_t s, uint64_t v) {
    if(v < (1ULL << 7)) {
        if(s < 1) {
            return 0;
        }
        v <<= 1;
        mfence_c();
        _fast_memcpy<1>(p, &v);
        return 1;
    }
    if(v < (1ULL << 14)) {
        if(s < 2) {
            return 0;
        }
        v = (v << 2) | 0x1;
        mfence_c();
        _fast_memcpy<2>(p, &v);
        return 2;
    }
    if(v < (1ULL << 21)) {
        if(s < 3) {
            return 0;
        }
        v = (v << 3) | 0x3;
        mfence_c();
        _fast_memcpy<3>(p, &v);
        return 3;
    }
    if(v < (1ULL << 28)) {
        if(s < 4) {
            return 0;
        }
        v = (v << 4) | 0x7;
        mfence_c();
        _fast_memcpy<4>(p, &v);
        return 4;
    }
    if(v < (1ULL << 35)) {
        if(s < 5) {
            return 0;
        }
        v = (v << 5) | 0xf;
        mfence_c();
        _fast_memcpy<5>(p, &v);
        return 5;
    }
    if(v < (1ULL << 42)) {
        if(s < 6) {
            return 0;
        }
        v = (v << 6) | 0x1f;
        mfence_c();
        _fast_memcpy<6>(p, &v);
        return 6;
    }
    if(v < (1ULL << 49)) {
        if(s < 7) {
            return 0;
        }
        v = (v << 7) | 0x3f;
        mfence_c();
        _fast_memcpy<7>(p, &v);
        return 7;
    }
    if(v < (1ULL << 56)) {
        if(s < 8) {
            return 0;
        }
        v = (v << 8) | 0x7f;
        mfence_c();
        _fast_memcpy<8>(p, &v);
        return 8;
    }
    if(s < 9) {
        return 0;
    }
    p[0] = 0xff;
    _fast_memcpy<8>(p + 1, &v);
    return 9;
}

static inline int compress_int64(char* p, size_t s, int64_t v) {
    return compress_uint64(p, s, zigzag_encode(v));
}

static inline int decompress_uint64(const char* p, size_t s, uint64_t* v) {
    if(s < 1) {
        return 0;
    }
    uint64_t tmp = 0;
    _fast_memcpy<1>(&tmp, p);
    mfence_c();
    if((tmp & 0x1) == 0) {
        *v = (tmp >> 1);
        return 1;
    }
    if((tmp & 0x2) == 0) {
        if(s < 2) {
            return 0;
        }
        _fast_memcpy<1>(reinterpret_cast<char*>(&tmp) + 1, p + 1);
        mfence_c();
        *v = (tmp >> 2);
        return 2;
    }
    if((tmp & 0x4) == 0) {
        if(s < 3) {
            return 0;
        }
        _fast_memcpy<2>(reinterpret_cast<char*>(&tmp) + 1, p + 1);
        mfence_c();
        *v = (tmp >> 3);
        return 3;
    }
    if((tmp & 0x8) == 0) {
        if(s < 4) {
            return 0;
        }
        _fast_memcpy<3>(reinterpret_cast<char*>(&tmp) + 1, p + 1);
        mfence_c();
        *v = (tmp >> 4);
        return 4;
    }
    if((tmp & 0x10) == 0) {
        if(s < 5) {
            return 0;
        }
        _fast_memcpy<4>(reinterpret_cast<char*>(&tmp) + 1, p + 1);
        mfence_c();
        *v = (tmp >> 5);
        return 5;
    }
    if((tmp & 0x20) == 0) {
        if(s < 6) {
            return 0;
        }
        _fast_memcpy<5>(reinterpret_cast<char*>(&tmp) + 1, p + 1);
        mfence_c();
        *v = (tmp >> 6);
        return 6;
    }
    if((tmp & 0x40) == 0) {
        if(s < 7) {
            return 0;
        }
        _fast_memcpy<6>(reinterpret_cast<char*>(&tmp) + 1, p + 1);
        mfence_c();
        *v = (tmp >> 7);
        return 7;
    }
    if((tmp & 0x80) == 0) {
        if(s < 8) {
            return 0;
        }
        _fast_memcpy<7>(reinterpret_cast<char*>(&tmp) + 1, p + 1);
        mfence_c();
        *v = (tmp >> 8);
        return 8;
    }
    assert(static_cast<uint8_t>(p[0]) == 0xff);
    _fast_memcpy<8>(reinterpret_cast<char*>(v), p + 1);
    return 9;
}

static inline int decompress_int64(const char* p, size_t s, int64_t* v) {
    uint64_t x;
    int code = decompress_uint64(p, s, &x);
    *v = zigzag_decode(x);
    return code;
}

// ------------------------------------------------------------

static inline bool compress_uint64(WriteableByteArray* bytes, uint64_t v) {
    char p[9];
    int s = compress_uint64(p, sizeof(p), v);
    return bytes->write(reinterpret_cast<const Byte*>(p), s);
}

static inline bool compress_int64(WriteableByteArray* bytes, int64_t v) {
    return compress_uint64(bytes, zigzag_encode(v));
}

static inline bool decompress_uint64(ReadableByteArray* bytes, uint64_t* v) {
    ByteSize size = 0;
    const Byte* p = bytes->remain(&size);
    int n = decompress_uint64(reinterpret_cast<const char*>(p), size, v);
    if(n == 0) {
        return false;
    }
    assert(bytes->read(NULL, n));
    return true;
}

static inline bool decompress_int64(ReadableByteArray* bytes, int64_t* v) {
    uint64_t x;
    if(!decompress_uint64(bytes, &x)) {
        return false;
    }
    *v = zigzag_decode(x);
    return true;
}

} // namespace share

#endif // __CC_SHARE_COMPRESS_H__
