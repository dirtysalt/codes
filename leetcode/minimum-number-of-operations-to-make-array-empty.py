#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def find(rep):
            if rep % 3 == 0:
                return rep // 3
            elif rep % 3 == 1:
                return (rep - 4) // 3 + 2
            else:
                return (rep // 3) + 1

        nums.sort()
        i, j = 0, 0
        ans = 0
        while i < len(nums):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            rep = j - i
            if rep < 2: return -1
            c = find(rep)
            # print(nums[i], c)
            ans += c
            i = j
        return ans


if __name__ == '__main__':
    pass
