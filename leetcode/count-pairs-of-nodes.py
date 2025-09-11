#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        freq = [0] * n
        for x, y in edges:
            freq[x - 1] += 1
            freq[y - 1] += 1
        conn = [[] for _ in range(n)]
        for x, y in edges:
            conn[x - 1].append(y - 1)
            conn[y - 1].append(x - 1)

        import itertools
        for i in range(n):
            xs = conn[i]
            xs.sort()
            cs = []
            for k, g in itertools.groupby(xs):
                cs.append((k, len(list(g))))
            conn[i] = cs

        cnt = []
        for i in range(n):
            cnt.append((i, freq[i]))
        cnt.sort(key=lambda x: x[1])

        ans = []
        for q in queries:
            res = 0
            for i in range(n):
                s, e = 0, n - 1
                while s <= e:
                    m = (s + e) // 2
                    if (cnt[m][1] + cnt[i][1]) <= q:
                        s = m + 1
                    else:
                        e = m - 1
                left = n - s
                x = cnt[i][0]

                if cnt[i][1] * 2 > q:
                    left -= 1

                sub = 0
                for y, c in conn[x]:
                    if (cnt[i][1] + freq[y] > q) and (cnt[i][1] + freq[y] - c) <= q:
                        sub += 1
                res += left - sub
            ans.append(res // 2)
        return ans


cases = [
    (4, [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], [2, 3], [6, 5]),
    (5, [[1, 5], [1, 5], [3, 4], [2, 5], [1, 3], [5, 1], [2, 3], [2, 5]], [1, 2, 3, 4, 5], [10, 10, 9, 8, 6]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countPairs, cases)
