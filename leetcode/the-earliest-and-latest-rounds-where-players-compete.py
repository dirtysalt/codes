#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer -= 1
        secondPlayer -= 1

        def next(state):
            pairs = []
            for i in range(n):
                if (state >> i) & 0x1:
                    pairs.append(i)

            pn = len(pairs)
            sz = pn // 2

            match = False
            for i in range(sz):
                if pairs[i] == firstPlayer and pairs[pn - 1 - i] == secondPlayer:
                    match = True
                    return [], match

            res = []
            for st in range((1 << sz) - 1):
                base = 0
                if pn % 2 == 1:
                    base = (1 << pairs[sz])
                for i in range(sz):
                    if pairs[i] in (firstPlayer, secondPlayer):
                        base |= (1 << pairs[i])
                    elif pairs[pn - 1 - i] in (firstPlayer, secondPlayer):
                        base |= (1 << pairs[pn - 1 - i])
                    elif (st >> i) & 0x1:
                        base |= (1 << pairs[i])
                    else:
                        base |= (1 << pairs[pn - 1 - i])

                res.append(base)
            return res, match

        from functools import lru_cache
        @lru_cache(maxsize=None)
        def search(state):
            res, match = next(state)
            if match:
                return 1, 1

            a, b = 1 << 30, 0
            for r in res:
                mn, mx = search(r)
                a = min(mn, a)
                b = max(mx, b)

            return a + 1, b + 1

        a, b = search((1 << n) - 1)
        return [a, b]


true, false, null = True, False, None
cases = [
    (11, 2, 4, [3, 4]),
    (10, 1, 2, [4, 4]),
    (5, 1, 5, [1, 1])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().earliestAndLatest, cases)

if __name__ == '__main__':
    pass
