#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for x in set(nums):
            if x > k:
                ans += 1
            elif x < k:
                return -1
        return ans


if __name__ == '__main__':
    pass
