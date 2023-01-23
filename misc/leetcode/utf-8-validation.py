#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param data: an array of integers
    @return: whether it is a valid utf-8 encoding
    """

    def validUtf8(self, data):
        # Write your code here

        def check_rest(data, idx, size):
            if idx + size > len(data):
                return False
            for i in range(size - 1):
                if data[idx + 1 + i] & 0xc0 != 0x80:
                    return False
            return True

        if not data:
            return False

        acts = ((0x80, 0x0, 1),
                (0xe0, 0xc0, 2),
                (0xf0, 0xe0, 3),
                (0xf8, 0xf0, 4))
        idx = 0
        while idx < len(data):
            b = data[idx]
            ok = False
            for mask, exp, size in acts:
                if b & mask == exp:
                    if not check_rest(data, idx, size):
                        return False
                    idx += size
                    ok = True
                    break
            if not ok:
                return False
        return True
