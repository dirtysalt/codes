#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = nums[0] - k - 1
        ans = 0
        for i in range(len(nums)):
            # (nums[i] - k, nums[i] + k)
            exp = prev + 1
            a, b = nums[i] - k, nums[i] + k
            if exp < a:
                ans += 1
                prev = a
            elif a <= exp <= b:
                ans += 1
                prev = exp
            else:
                pass
        return ans


if __name__ == '__main__':
    pass
