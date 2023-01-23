#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def unpack_varint(bs, offset):
    ans = 0
    move = 0
    while True:
        b = bs[offset]
        offset += 1
        payload = b & 0x7f
        ans |= (payload << move)
        move += 7
        if (b >> 7) == 0:
            break
    return ans, offset


def pack_varint(bs, value):
    while value >= 128:
        x = value & 0x7f
        bs.append((1 << 7) | x)
        value = value >> 7
    bs.append(value)


bs = bytearray()
pack_varint(bs, 300)
print(bs)
ans, offset = unpack_varint(bs, 0)
assert offset == len(bs)
print(ans, offset)
