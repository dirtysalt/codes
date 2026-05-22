#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        a, b, c = [], [], 0

        for x in nums:
            if x > 0:
                a.append(x)
            elif x < 0:
                b.append(x)
            else:
                c += 1

        if len(a) == 0 and len(b) <= 1:
            if len(b) == 0: return 0
            if c == 0:
                return b[0]
            else:
                return 0

        ans = 1
        for x in a:
            ans = ans * x
        b.sort()
        for i in range(0, len(b) - 1, 2):
            ans = ans * b[i] * b[i + 1]
        return ans


if __name__ == '__main__':
    pass
