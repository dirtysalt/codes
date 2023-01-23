#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])
        ans = [['.'] * n for _ in range(m)]

        def flush(i, j, stone):
            if j < m:
                ans[j][i] = '*'
            while stone:
                j -= 1
                stone -= 1
                ans[j][i] = '#'

        for i in range(n):
            stone = 0
            for j in range(m):
                if box[i][j] == '#':
                    stone += 1
                elif box[i][j] == '*':
                    flush(n - 1 - i, j, stone)
                    stone = 0
            flush(n - 1 - i, m, stone)

        return ans


cases = [
    ([["#", ".", "#"]], [["."], ["#"], ["#"]]),
    ([["#", ".", "*", "."], ["#", "#", "*", "."]], [["#", "."], ["#", "#"], ["*", "*"], [".", "."]])

]

import aatest_helper

aatest_helper.run_test_cases(Solution().rotateTheBox, cases)

if __name__ == '__main__':
    pass
