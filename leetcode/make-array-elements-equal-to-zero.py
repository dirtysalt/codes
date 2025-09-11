#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s = sum(nums)
        ans = 0
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                right = s - left
                d = abs(right - left)
                if d == 1:
                    ans += 1
                elif d == 0:
                    ans += 2
            else:
                left += nums[i]
        return ans


if __name__ == '__main__':
    pass
