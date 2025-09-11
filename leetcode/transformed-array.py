#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                j = (i + nums[i] + n) % n
                ans.append(nums[j])
            else:
                ans.append(0)
        return ans


if __name__ == '__main__':
    pass
