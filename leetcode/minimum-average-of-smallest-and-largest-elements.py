#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        tmp = [float(x) for x in nums]
        tmp.sort()
        from math import inf
        ans = inf
        for _ in range(len(tmp) // 2):
            v = (tmp[0] + tmp[-1]) * 0.5
            ans = min(ans, v)
            tmp = tmp[1:-1]
        return ans


if __name__ == '__main__':
    pass
