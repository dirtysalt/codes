#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        a, b = 0, 0
        for x in nums:
            if x > 0:
                a += 1
            elif x < 0:
                b += 1
        return max(a, b)


if __name__ == '__main__':
    pass
