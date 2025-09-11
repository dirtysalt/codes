#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    r = (nums[i] - nums[j]) * nums[k]
                    ans = max(ans, r)
        return ans


if __name__ == '__main__':
    pass
