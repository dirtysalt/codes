#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i - 1]: continue
            a = 0
            for j in reversed(range(i)):
                if nums[i] != nums[j]:
                    a = nums[j] - nums[i]
                    break
            if a == 0:
                continue
            b = 0
            for j in range(i + 1, len(nums)):
                if nums[i] != nums[j]:
                    b = nums[j] - nums[i]
                    break
            if b == 0:
                continue
            if a * b > 0:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
