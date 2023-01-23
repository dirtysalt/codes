#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] or nums[i] == nums[k] or nums[j] == nums[k]:
                        pass
                    else:
                        ans += 1
        return ans


if __name__ == '__main__':
    pass
