#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        a, b = [], []
        for x in nums:
            if x > 0:
                a.append(x)
            else:
                b.append(x)
        A = sum(a)
        ans = len(a)
        b.sort(reverse=True)
        for x in b:
            if (A + x) <= 0:
                break
            A += x
            ans += 1
        return ans


if __name__ == '__main__':
    pass
