#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 00 -> 10
# 010 -> 001 -> 101
# 0110 -> 0101 -> 0010 -> 1010
# 01110 -> 01101 -> 01011 -> 00111 -> 10111
# 011100 -> 101110 -> 1101111
# 0101 -> 0011 -> 1011

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        res = []
        i = 0
        n = len(binary)

        # search first 0.
        while i < n and binary[i] == '1':
            i += 1
        res.append(binary[:i])

        first = i
        # search next 0
        i += 1
        while i < n and binary[i] == '1':
            i += 1
        second = i
        while second < n:
            res.append('1')
            first += 1
            second += 1
            while second < n and binary[second] == '1':
                second += 1

        if first < n:
            res.append('0')
            res.append('1' * (n - 1 - first))

        ans = ''.join(res)
        return ans


cases = [
    ("000110", "111011"),
    ("01", "01")
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumBinaryString, cases)
