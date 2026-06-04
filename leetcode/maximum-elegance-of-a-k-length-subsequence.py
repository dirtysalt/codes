#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x: -x[0])
        ans = 0
        total = 0

        vis = set()
        dup = []
        for i in range(len(items)):
            profit, category = items[i]
            if i < k:
                total += profit
                if category not in vis:
                    vis.add(category)
                else:
                    dup.append(profit)
            elif dup and category not in vis:
                vis.add(category)
                total += profit - dup.pop()

            ans = max(ans, total + len(vis) ** 2)
        return ans


if __name__ == '__main__':
    pass
