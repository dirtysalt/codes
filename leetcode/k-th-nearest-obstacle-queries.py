#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        from sortedcontainers import SortedList
        sl = SortedList()
        ans = []
        for x, y in queries:
            sl.add(abs(x) + abs(y))
            if len(sl) < k:
                ans.append(-1)
            else:
                ans.append(sl[k - 1])
        return ans


if __name__ == '__main__':
    pass
