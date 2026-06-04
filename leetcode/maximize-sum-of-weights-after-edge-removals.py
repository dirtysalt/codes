#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List, Tuple


class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dfs(x, p) -> Tuple[int, int]:
            # [a, b]
            # a: 如果必须需要cut edge(p-x)才可以满足的最大值
            # b: 如果不必须需要cut edge(p-x)就可以满足的最大值
            if len(adj[x]) == 1 and adj[x][0] == p:
                return 0, 0

            child = []
            for y, w in adj[x]:
                if y == p: continue
                a, b = dfs(y, x)
                child.append((a, b + w))

            # 不保留w, 可以得到a
            # 保留边w, 可以得到b+w
            child.sort(key=lambda x: x[1] - x[0], reverse=True)
            base = sum([x[0] for x in child])
            values = [base]
            for a, bw in child:
                base += (bw - a)
                values.append(max(values[-1], base))

            if len(values) >= (k + 1):
                return values[k], values[k - 1]
            else:
                return values[-1], values[-1]

        a, b = dfs(0, -1)
        return max(a, b)


true, false, null = True, False, None
import aatest_helper

cases = [
    # aatest_helper.OrderedDict(edges=[[0, 1, 4], [0, 2, 2], [2, 3, 12], [2, 4, 6]], k=2, res=22),
    # aatest_helper.OrderedDict(edges=[[0, 1, 5], [1, 2, 10], [0, 3, 15], [3, 4, 20], [3, 5, 5], [0, 6, 10]], k=3,
    #                           res=65),
    # ([[0, 1, 25], [0, 2, 10], [1, 3, 29]], 1, 39),
    ([[0, 1, 45]], 1, 45),
]

aatest_helper.run_test_cases(Solution().maximizeSumOfWeights, cases)

if __name__ == '__main__':
    pass
