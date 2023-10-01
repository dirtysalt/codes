#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ss = set()
        i = len(nums) - 1
        while i >= 0:
            x = nums[i]
            i -= 1
            if x <= k:
                ss.add(x)
                if len(ss) == k:
                    break
        return len(nums) - 1 - i


if __name__ == '__main__':
    pass
