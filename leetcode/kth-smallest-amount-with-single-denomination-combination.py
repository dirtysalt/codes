#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        def precompute():
            ops = []
            n = len(coins)
            for sz in range(1, n + 1):
                import itertools
                op = []
                for xs in itertools.combinations(coins, sz):
                    l = 1
                    for x in xs:
                        l = lcm(x, l)
                    op.append(l)
                ops.append(op)
            return ops

        ops = precompute()

        def test(value):
            res = 0
            for idx, op in enumerate(ops):
                sign = 1 if idx % 2 == 0 else -1
                r = 0
                for x in op:
                    r += value // x
                res += r * sign
            return res

        coins.sort()
        s, e = 0, k * coins[-1]
        while s <= e:
            m = (s + e) // 2
            r = test(m)
            # print(m, r)
            if r >= k:
                e = m - 1
            else:
                s = m + 1
        return s


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 6, 9], 3, 9),
    ([5, 2, ], 7, 12),
    ([6, 1, 2, 4], 4, 4),
    ([4, 1, 7, 6], 7, 7),
    ([23, 10, 5, 16, 21, 11, 19, 18], 98125, 223509)
]

aatest_helper.run_test_cases(Solution().findKthSmallest, cases)

if __name__ == '__main__':
    pass
