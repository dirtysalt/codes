#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs) + 1

        from collections import defaultdict
        adj = defaultdict(list)
        cnt = defaultdict(int)

        for x, y in adjacentPairs:
            cnt[x] += 1
            cnt[y] += 1
            adj[x].append(y)
            adj[y].append(x)

        # for k, v in adj.items():
        #     v.sort(key=lambda x: -cnt[x])

        ans = []
        for k, v in cnt.items():
            if v % 2 == 1:
                ans.append(k)
                break

        choose = set()
        choose.add(ans[-1])
        while len(ans) != n:
            x = ans[-1]
            for y in adj[x]:
                if y not in choose:
                    ans.append(y)
                    choose.add(y)
                    break

        return ans


cases = [
    ([[2, 1], [3, 4], [3, 2]], [1, 2, 3, 4, ]),
    ([[4, -2], [1, 4], [-3, 1]], [-2, 4, 1, -3]),
    ([[100000, -100000]], [100000, -100000])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().restoreArray, cases)
