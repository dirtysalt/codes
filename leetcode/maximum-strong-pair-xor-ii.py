#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        MAXB = 20
        N = 1 << MAXB
        tree = [0] * (2 * N)

        def update(x, v):
            p = N + x
            tree[p] = v
            while p != 1:
                p2 = p // 2
                tree[p2] = tree[2 * p2] + tree[2 * p2 + 1]
                p = p2

        def search(x):
            p = 1
            if tree[p] == 0: return 0
            for i in reversed(range(MAXB)):
                b = x & (1 << i)
                if b:
                    if tree[2 * p]:
                        p = 2 * p
                    else:
                        p = 2 * p + 1
                else:
                    if tree[2 * p + 1]:
                        p = 2 * p + 1
                    else:
                        p = 2 * p
            assert (tree[p])
            return (p - N) ^ x

        j, k = 0, 0
        ans = 0
        for i in range(len(nums)):
            while j < i:
                update(nums[j], 0)
                j += 1
            while k < len(nums) and nums[k] <= 2 * nums[i]:
                update(nums[k], 1)
                k += 1
            r = search(nums[i])
            ans = max(ans, r)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4, 5], 7),
    ([10, 100], 0),
    ([500, 520, 2500, 3000], 1020),
]

aatest_helper.run_test_cases(Solution().maximumStrongPairXor, cases)

if __name__ == '__main__':
    pass
