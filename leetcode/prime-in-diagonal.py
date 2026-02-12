#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        def isprime(x):
            if x == 1: return False
            for z in range(2, x):
                if z * z > x: break
                if x % z == 0: return False
            return True

        ans = 0
        n = len(nums)
        for i in range(n):
            x = nums[i][i]
            if isprime(x):
                ans = max(ans, x)
            x = nums[i][n - 1 - i]
            if isprime(x):
                ans = max(ans, x)
        return ans


if __name__ == '__main__':
    pass
