#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(list)
        for i in range(len(nums)):
            x = nums[i]
            d[x].append(i)

        ans = (1 << 30)
        for k, xs in d.items():
            gap = len(nums) - xs[-1] + xs[0]
            for i in range(1, len(xs)):
                d = xs[i] - xs[i - 1]
                gap = max(d, gap)
            ans = min(ans, gap // 2)
        return ans


if __name__ == '__main__':
    pass
