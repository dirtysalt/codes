#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        INF = 1 << 30
        nums.sort(reverse=True)

        def tobit(x):
            c = 0
            while x != 1:
                c += 1
                x = x // 2
            return c

        bits = [tobit(x) for x in nums]

        T = []
        for i in reversed(range(32)):
            if target & (1 << i):
                T.append(i)

        @functools.cache
        def findNextPos(i, j):
            t = 1 << T[j]
            while i < len(bits):
                t -= nums[i]
                if t <= 0: break
                i += 1
            return i if t == 0 else len(bits)

        @functools.cache
        def search(i, j):
            if j == len(T): return 0
            if i == len(bits): return INF

            ans = search(i + 1, j)
            if bits[i] == T[j]:
                c = search(i + 1, j + 1)
                ans = min(ans, c)
            elif bits[i] > T[j]:
                for k in range(j, len(T)):
                    cost = bits[i] - T[k]
                    c = cost + search(i + 1, k + 1)
                    ans = min(ans, c)
            else:
                # bits[i] < T[j]
                nextPos = findNextPos(i, j)
                if nextPos < len(bits):
                    c = search(nextPos + 1, j + 1)
                    ans = min(ans, c)
            return ans

        ans = search(0, 0)
        if ans == INF: ans = -1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 8], 7, 1),
    ([1, 32, 1, 2], 12, 2),
    ([1, 32, 1], 35, -1),
    ([128, 1, 128, 1, 64], 4, 4),
    ([1, 1, 64], 4, 4),
]

aatest_helper.run_test_cases(Solution().minOperations, cases)

if __name__ == '__main__':
    pass
