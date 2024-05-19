#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        count = [[0] * 10 for _ in range(10)]
        total = [0] * 10
        for x in nums:
            i = 0
            while x:
                count[i][x % 10] += 1
                total[i] += 1
                x = x // 10
                i += 1

        ans = 0
        for x in nums:
            i = 0
            while x:
                ans += total[i] - count[i][x % 10]
                i += 1
                x = x // 10
        return ans // 2


if __name__ == '__main__':
    pass
