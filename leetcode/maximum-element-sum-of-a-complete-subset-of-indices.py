#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        base = []
        i = 1
        while i * i <= n:
            base.append(i * i)
            i += 1

        ans = max(nums)
        scale = 1
        while True:
            idx = [scale * x for x in base if scale * x <= n]
            if not idx: break
            # print(idx)
            c = sum((nums[x - 1] for x in idx))
            scale += 1
            ans = max(ans, c)
        return ans


if __name__ == '__main__':
    pass
