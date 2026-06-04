/*
 * Copyright (C) dirlt
 */

#ifndef __CC_SHARE_SERIALIZER_H__
#define __CC_SHARE_SERIALIZER_H__

#include <string>
#include "share/byte_array.h"
#include "share/compress.h"
#include "share/utils.h"

namespace share {
namespace serializer {

// ------------------------------------------------------------
class Serializable {
public:
    virtual bool serialize(WriteableByteArray* bytes) const = 0;
    virtual bool deserialize(ReadableByteArray* bytes) = 0;
    virtual ~Serializable() {}
}; // class Serializable

// ------------------------------------------------------------
template<typename T>
class Stream {
public:
    bool out(const T& x, WriteableByteArray* bytes) const {
        return x.serialize(bytes);
    }
    bool in(T* x, ReadableByteArray* bytes) {
        return x->deserialize(bytes);
    }
}; // class Stream

// ------------------------------------------------------------
#define CC_SHARE_SERIALIZER_ENUM_TYPE(type)                    \
    template<>                                                            \
    class Stream<type> {                                                  \
    public:                                                              \
        bool out(const type& x,WriteableByteArray* bytes) const{             \
            return serialize(x,bytes);                                         \
        }                                                                    \
        bool in(type* x,ReadableByteArray* bytes) const{                     \
            return deserialize(x,bytes);                                      \
        }                                                                    \
    }

// --------------------uint64_t--------------------
static inline bool serialize(const uint64_t u, WriteableByteArray* bytes) {
    return compress_uint64(bytes, u);
}
static inline bool deserialize(uint64_t* u, ReadableByteArray* bytes) {
    return decompress_uint64(bytes, u);
}
CC_SHARE_SERIALIZER_ENUM_TYPE(uint64_t);

// --------------------int64_t--------------------
static inline bool serialize(const int64_t u, WriteableByteArray* bytes) {
    return compress_int64(bytes, u);
}
static inline bool deserialize(int64_t* u, ReadableByteArray* bytes) {
    return decompress_int64(bytes, u);
}
CC_SHARE_SERIALIZER_ENUM_TYPE(int64_t);

// --------------------uint32_t--------------------
static inline bool serialize(const uint32_t u, WriteableByteArray* bytes) {
    return compress_uint64(bytes, u);
}
static inline bool deserialize(uint32_t* u, ReadableByteArray* bytes) {
    uint64_t x;
    bool ok = decompress_uint64(bytes, &x);
    if(ok) {
        *u = x;
    }
    return ok;
}
CC_SHARE_SERIALIZER_ENUM_TYPE(uint32_t);

// --------------------int32_t--------------------
static inline bool serialize(const int32_t u, WriteableByteArray* bytes) {
    return compress_int64(bytes, u);
}
static inline  bool deserialize(int32_t* u, ReadableByteArray* bytes) {
    int64_t x;
    bool ok = decompress_int64(bytes, &x);
    if(ok) {
        *u = x;
    }
    return ok;
}
CC_SHARE_SERIALIZER_ENUM_TYPE(int32_t);

// --------------------std::string--------------------
static inline bool serialize(const std::string& u, WriteableByteArray* bytes) {
    if(!serialize(static_cast<uint64_t>(u.size()), bytes)) {
        return false;
    }
    return bytes->write(reinterpret_cast<const Byte*>(u.data()), u.size());
}
static inline bool deserialize(std::string* u, ReadableByteArray* bytes) {
    uint64_t size;
    if(!deserialize(&size, bytes)) {
        return false;
    }
    u->resize(size);
    return bytes->read(reinterpret_cast<Byte*>(string_as_array(u)), size);
}
CC_SHARE_SERIALIZER_ENUM_TYPE(std::string);

#undef CC_SHARE_SERIALIZER_ENUM_TYPE

} // namespace serializer
} // namespace share

#endif // __CC_SHARE_SERIALIZER_H__
