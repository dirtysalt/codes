#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        exp = len(set(nums))
        ans = 0
        for i in range(n):
            ss = set()
            for j in range(i, n):
                ss.add(nums[j])
                if len(ss) == exp:
                    ans += 1
        return ans


if __name__ == '__main__':
    pass
