#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minRemainingSpace(self, N: List[int], V: int) -> int:
        dp = set([0])

        for x in N:
            dp2 = dp.copy()
            for y in dp:
                if (x + y) <= V:
                    dp2.add(x + y)
            dp = dp2

        ans = V - max(dp)
        return ans


if __name__ == '__main__':
    pass
