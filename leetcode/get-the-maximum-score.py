#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        acc1 = nums1.copy()
        acc2 = nums2.copy()
        for i in range(1, n):
            acc1[i] += acc1[i - 1]
        for i in range(1, m):
            acc2[i] += acc2[i - 1]

        from collections import defaultdict
        cross = defaultdict(list)
        for i in range(n):
            cross[nums1[i]].append(i)
        for i in range(m):
            cross[nums2[i]].append(i)

        seq = [(-1, -1)]
        for k, xs in cross.items():
            if len(xs) == 2:
                seq.append(xs)
        seq.append((n - 1, m - 1))

        ans = 0
        for j in range(1, len(seq)):
            a, b = seq[j - 1][0] + 1, seq[j][0]
            c, d = seq[j - 1][1] + 1, seq[j][1]
            # sum(nums1[a+1 .. b]), sum(nums2[c+1 .. d])
            t0 = acc1[b] - (acc1[a - 1] if a != 0 else 0)
            t1 = acc2[d] - (acc2[c - 1] if c != 0 else 0)
            ans += max(t0, t1)
        MOD = 10 ** 9 + 7
        ans = ans % MOD
        return ans


cases = [
    ([2, 4, 5, 8, 10], [4, 6, 8, 9], 30),
    ([1, 4, 5, 8, 9, 11, 19], [2, 3, 4, 11, 12], 61),
    ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 40),
    ([1, 3, 5, 7, 9], [3, 5, 100], 109),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().maxSum, cases)
