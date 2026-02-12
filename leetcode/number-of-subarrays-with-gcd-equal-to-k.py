#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        n = len(nums)
        for i in range(n):
            t = nums[i]
            if t == k:
                ans += 1
            for j in range(i + 1, n):
                t = gcd(t, nums[j])
                if t == k:
                    ans += 1
        return ans


if __name__ == '__main__':
    pass
