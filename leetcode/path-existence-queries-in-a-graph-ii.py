#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # compute upper values
        values = list(set(nums))
        values.sort()
        upper = {}
        j = 0
        for i in range(len(values)):
            while j < len(values) and values[j] - values[i] <= maxDiff:
                j += 1
            upper[values[i]] = values[j - 1]
        # print(upper)

        # compress upper values via logn
        max_depth = 1
        while (1 << max_depth) < len(values):
            max_depth += 1

        from collections import defaultdict
        dist = defaultdict(lambda: [0] * (max_depth + 1))
        for v in values:
            dist[v][0] = upper[v]
        for i in range(1, max_depth + 1):
            for v in values:
                dist[v][i] = dist[dist[v][i - 1]][i - 1]

        def query(u, v, i, j):
            if i == j: return 0
            if u == v: return 1
            if u > v: u, v = v, u
            d = max_depth
            if dist[u][d] < v:
                return -1

            res = 0
            while u < v:
                if dist[u][d] < v or d == 0:
                    res += (1 << d)
                    u = dist[u][d]
                else:
                    d = d - 1
            return res

        ans = []
        for u, v in queries:
            r = query(nums[u], nums[v], u, v)
            ans.append(r)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(n=5, nums=[1, 8, 3, 4, 2], maxDiff=3, queries=[[0, 3], [2, 4]], res=[1, 1]),
    aatest_helper.OrderedDict(n=5, nums=[5, 3, 1, 9, 10], maxDiff=2, queries=[[0, 1], [0, 2], [2, 3], [4, 3]],
                              res=[1, 2, -1, 1]),
    aatest_helper.OrderedDict(n=3, nums=[3, 6, 1], maxDiff=1, queries=[[0, 0], [0, 1], [1, 2]], res=[0, -1, -1]),
    (2, [15, 15], 18, [[0, 0], [1, 1], [1, 0]], [0, 0, 1]),
    (5, [18, 14, 8, 18, 0], 8, [[1, 1], [4, 0]], [0, 3]),
    (62, [14743, 79279, 21290, 74375, 12476, 91286, 63146, 29306, 38542, 84034, 2630, 37075, 83583, 37325, 84698, 84506,
          33657, 93096, 61736, 67237, 68089, 39695, 18244, 15325, 14653, 37185, 89898, 37008, 39918, 87821, 76303,
          70080, 74516, 57949, 18222, 10629, 13808, 61776, 72431, 54262, 85610, 34050, 27407, 62667, 25001, 66495,
          26081, 26550, 243, 8313, 42911, 17957, 49921, 37759, 20485, 62952, 75536, 83300, 55512, 78872, 44266, 87795],
     10744, [[45, 39], [51, 0], [24, 34], [10, 9], [2, 27], [57, 50], [57, 12], [54, 34], [36, 44], [18, 61]]
     , [2, 1, 1, 9, 2, 5, 1, 1, 2, 3])
]

aatest_helper.run_test_cases(Solution().pathExistenceQueries, cases)

if __name__ == '__main__':
    pass
