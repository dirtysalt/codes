#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        v = max(nums)
        ans = 0
        for _ in range(k):
            ans += v
            v += 1
        return ans


if __name__ == '__main__':
    pass
