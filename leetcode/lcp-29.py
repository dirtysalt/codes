#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        a = min(xPos, num - 1 - xPos)
        b = min(yPos, num - 1 - yPos)
        start = min(a, b)
        # start position = 0 ... start - 1
        # size = num ...num - 2, num - 2*(start-1)
        # if size then # of elements is 4 * (size - 1)
        index = 4 * (num - start) * start
        # print(start, index)

        x0, x1 = start, num - 1 - start
        y0, y1 = start, num - 1 - start
        size = num - 2 * start

        if xPos == x0:
            index += yPos - y0 + 1

        elif yPos == y1:
            index += size - 1
            index += xPos - x0 + 1

        elif xPos == x1:
            index += 2 * (size - 1)
            index += (y1 - yPos + 1)

        else:
            index += 3 * (size - 1)
            index += (x1 - xPos + 1)

        return (index + 8) % 9 + 1

debug = False
if debug:
    sol = Solution()
    size = 5
    for x in range(size):
        for y in range(size):
            print(" %d " % sol.orchestraLayout(size, x, y), end='')
            print("")

cases = [
    (5, 2, 2, 7),
    (3, 0, 2, 3),
    (4, 1, 2, 5),
    (2511, 1504, 2235, 3),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().orchestraLayout, cases)



if __name__ == '__main__':
    pass
