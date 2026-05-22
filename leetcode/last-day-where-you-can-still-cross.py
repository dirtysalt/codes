#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def bfs(days):
            import heapq
            hp = []
            visited = set()
            blocked_cells = cells[:days]
            blocked = set([(x - 1, y - 1) for (x, y) in blocked_cells])

            # print(days)
            # use row - <i> as first element
            # so bfs is actually A*

            # print(days, blocked)
            for j in range(col):
                if (0, j) in blocked:
                    continue
                heapq.heappush(hp, (row, 0, j))
                visited.add((0, j))

            while hp:
                _, r, c = heapq.heappop(hp)
                if r == (row - 1): return True
                for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    x, y = r + dx, c + dy
                    if 0 <= x < row and 0 <= y < col:
                        if (x, y) in visited or (x, y) in blocked:
                            continue
                        else:
                            heapq.heappush(hp, (row - x, x, y))
                            visited.add((x, y))
            return False

        s, e = 1, len(cells)
        while s <= e:
            m = (s + e) // 2
            if bfs(m):
                s = m + 1
            else:
                e = m - 1
        ans = e
        return ans


true, false, null = True, False, None
cases = [
    (2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]], 2),
    (2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]], 1),
    (3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]], 3),
    (6, 2, [[4, 2], [6, 2], [2, 1], [4, 1], [6, 1], [3, 1], [2, 2], [3, 2], [1, 1], [5, 1], [5, 2], [1, 2]], 3),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().latestDayToCross, cases)

if __name__ == '__main__':
    pass
