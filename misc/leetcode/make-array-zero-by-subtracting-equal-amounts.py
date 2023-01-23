#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        while True:
            nums = [x for x in nums if x > 0]
            nums.sort()
            if not nums or nums[0] == 0:
                break
            t = nums[0]
            nums = [x - t for x in nums]
            ans += 1
        return ans


if __name__ == '__main__':
    pass
