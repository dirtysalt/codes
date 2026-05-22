#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def sumGame(self, num: str) -> bool:
        acc, q = 0, 0

        n = len(num) // 2
        for i in range(n):
            if num[i] == '?':
                q += 1
            else:
                acc += int(num[i])
        for i in range(n, len(num)):
            if num[i] == '?':
                q -= 1
            else:
                acc -= int(num[i])
        if acc < 0:
            acc = -acc
            q = -q

        # acc > 0
        if acc > 0 and q > 0:
            return True
        q = -q

        # if Alice votes all 0, and Bob votes all 9
        # then sum is (q // 2) * 9
        # and if Alice votes all 9, and Bob votes all 0
        # then sum is (q+1) // 2 * 9
        if acc > (q // 2) * 9 or acc < (q + 1) // 2 * 9:
            return True
        return False


true, false, null = True, False, None
cases = [
    ["5023", false],
    ["25??", true],
    ["?3295???", false]
]

import aatest_helper

aatest_helper.run_test_cases(Solution().sumGame, cases)

if __name__ == '__main__':
    pass
