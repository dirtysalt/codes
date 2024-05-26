#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        t = 0
        while (1 << t) < n:
            t += 1
        n = 1 << t

        class Node:
            def __init__(self):
                self.value = [[0] * 2 for _ in range(2)]

            def __repr__(self):
                return str(self.value)

        nodes: List[Node] = [Node() for _ in range(2 * n)]

        def update_once(p):
            c, l, r = nodes[p], nodes[2 * p], nodes[2 * p + 1]
            c.value[0][0] = max(l.value[0][0] + r.value[1][0], l.value[0][1] + r.value[0][0])
            c.value[0][1] = max(l.value[0][0] + r.value[1][1], l.value[0][1] + r.value[0][1])
            c.value[1][0] = max(l.value[1][0] + r.value[1][0], l.value[1][1] + r.value[0][0])
            c.value[1][1] = max(l.value[1][0] + r.value[1][1], l.value[1][1] + r.value[0][1])

        for i in range(len(nums)):
            p = i + n
            np = nodes[p]
            np.value[0][0] = 0
            np.value[0][1] = 0
            np.value[1][0] = 0
            np.value[1][1] = nums[i]

        for p in reversed(range(1, n)):
            update_once(p)

        def update(x, v):
            x = x + n
            nodes[x].value[1][1] = v
            p = x // 2
            while p:
                update_once(p)
                p = p // 2

        def query():
            np = nodes[1]
            return max(np.value[0][0], np.value[0][1], np.value[1][0], np.value[1][1])

        ans = 0
        for p, v in queries:
            update(p, v)
            # print(nodes)
            r = query()
            # print(r)
            ans += r

        MOD = 10 ** 9 + 7
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 5, 9], [[1, -2], [0, -3]], 21),
    ([0, -1], [[0, -5]], 0),
]

aatest_helper.run_test_cases(Solution().maximumSumSubsequence, cases)

if __name__ == '__main__':
    pass
