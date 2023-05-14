#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ans, M, px = 0, 0, 0
        nums.sort()
        for x in nums:
            M = 2 * M - px + x
            px = x
            c = x * x * M
            ans += c

        return ans % MOD


if __name__ == '__main__':
    pass
