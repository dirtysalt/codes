#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        nums.sort()

        back = [0] * n
        size = [0] * n

        # 好像没有更好的办法来减少扫描次数
        for i in range(n):
            k = i
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if size[j] > size[k]:
                        k = j

            size[i] = size[k] + 1
            back[i] = k

        k = 0
        for i in range(n):
            if size[i] > size[k]:
                k = i

        ans = []
        while back[k] != k:
            ans.append(nums[k])
            k = back[k]
        ans.append(nums[k])
        ans = ans[::-1]
        return ans


import aatest_helper

cases = [
    ([1, 2, 3], [1, 2]),
    ([1, 2, 4, 8], [1, 2, 4, 8])
]

aatest_helper.run_test_cases(Solution().largestDivisibleSubset, cases)
