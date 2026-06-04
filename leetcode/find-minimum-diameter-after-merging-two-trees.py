#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def find(edges):

            n = len(edges) + 1
            if n == 1:
                return 0, 0

            adj = [[] for _ in range(n)]
            for x, y in edges:
                adj[x].append(y)
                adj[y].append(x)

            depth = [[] for _ in range(n)]

            def search(x, p):
                # return tree_depth, max_dist
                if len(adj[x]) == 1 and adj[x][0] == p:
                    return 0, 0

                res = 0
                for y in adj[x]:
                    if y == p: continue
                    td, md = search(y, x)
                    depth[x].append((y, td + 1))
                    res = max(res, md)
                depth[x].sort(key=lambda x: x[1])
                d = depth[x]
                if len(d) >= 2:
                    res = max(res, d[-1][1] + d[-2][1])
                res = max(res, d[-1][1])
                return d[-1][1], res

            _, max_dist = search(0, -1)

            print(depth)

            radius = [0] * n

            def dfs(x, p, d0):
                if len(adj[x]) == 1 and adj[x][0] == p:
                    radius[x] = d0
                    return d0

                d = depth[x]
                ans = max(d[-1][1], d0)
                radius[x] = ans

                for y in adj[x]:
                    if y == p: continue
                    d1 = d[-1][1]
                    if y == d[-1][0]:
                        if len(d) >= 2:
                            d1 = d[-2][1]
                        else:
                            d1 = 0
                    # 从x遍历到y, y为分界点, Y的到其他点的最大距离有
                    # 1. y 通过 x 之前的节点到达其他节点最大距离是 d0 + 1
                    # 2. y 通过 x 到达其他节点最大距离是 d1 + 1
                    r = dfs(y, x, max(d0 + 1, d1 + 1))
                    ans = min(r, ans)

                return ans

            rad = dfs(0, -1, 0)
            print(radius)
            return rad, max_dist

        r0, d0 = find(edges1)
        r1, d1 = find(edges2)
        print(r0, d0, r1, d1)
        return max(r0 + r1 + 1, d0, d1)


true, false, null = True, False, None
import aatest_helper

cases = [
    # aatest_helper.OrderedDict(edges1=[[0, 1], [0, 2], [0, 3]], edges2=[[0, 1]], res=3),
    # aatest_helper.OrderedDict(edges1=[[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
    #                           edges2=[[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]], res=5),
    # ([], [], 1),
    ([[1, 0], [2, 3], [1, 4], [2, 1], [2, 5]], [[4, 5], [2, 6], [3, 2], [4, 7], [3, 4], [0, 3], [1, 0], [1, 8]], 6)
]

aatest_helper.run_test_cases(Solution().minimumDiameterAfterMerge, cases)

if __name__ == '__main__':
    pass
