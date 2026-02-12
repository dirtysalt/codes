#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> int:
        def rev(x):
            t = 0
            while x:
                t = t * 10 + x % 10
                x = x // 10
            return t

        MOD = 10 ** 9 + 7

        def diff(x):
            t = x - rev(x)
            return t

        from collections import Counter
        xs = [diff(x) for x in nums]
        cnt = Counter(xs)

        ans = 0
        for x in xs:
            ans += (cnt[x] - 1)
        ans = ans // 2
        return ans % MOD


if __name__ == '__main__':
    pass
