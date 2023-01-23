#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = 1 if nums[i] % p == 0 else 0
            acc[i + 1] += acc[i]

        dup = set()
        ans = 0
        for i in range(n):
            for j in range(i, n):
                d = acc[j + 1] - acc[i]
                if d <= k:
                    v = tuple(nums[i:j + 1])
                    if v not in dup:
                        ans += 1
                        dup.add(v)
        return ans


if __name__ == '__main__':
    pass
