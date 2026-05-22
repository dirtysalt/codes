#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bits = 30
        acc = [[0] * bits for _ in range(n + 1)]
        for i, x in enumerate(nums):
            for j in range(bits):
                if x & (1 << j):
                    acc[i + 1][j] += 1
                acc[i + 1][j] += acc[i][j]

        def get_range(l, r):
            sz = r - l + 1
            ans = 0
            for j in range(bits):
                if acc[r + 1][j] - acc[l][j] == sz:
                    ans |= (1 << j)
            return ans

        # find the largest one smaller than k
        def B():
            r = 0
            ans = 1 << 63
            for l, x in enumerate(nums):
                while r < len(nums):
                    v = get_range(l, r)
                    if v <= k:
                        # print(l, r, v)
                        ans = min(ans, k - v)
                        break
                    r += 1
            return ans

        # find the smallest one larger than k
        def A():
            l = 0
            ans = 1 << 63
            for r, x in enumerate(nums):
                while l <= r:
                    v = get_range(l, r)
                    if v >= k:
                        # print(l, r, v)
                        ans = min(ans, v - k)
                        break
                    l += 1
            return ans

        return min(A(), B())


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 4, 5], 3, 1),
    ([1, 2, 1, 2], 2, 0),
    ([1], 10, 9),
    ([4, 1], 6, 2),
    ([1, 8], 10, 2),
]

aatest_helper.run_test_cases(Solution().minimumDifference, cases)

if __name__ == '__main__':
    pass
