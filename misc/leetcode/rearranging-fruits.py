#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        from collections import Counter
        cnt = Counter(basket1)
        for x in basket2:
            cnt[x] -= 1

        A = []
        B = []
        for x in cnt.keys():
            d = cnt[x]
            if d == 0: continue
            if d % 2 != 0: return -1
            C = A
            if d < 0:
                C = B
                d = -d
            d = d // 2
            for _ in range(d):
                C.append(x)

        assert (len(A) == len(B))
        proxy = min(basket1 + basket2)
        A.sort()
        B.sort(reverse=True)
        ans = 0
        for a, b in zip(A, B):
            c1 = min(a, b)
            c2 = 2 * proxy
            ans += min(c1, c2)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([4, 2, 2, 2], [1, 4, 1, 2], 1),
    ([2, 3, 4, 1], [3, 2, 5, 1], -1),
    ([84, 80, 43, 8, 80, 88, 43, 14, 100, 88], [32, 32, 42, 68, 68, 100, 42, 84, 14, 8], 48),
]

aatest_helper.run_test_cases(Solution().minCost, cases)

if __name__ == '__main__':
    pass
