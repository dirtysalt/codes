#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        for b in range(32):
            c0, c1 = k & (1 << b), n & (1 << b)
            if c0 == 0 and c1 != 0:
                ans += 1
            if c0 != 0 and c1 == 0:
                return -1
        return ans


if __name__ == '__main__':
    pass
