#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diff = []
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                diff.append(i)
        if len(diff) % 2 != 0:
            return -1

        INF = 1 << 30

        import functools
        @functools.cache
        def find(i, j):
            if i > j: return 0
            # i and i + 1
            ans = INF
            if True:
                d = diff[i + 1] - diff[i]
                c = min(d, x) + find(i + 2, j)
                ans = min(ans, c)
            if True:
                d = diff[j] - diff[j - 1]
                c = min(d, x) + find(i, j - 2)
                ans = min(ans, c)
            if True:
                d = diff[j] - diff[i]
                c = min(d, x) + find(i + 1, j - 1)
                ans = min(ans, c)
            return ans

        ans = find(0, len(diff) - 1)
        return ans


if __name__ == '__main__':
    pass
