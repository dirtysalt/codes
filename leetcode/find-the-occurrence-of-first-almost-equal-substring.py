#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z


class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        pre_z = z_function(pattern + s)
        suf_z = z_function(pattern[::-1] + s[::-1])
        suf_z.reverse()

        m = len(pattern)
        for i in range(m, len(s) + 1):
            if pre_z[i] + suf_z[i - 1] >= m - 1:
                return i - m
        return -1


if __name__ == '__main__':
    pass
