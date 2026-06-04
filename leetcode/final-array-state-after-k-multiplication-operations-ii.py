#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # base = Solution2().getFinalState(nums, k, multiplier)
        # print(base)

        if multiplier == 1: return nums
        n = len(nums)

        arr = nums.copy()
        M = max(nums)
        todo = 0
        for i in range(n):
            x = nums[i]
            while x < M:
                x = x * multiplier
                todo += 1
            arr[i] = x

        if todo >= k:
            return Solution2().getFinalState(nums, k, multiplier)

        def pow(a, b, mod):
            r = 1
            while b:
                if b & 0x1:
                    r = (r * a) % mod
                a = (a * a) % mod
                b = b >> 1
            return r

        MOD = 10 ** 9 + 7
        k -= todo
        rep, k = k // n, k % n
        idx = list(range(n))
        idx.sort(key=lambda x: arr[x])
        for i in range(n):
            r = rep
            if i < k: r += 1
            j = idx[i]
            arr[j] = arr[j] * pow(multiplier, r, MOD)
            arr[j] = arr[j] % MOD
        return arr


class Solution2:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD = 10 ** 9 + 7
        import heapq
        q = []
        for i in range(len(nums)):
            q.append((nums[i], i))
        heapq.heapify(q)

        ans = [0] * len(nums)
        for _ in range(k):
            (x, idx) = heapq.heappop(q)
            heapq.heappush(q, (x * multiplier, idx))

        for (x, idx) in q:
            ans[idx] = x % MOD
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[2, 1, 3, 5, 6], k=5, multiplier=2, res=[8, 4, 6, 5, 6]),
    aatest_helper.OrderedDict(nums=[100000, 2000], k=2, multiplier=1000000, res=[999999307, 999999993]),
    aatest_helper.OrderedDict(nums=[2, 1, 3, 5, 6], k=10000, multiplier=2,
                              res=[996874050, 498437025, 247655534, 873046283, 247655534]),
]

aatest_helper.run_test_cases(Solution().getFinalState, cases)

if __name__ == '__main__':
    pass
