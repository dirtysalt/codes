#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans = 0
        for x in range(1, 100 + 1):
            for a, b in nums:
                if a <= x <= b:
                    ans += 1
                    break
        return ans


if __name__ == '__main__':
    pass
