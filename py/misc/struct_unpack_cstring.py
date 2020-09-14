#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

# parse 'Z' as null-terminated string.
import struct
def struct_unpack(fmt, data, offset):
    # first character indicates endian.
    endian = fmt[0]
    saved_fmt = ''
    data_offset = offset
    data_size = 0
    results = []
    for i in range(1, len(fmt)):
        if fmt[i] == 'Z':
            if saved_fmt:
                # print endian + saved_fmt, struct.calcsize(endian + saved_fmt)
                result = struct.unpack_from(endian + saved_fmt, data, data_offset)
                results.extend(result)
                data_offset += struct.calcsize(endian + saved_fmt)
                saved_fmt = ''
            pos = data[data_offset:].find(chr(0x0))
            assert(pos != -1)
            s = data[data_offset:data_offset + pos]
            # print s
            data_offset += pos + 1
            results.append(s)
        else:
            saved_fmt += fmt[i]
    if saved_fmt:
        # print endian + saved_fmt, struct.calcsize(endian + saved_fmt)
        result = struct.unpack_from(endian + saved_fmt, data, data_offset)
        results.extend(result)
        data_offset += struct.calcsize(endian + saved_fmt)
    return results, data_offset - offset
