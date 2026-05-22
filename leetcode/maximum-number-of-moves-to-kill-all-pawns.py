#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        positions = [tuple(x) for x in positions]
        positions.append((kx, ky))
        n = len(positions)
        INV = {positions[i]: i for i in range(n)}
        D = [[-1] * n for _ in range(n)]

        def populate_distance(x, y):
            oi = INV[(x, y)]
            q = [(x, y)]
            d = [[-1] * 50 for _ in range(50)]
            step = 1
            while q:
                tmp = q
                q = []
                for x, y in tmp:
                    for dx, dy in ((1, 2), (-1, 2), (1, -2), (-1, -2),
                                   (2, 1), (-2, 1), (2, -1), (-2, -1)):
                        x2, y2 = x + dx, y + dy
                        if 0 <= x2 < 50 and 0 <= y2 < 50 and d[x2][y2] == -1:
                            d[x2][y2] = step
                            q.append((x2, y2))
                step += 1

            for x in range(50):
                for y in range(50):
                    oj = INV.get((x, y))
                    if oj is None: continue
                    D[oi][oj] = d[x][y]
                    D[oj][oi] = d[x][y]

        for x, y in positions:
            populate_distance(x, y)

        import functools
        @functools.cache
        def dfs(st, idx):
            if st == 0:
                return 0
            values = []
            step = n - (st.bit_count())
            op = max if step % 2 else min
            res = 0 if step % 2 else (1 << 30)
            for i in range(n - 1):
                if st & (1 << i):
                    r = dfs(st & ~(1 << i), i) + D[idx][i]
                    res = op(res, r)
            return res

        st = (1 << (n - 1)) - 1
        ans = dfs(st, n - 1)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (1, 1, [[0, 0]], 4),
    (0, 2, [[1, 1], [2, 2], [3, 3]], 8),
    (0, 0, [[1, 2], [2, 4]], 3),
    (8, 4, [[5, 33], [32, 31], [3, 39], [22, 10], [35, 28], [23, 36], [34, 12], [26, 32], [34, 32], [36, 15], [33, 27],
            [28, 35]], 109),
    (21, 20,
     [[36, 34], [40, 42], [2, 46], [30, 29], [38, 27], [8, 1], [44, 23], [6, 25], [17, 12], [25, 1], [6, 45], [44, 28],
      [15, 7], [24, 19], [40, 23]], 175),
]

aatest_helper.run_test_cases(Solution().maxMoves, cases)

if __name__ == '__main__':
    pass
