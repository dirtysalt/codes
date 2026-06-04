#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        mm = [memory1, memory2, 0]

        def check():
            if mm[0] < mm[1]:
                mm[0], mm[1] = mm[1], mm[0]
                mm[2] = 1 - mm[2]
            elif mm[0] == mm[1]:  # 分配到内存1
                mm[2] = False

        t = 1
        while True:
            check()
            a = mm[0]
            if a < t:
                break
            diff = mm[0] - mm[1]
            s, e = 1, diff // t + 1
            while s <= e:
                m = (s + e) // 2
                # t + .. tm
                acc = (2 * t + m) * (m + 1) // 2
                if acc > diff:
                    e = m - 1
                else:
                    s = m + 1
            # step
            m = e
            acc = (2 * t + m) * (m + 1) // 2
            mm[0] -= acc
            t += (m + 1)

        # print(mm)
        if mm[2]:
            mm[0], mm[1] = mm[1], mm[0]
        ans = [t] + mm[:2]
        return ans


cases = [
    (2, 2, [3, 1, 0]),
    (8, 11, [6, 0, 4])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().memLeak, cases)

if __name__ == '__main__':
    pass
