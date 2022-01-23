#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        i = 0
        ans = 0
        while (i + 2) < len(cost):
            ans += cost[i] + cost[i + 1]
            i += 3

        ans += sum(cost[i:])
        return ans


if __name__ == '__main__':
    pass
