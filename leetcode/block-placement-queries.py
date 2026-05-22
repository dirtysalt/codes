#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        maxsz = max([q[1] for q in queries])
        n = maxsz + 2
        t = 0
        while (1 << t) < n:
            t += 1
        n = 1 << t

        trees = [0] * (2 * n)

        def update_once(p):
            l, r = 2 * p, 2 * p + 1
            trees[p] = max(trees[l], trees[r])

        def update(p, v):
            p += n
            trees[p] = v
            p = p // 2
            while p:
                update_once(p)
                p = p // 2

        def query(p, s, e, end):
            if e <= end: return trees[p]
            m = (s + e) // 2
            if end <= m:
                return query(2 * p, s, m, end)
            a = trees[2 * p]
            b = query(2 * p + 1, m + 1, e, end)
            return max(a, b)

        ans = []
        from sortedcontainers import SortedList
        sl = SortedList([0, maxsz + 1])
        for q in queries:
            x = q[1]
            idx = sl.bisect_left(x)
            pre = sl[idx - 1]
            if q[0] == 1:
                nxt = sl[idx]
                update(x, x - pre)
                update(nxt, nxt - x)
                sl.add(x)
            else:
                r = query(1, 0, n - 1, pre)
                r = max(r, x - pre)
                # print(r)
                ans.append(r >= q[2])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]], [false, true, true]),
    ([[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]], [true, true, false]),
]

aatest_helper.run_test_cases(Solution().getResults, cases)

if __name__ == '__main__':
    pass
