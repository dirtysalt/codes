#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(x, p):
            ST = 0
            C1 = []
            C2 = []
            for y in adj[x]:
                if y == p: continue
                t, c1, c2 = dfs(y, x)
                ST = max(ST, t)
                C1.append(c1)
                C2.append(c2)

            t = ST

            if len(C1) == 0:
                # 如果是叶子节点的话
                return 0, price[x], 0
            elif len(C1) == 1:
                # 如果只有1条路径的话，那么可以选择"裁剪叶子节点" + 当前节点作为最优路径
                t = max(t, C2[0] + price[x])
            else:
                # TODO(yanz): efficient more.
                # 如果有超过2条路，那么选择一条"裁剪叶子节点"和一点"没有裁剪叶子节点"的路径
                # 所以C2其实只需要保存最近的2个节点
                for i in range(len(C1)):
                    for j in range(len(C2)):
                        if i == j: continue
                        t = max(t, C1[i] + C2[j] + price[x])

            c1 = max(C1) + price[x]
            c2 = max(C2) + price[x]
            return t, c1, c2

        t, c1, c2 = dfs(0, -1)
        # c1是全路径的最优节点，其实我们可以将root作为叶子节点
        ans = max(t, c1 - price[0])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (6, [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5]], [9, 8, 7, 6, 10, 5], 24),
    (3, [[0, 1], [1, 2]], [1, 1, 1], 2),
    (2, [[0, 1]], [3, 8], 8),
    (4, [[0, 3], [2, 1], [1, 3]], [6, 8, 2, 14], 28),
]

aatest_helper.run_test_cases(Solution().maxOutput, cases)

if __name__ == '__main__':
    pass
