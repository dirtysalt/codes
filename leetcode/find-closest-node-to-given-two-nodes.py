#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def computeDistance(node):
            dist = [-1] * n
            d = 0
            dist[node] = d
            while True:
                dist[node] = d
                node = edges[node]
                d += 1
                if node == -1 or dist[node] != -1:
                    break
            return dist

        A = computeDistance(node1)
        B = computeDistance(node2)
        cost = 1 << 30
        ans = -1
        for i in range(n):
            if A[i] != -1 and B[i] != -1:
                d = max(A[i], B[i])
                if d < cost:
                    cost = d
                    ans = i
        return ans


true, false, null = True, False, None
cases = [
    ([2, 2, 3, -1], 0, 1, 2),
    ([1, 2, -1], 0, 2, 2),
    ([4, 4, 4, 5, 1, 2, 2], 1, 1, 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().closestMeetingNode, cases)

if __name__ == '__main__':
    pass
