#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # O(lgn * N * n)
        # n = 10 ** 5, N = 32 lgn = 32
        n = len(nums)
        maxv = max(nums)
        N = 1
        while (1 << N) <= maxv:
            N += 1
        acc = [[0] * N for _ in range(n + 1)]

        def bits(x):
            cnt = [0] * N
            for i in range(N):
                if (x >> i) & 0x1:
                    cnt[i] += 1
            return cnt

        for i in range(n):
            x = nums[i]
            cnt = bits(x)
            for j in range(N):
                acc[i + 1][j] = acc[i][j] + cnt[j]

        def ok(i, j):
            for k in range(N):
                # i..j j+1 .. n-1
                a = acc[j + 1][k] - acc[i][k]
                b = acc[n][k] - acc[j + 1][k]
                if a == 0 and b > 0:
                    return False
            return True

        ans = []
        j = 0
        for i in range(n):
            j = max(j, i)
            while j < n and not ok(i, j): j += 1
            size = j - i + 1
            if j == n:
                size -= 1
            ans.append(size)
        return ans


true, false, null = True, False, None
cases = [
    ([1, 0, 2, 1, 3], [3, 3, 2, 2, 1]),
    ([1, 2], [2, 1]),
    ([1, 0], [1, 1]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().smallestSubarrays, cases)

if __name__ == '__main__':
    pass
