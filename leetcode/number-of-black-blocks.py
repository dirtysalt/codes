#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        seen = set()
        ans = [0] * 5
        C = set()
        for x, y in coordinates:
            C.add((x, y))

        for x, y in coordinates:
            corners = ((x - 1, y - 1), (x - 1, y), (x, y - 1), (x, y))
            for cx, cy in corners:
                if not (0 <= cx < (m - 1) and 0 <= cy < (n - 1)): continue
                if (cx, cy) in seen: continue
                seen.add((cx, cy))
                v = 0
                for dx, dy in ((0, 0), (0, 1), (1, 0), (1, 1)):
                    cx2, cy2 = cx + dx, cy + dy
                    if 0 <= cx2 < m and 0 <= cy2 < n and (cx2, cy2) in C:
                        v += 1
                # print(cx, cy, v)
                ans[v] += 1

        ans[0] = (m - 1) * (n - 1) - sum(ans)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (3, 3, [[0, 0]], [3, 1, 0, 0, 0]),
    (3, 3, [[0, 0], [1, 1], [0, 2]], [0, 2, 2, 0, 0]),
]

aatest_helper.run_test_cases(Solution().countBlackBlocks, cases)

if __name__ == '__main__':
    pass
