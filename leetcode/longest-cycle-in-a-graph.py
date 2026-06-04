#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        circle = [-1] * n

        def detectCircle(node):
            if circle[node] != -1: return circle[node]

            history = []
            index = {}
            sz = 0
            while True:
                index[node] = len(history)
                history.append(node)
                node = edges[node]
                # found old loop
                if circle[node] != -1:
                    sz = circle[node]
                    break

                # found new loop
                if node in index:
                    sz = len(history) - index[node]
                    break

                if node == -1:
                    break

            for x in history:
                circle[x] = sz
            return sz

        ans = 0
        for x in range(n):
            r = detectCircle(x)
            ans = max(ans, r)
        if ans == 0: return -1
        return ans


true, false, null = True, False, None
cases = [
    ([3, 3, 4, 2, 3], 3),
    ([2, -1, 3, 1], -1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestCycle, cases)

if __name__ == '__main__':
    pass
