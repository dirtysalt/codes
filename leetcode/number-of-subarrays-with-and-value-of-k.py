#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countSubarrays2(self, nums: List[int], k: int) -> int:
        # note: this is to count sequence not array.
        BITS = 32

        import functools
        @functools.cache
        def dfs(i, x):
            if i == len(nums):
                return x == k

            ans = dfs(i + 1, x)
            tmp = nums[i] & x
            ok = True
            for b in range(BITS):
                if ((k & (1 << b)) == 1) and ((tmp & (1 << b)) == 0):
                    ok = False
                    break
            if ok:
                ans += dfs(i + 1, tmp)
            return ans

        ans = dfs(0, (1 << BITS) - 1)
        return ans

    def countSubarrays(self, nums: List[int], k: int) -> int:
        BITS = 32

        def fail(x):
            # more elegent way ?
            for b in range(BITS):
                if k & (1 << b) and ((x & (1 << b)) == 0):
                    return True
            return False

        def find(arr):
            n = len(arr)

            acc = [[0] * BITS for _ in range(n + 1)]
            for i in range(n):
                x = arr[i]
                for b in range(BITS):
                    if x & (1 << b):
                        acc[i + 1][b] = acc[i][b] + 1

            def range_value(s, e):
                res = 0
                for b in range(BITS):
                    if acc[e + 1][b] - acc[s][b] == (e - s + 1):
                        res = res | (1 << b)
                return res

            ans = 0
            p = 0
            for i in range(n):
                while p < n and range_value(i, p) != k:
                    p += 1
                if p == n: break
                ans += (n - p)
            return ans

        n = len(nums)
        i, ans = 0, 0
        while i < n:
            val = (1 << BITS) - 1
            j = i
            while j < n:
                val = val & nums[j]
                if fail(val): break
                j += 1
            ans += find(nums[i:j])
            i = j + 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 1, 1, ], 1, 6),
    ([1, 1, 2], 1, 3),
    ([1, 2, 3, ], 2, 2),
    ([1, 9, 9, 7, 4], 1, 6)
]

aatest_helper.run_test_cases(Solution().countSubarrays, cases)

if __name__ == '__main__':
    pass
