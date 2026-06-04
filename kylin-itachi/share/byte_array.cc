/*
 * Copyright (C) dirlt
 */

#include "share/util.h"
#include "share/byte_array.h"
#include "share/logging.h"

namespace share {

// ------------------------------------------------------------
// ReadableByteArray Implementation
ReadableByteArray::ReadableByteArray(const Byte* bytes, ByteSize size):
    bytes_(bytes), size_(size), cur_(0) {
}

bool ReadableByteArray::read(Byte* bytes, ByteSize size) {
    if((cur_ + size) > size_) {
        return false;
    }
    if(bytes) {
        memcpy(bytes, bytes_ + cur_, size);
    }
    cur_ += size;
    return true;
}

const Byte* ReadableByteArray::remain(ByteSize* size) const {
    if(size) {
        *size = size_ - cur_;
    }
    return bytes_ + cur_;
}

const Byte* ReadableByteArray::data(ByteSize* size) const {
    if(size) {
        *size = size_;
    }
    return bytes_;
}

// ------------------------------------------------------------
// WriteableByteArray Implementation
WriteableByteArray::WriteableByteArray(bool user_free):
    user_free_(user_free), bytes_(small_), size_(kSmallBufferSize), cur_(0) {
    // if this buffer need user to free
    // we must do real allocation.
    if(user_free_) {
        bytes_ = NULL;
        size_ = 0;
    }
}

WriteableByteArray::~WriteableByteArray() {
    if(!user_free_ && bytes_ != small_) {
        free(bytes_);
    }
}

bool WriteableByteArray::write(const Byte* bytes, ByteSize size) {
    Byte* _bytes = allocate(size);
    if(!_bytes) {
        return false;
    }
    memcpy(_bytes, bytes, size);
    return true;
}

Byte* WriteableByteArray::allocate(ByteSize size) {
    if((cur_ + size) > size_) {
        if(size_ == 0) {
            size_ = kSmallBufferSize;
        }
        ByteSize next_size = size_ * 2;
        while((cur_ + size) > next_size) {
            next_size *= 2;
        }
        if(bytes_ == small_) {
            Byte* tmp = static_cast<Byte*>(malloc(next_size));
            if(tmp == NULL) {
                WARNING("malloc(%zu) failed(%s)", next_size, SERRNO);
                return NULL;
            }
            bytes_ = tmp;
            memcpy(bytes_, small_, cur_);
        } else {
            Byte* tmp = static_cast<Byte*>(realloc(bytes_, next_size));
            if(tmp == NULL) {
                WARNING("realloc(%p,%zu) failed(%s)", bytes_, next_size, SERRNO);
                return NULL;
            }
            bytes_ = tmp;
        }
        size_ = next_size;
    }
    Byte* addr = bytes_ + cur_;
    cur_ += size;
    return addr;
}

const Byte* WriteableByteArray::data(ByteSize* size) const {
    if(size) {
        *size = cur_;
    }
    return bytes_;
}

// ------------------------------------------------------------
// STLStringByteArray Implementation
STLStringByteArray::STLStringByteArray(std::string* s):
    ReadableByteArray(reinterpret_cast<const Byte*>(s->data()),
                      s->size()),
    s_(s) {
}

bool STLStringByteArray::read(Byte* bytes, ByteSize size) {
    return ReadableByteArray::read(bytes, size);
}

bool STLStringByteArray::write(const Byte* bytes, ByteSize size) {
    s_->append(reinterpret_cast<const char*>(bytes), size);
    return true;
}

const Byte* STLStringByteArray::data(ByteSize* size) const {
    const Byte* data = reinterpret_cast<const Byte*>(s_->data());
    if(size) {
        *size = s_->size();
    }
    return data;
}

const Byte* STLStringByteArray::remain(ByteSize* size) const {
    return ReadableByteArray::remain(size);
}

Byte* STLStringByteArray::allocate(ByteSize size) {
    ByteSize old_size = s_->size();
    s_->resize(old_size + size);
    char* addr = string_as_array(s_);
    return reinterpret_cast<Byte*>(addr + old_size);
}

} // namespace share
