#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        pos = list(zip(range(n), positions, healths, directions))
        pos.sort(key=lambda x: x[1])
        # print(pos)
        st = []

        for idx, p, h, d in pos:
            while st:
                idx2, p2, h2, d2 = st[-1]

                if d == d2: break
                if d == 'R' and d2 == 'L': break

                idx2, p2, h2, d2 = st.pop()
                if h2 == h:
                    h = 0
                    break
                elif h2 < h:
                    h -= 1
                else:
                    h = 0
                    h2 -= 1
                    st.append((idx2, p2, h2, d2))
                    break
            if h > 0:
                st.append((idx, p, h, d))

        tmp = [0] * n
        for idx, p, h, d in st:
            tmp[idx] = h

        ans = [h for h in tmp if h > 0]
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR", [2, 17, 9, 15, 10]),
    ([3, 5, 2, 6], [10, 10, 15, 12], "RLRL", [14],),
    ([1, 2, 5, 6], [10, 10, 11, 11], "RLRL", []),
]

aatest_helper.run_test_cases(Solution().survivedRobotsHealths, cases)

if __name__ == '__main__':
    pass
