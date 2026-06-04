#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        # no reorder.
        ans = 0
        for x, y in zip(arr, brr):
            ans += abs(x - y)

        # reorder, and remove same elements first.
        c = k
        arr2 = sorted(arr)
        brr2 = sorted(brr)
        for x, y in zip(arr2, brr2):
            c += abs(x - y)

        ans = min(ans, c)
        return ans


if __name__ == '__main__':
    pass
