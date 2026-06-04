#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        N = 20
        now = [0] * N
        for x in nums:
            for i in range(N):
                now[i] = now[i] ^ ((x >> i) & 0x1)

        ans = 0
        for i in range(N):
            ans += (now[i] != ((k >> i) & 0x1))
        return ans


if __name__ == '__main__':
    pass
