#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        back = [1] * n

        ans = 1
        for i in range(1, n):
            if prices[i] - prices[i - 1] == -1:
                back[i] = back[i - 1] + 1
            else:
                back[i] = 1
            ans += back[i]
        return ans


if __name__ == '__main__':
    pass
