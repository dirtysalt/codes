#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mask = set()
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] - nums[i] == k:
                    mask.add((1 << i) | (1 << j))

        ans = 0
        for st in range(1, 1 << n):
            ok = True
            for m in mask:
                if st & m == m:
                    ok = False
                    break
            ans += ok
        return ans


if __name__ == '__main__':
    pass
