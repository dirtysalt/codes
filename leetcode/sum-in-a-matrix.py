#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for x in nums:
            x.sort()
        tmp = list(zip(*nums))
        ans = 0
        for x in tmp:
            ans += max(x)
        return ans


if __name__ == '__main__':
    pass
