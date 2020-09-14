#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        dp = [[-1] * 20 for _ in range(n)]
        for i in range(n):
            dp[i][0] = parent[i]

        for k in range(1, 20):
            for i in range(n):
                p = dp[i][k - 1]
                if p != -1:
                    dp[i][k] = dp[dp[i][k - 1]][k - 1]
        self.dp = dp

    def getKthAncestor(self, node: int, k: int) -> int:
        dp = self.dp
        while k > 0:
            d = 0
            while (1 << (d + 1)) <= k:
                d += 1
            node = dp[node][d]
            if node == -1:
                break
            k = k - (1 << d)
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

null = None
cases = [
    (["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"],
     [[5, [-1, 0, 0, 0, 3]], [1, 5], [3, 2], [0, 1], [3, 1], [3, 5]], [null, -1, -1, -1, 0, -1]),
]

import aatest_helper

aatest_helper.run_simulation_cases(TreeAncestor, cases)
