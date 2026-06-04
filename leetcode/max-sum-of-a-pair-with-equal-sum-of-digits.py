#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(list)

        def tt(x):
            a = 0
            while x:
                a += x % 10
                x = x // 10
            return a

        for x in nums:
            t = tt(x)
            d[t].append(x)

        ans = -1
        for xs in d.values():
            xs.sort()
            if len(xs) >= 2:
                a = xs[-1] + xs[-2]
                ans = max(ans, a)
        return ans


if __name__ == '__main__':
    pass
