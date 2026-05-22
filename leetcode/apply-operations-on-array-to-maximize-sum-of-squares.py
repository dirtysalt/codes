#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bits = [0] * 32

        for i in range(len(nums)):
            for j in range(32):
                if nums[i] & (1 << j):
                    bits[j] += 1

        # print(bits)
        MOD = 10 ** 9 + 7
        ans = 0
        for i in range(k):
            v = 0
            for j in range(32):
                if bits[j]:
                    v |= (1 << j)
                    bits[j] -= 1
            # print(v)
            ans += (v * v)
            ans %= MOD

        return ans % MOD


if __name__ == '__main__':
    pass
