#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class TreeNode:
    def __init__(self, index, value, depth):
        self.index = index
        self.value = value
        self.total = value
        self.depth = depth
        self.parent = set()


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)

        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        tt = 0
        for x in nums:
            tt ^= x

        trees = [None] * n

        def build(x, d, pt):
            t = TreeNode(x, nums[x], d)
            pt.append(x)
            t.parent = set(pt)
            trees[x] = t
            for y in adj[x]:
                if trees[y]: continue
                t2 = build(y, d + 1, pt)
                t.total ^= t2.total
            pt.pop()

            return t

        build(0, 0, [])
        for xx in edges:
            xx.sort(key=lambda x: trees[x].depth)

        inf = 1 << 30
        ans = inf
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                a, b = edges[i]
                c, d = edges[j]
                ta, tb, tc, td = [trees[x] for x in [a, b, c, d]]
                # tb -> ta
                # td -> tc
                if d in ta.parent:
                    # tb -> ta -> ...  td -> tc
                    x = tb.total
                    y = td.total ^ x
                elif b in tc.parent:
                    # td -> tc -> tb -> ta
                    x = td.total
                    y = tb.total ^ x
                else:
                    x = tb.total
                    y = td.total
                z = tt ^ x ^ y
                minv = min(x, y, z)
                maxv = max(x, y, z)
                res = maxv - minv
                ans = min(res, ans)
        return ans


true, false, null = True, False, None
cases = [
    ([1, 5, 5, 4, 11], [[0, 1], [1, 2], [1, 3], [3, 4]], 9),
    ([5, 5, 2, 4, 4, 2], [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]], 0),
    ([29, 29, 23, 32, 17], [[3, 1], [2, 3], [4, 1], [0, 4]], 15),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumScore, cases)

if __name__ == '__main__':
    pass
