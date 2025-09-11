#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        from collections import Counter
        import heapq
        points = Counter()

        n, m = len(grid), len(grid[0])
        dq = []
        dq.append((grid[0][0], 0, 0))
        visited = set()
        visited.add((0, 0))
        while dq:
            (v, x, y) = heapq.heappop(dq)
            points[v] += 1
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m:
                    if (x2, y2) not in visited:
                        visited.add((x2, y2))
                        value = max(grid[x2][y2], v)
                        heapq.heappush(dq, (value, x2, y2))

        events = [(k, 1, v) for k, v in points.items()]
        events += [(q, 0, i) for (i, q) in enumerate(queries)]
        events.sort()
        ans = [0] * len(queries)

        res = 0
        for k, ev, v in events:
            if ev == 0:
                ans[v] = res
            else:
                res += v
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 2, 3], [2, 5, 7], [3, 5, 1]], [5, 6, 2], [5, 8, 1]),
    ([[5, 2, 1], [1, 1, 2]], [3], [0]),
    ([[420766, 806051, 922751], [181527, 815280, 904568], [952102, 4037, 140319], [324081, 17907, 799523],
      [176688, 90257, 83661], [932477, 621193, 623068], [135839, 554701, 511427], [227575, 450848, 178065],
      [785644, 204668, 835141], [313774, 167359, 501496], [641317, 620688, 74989], [324499, 122376, 270369],
      [2121, 887154, 848859], [456704, 7763, 662087], [286827, 145349, 468865], [277137, 858176, 725551],
      [106131, 93684, 576512], [372563, 944355, 497187], [884187, 600892, 268120], [576578, 515031, 807686]],
     [352655, 586228, 169685, 541073, 584647, 413832, 576537, 616413],
     [0, 2, 0, 2, 2, 0, 2, 2]),
]

aatest_helper.run_test_cases(Solution().maxPoints, cases)

if __name__ == '__main__':
    pass
