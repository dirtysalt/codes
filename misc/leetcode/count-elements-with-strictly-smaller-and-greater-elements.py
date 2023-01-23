#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        a, b = nums[0], nums[-1]
        ans = 0
        for x in nums:
            if x == a or x == b:
                continue
            ans += 1
        return ans


if __name__ == '__main__':
    pass
