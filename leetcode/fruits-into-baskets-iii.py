#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        log = 1
        while (1 << log) < n:
            log += 1
        n = (1 << log)
        pq = [0] * (2 * n)

        def update(idx, v):
            p = idx + n
            pq[p] = v
            while p != 0:
                p = p // 2
                pq[p] = max(pq[2 * p], pq[2 * p + 1])

        def search(v):
            if pq[1] < v: return -1
            p = 1
            while p < n:
                p = 2 * p
                if pq[p] < v:
                    p += 1
            idx = p - n
            update(idx, 0)
            return idx

        for idx in range(len(baskets)):
            pq[idx + n] = baskets[idx]
        for p in reversed(range(1, n)):
            pq[p] = max(pq[2 * p], pq[2 * p + 1])

        # print(pq)

        ans = 0
        for f in fruits:
            idx = search(f)
            # print(f, idx)
            if idx == -1:
                ans += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([4, 2, 5], [3, 5, 4], 1),
    ([3, 6, 1], [6, 4, 7], 0),
]

aatest_helper.run_test_cases(Solution().numOfUnplacedFruits, cases)

if __name__ == '__main__':
    pass
