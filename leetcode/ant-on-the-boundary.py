#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        r, ans = 0, 0
        for x in nums:
            r += x
            if r == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
