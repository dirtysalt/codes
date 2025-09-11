#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


# class Solution:
#     def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
#         ans = []
#
#         for n, v in queries:
#             res = 0
#             while n != -1:
#                 res = max(res, n ^ v)
#                 n = parents[n]
#             ans.append(res)
#
#         return ans

# class Tree:
#     def __init__(self, lgn):
#         self.size = 1 << (lgn + 1)
#         self.lgn = lgn
#         self.data = [set() for _ in range(self.size)]
#
#     def insert(self, x, opts):
#         p = 1
#         for i in reversed(range(self.lgn)):
#             p = 2 * p
#             if (x >> i) & 0x1:
#                 p += 1
#             self.data[p].update(opts)
#
#     def find(self, val, node):
#         p = 1
#         ans = 0
#         for i in reversed(range(self.lgn)):
#             exp = 1 - (val >> i) & 0x1
#             p = 2 * p
#             ans = ans * 2
#             if exp == 1:
#                 if node in self.data[p + 1]:
#                     ans += 1
#                     p += 1
#                 else:
#                     pass
#             else:
#                 if node in self.data[p]:
#                     ans += 1
#                 else:
#                     p += 1
#         return ans
#
#
# class Solution:
#     def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
#         mxn = len(parents)
#         for v, p in queries:
#             mxn = max(mxn, p)
#         lgn = 1
#         while (1 << lgn) <= mxn:
#             lgn += 1
#
#         tree = Tree(lgn)
#         child = [set() for _ in range(len(parents))]
#
#         for x in range(len(parents)):
#             p = x
#             while p != -1:
#                 child[p].add(x)
#                 p = parents[p]
#                 if p == -1:
#                     break
#
#         for x in range(len(parents)):
#             # print(x, child[x])
#             tree.insert(x, child[x])
#
#         ans = []
#         for node, val in queries:
#             x = tree.find(val, node)
#             ans.append(x)
#         return ans

class Tree:
    def __init__(self):
        self.child = [None, None]
        self.cnt = 0


def insert(root, x, bits):
    for i in reversed(range(bits)):
        side = (x >> i) & 0x1
        if root.child[side] is None:
            t = Tree()
            root.child[side] = t
        root = root.child[side]
        root.cnt += 1


def query(root, x, bits):
    ans = 0
    for i in reversed(range(bits)):
        side = (x >> i) & 0x1
        ans = ans * 2
        if root.child[1 - side] is not None and root.child[1 - side].cnt != 0:
            ans += 1
            root = root.child[1 - side]
        else:
            root = root.child[side]
    return ans


def remove(root, x, bits):
    for i in reversed(range(bits)):
        side = (x >> i) & 0x1
        root = root.child[side]
        root.cnt -= 1


class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)
        child = [[] for _ in range(n)]
        root = None
        for i in range(n):
            p = parents[i]
            child[p].append(i)
            if p == -1:
                root = i

        maxValue = n
        flatQueries = [[] for _ in range(n)]
        for i in range(len(queries)):
            node, v = queries[i]
            flatQueries[node].append((i, v))
            maxValue = max(maxValue, v)

        bits = 1
        while (1 << bits) <= maxValue:
            bits += 1

        vis = [0] * n
        tree = Tree()
        ans = [0] * len(queries)

        def dfs(x):
            vis[x] = 1

            insert(tree, x, bits)
            for idx, v in flatQueries[x]:
                res = query(tree, v, bits)
                ans[idx] = res

            for y in child[x]:
                if vis[y]: continue
                dfs(y)

            remove(tree, x, bits)

        dfs(root)
        return ans


true, false, null = True, False, None
cases = [
    ([-1, 0, 1, 1], [[0, 2], [3, 2], [2, 5]], [2, 3, 7]),
    ([3, 7, -1, 2, 0, 7, 0, 2], [[4, 6], [1, 15], [0, 5]], [6, 14, 7]),
    ([-1, 0, 0, 0, 3], [[4, 6], [0, 0], [0, 3], [1, 8], [4, 0]], [6, 0, 3, 9, 4]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxGeneticDifference, cases)

if __name__ == '__main__':
    pass
