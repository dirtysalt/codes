#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import defaultdict
        nums = defaultdict(list)
        n = len(A)

        for i in range(n):
            x = A[i]
            nums[x].append(i)

        def find_next(exp, i):
            xs = nums[exp]
            s, e = 0, len(xs) - 1
            while s <= e:
                m = (s + e) // 2
                if xs[m] > i:
                    e = m - 1
                else:
                    s = m + 1
            # print(exp, xs, i, s)
            if s >= len(xs):
                return None
            return xs[s]

        visited = set()
        ans = 2
        for i in range(n):
            for j in range(i + 1, n):
                d = A[j] - A[i]
                if (i, j) in visited:
                    continue
                visited.add((i, d))
                sz = 2
                exp = A[j] + d
                k = j
                while True:
                    k2 = find_next(exp, k)
                    if k2 is None:
                        break
                    visited.add((k, k2))
                    sz += 1
                    exp += d
                    k = k2
                ans = max(ans, sz)
        return ans


cases = [
    (
        [44, 46, 22, 68, 45, 66, 43, 9, 37, 30, 50, 67, 32, 47, 44, 11, 15, 4, 11, 6, 20, 64, 54, 54, 61, 63, 23, 43, 3,
         12,
         51, 61, 16, 57, 14, 12, 55, 17, 18, 25, 19, 28, 45, 56, 29, 39, 52, 8, 1, 21, 17, 21, 23, 70, 51, 61, 21, 52,
         25,
         28], 6)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestArithSeqLength, cases)
