#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        cnt = [0] * 32
        total = 0
        for x in nums:
            total = total | x
            for j in range(32):
                if x & (1 << j):
                    cnt[j] += 1

        ans = 0
        for x in nums:
            now = total
            for j in range(32):
                if x & (1 << j) and cnt[j] == 1:
                    now &= ~(1 << j)

            now = now | (x << k)
            ans = max(ans, now)
        return ans


if __name__ == '__main__':
    pass
