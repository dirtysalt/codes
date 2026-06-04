#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        hp = []
        hp.append((0, 0, 0))
        inf = 1 << 30
        visit = [[inf] * m for _ in range(n)]

        import heapq
        while hp:
            (d, x, y) = heapq.heappop(hp)
            if (x, y) == (n - 1, m - 1):
                return d
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m:
                    gap = grid[x2][y2] - (d + 1)
                    if gap <= 0:
                        value = d + 1
                    else:
                        value0 = d + 1 + (gap + 1) // 2 * 2
                        # 也可以是下面这种形式
                        value1 = grid[x2][y2] + (grid[x2][y2] - x2 - y2) % 2
                        value = value0
                    if visit[x2][y2] > value:
                        visit[x2][y2] = value
                        heapq.heappush(hp, (value, x2, y2))
        return -1


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        # 将vis放在外面特别好，因为每次vis time是不同的
        vis = [[0] * m for _ in range(n)]

        def test(T):
            vis[-1][-1] = T
            from collections import deque
            dq = deque()
            dq.append((T, n - 1, m - 1))
            while dq:
                (t, x, y) = dq.popleft()
                if (x, y) == (0, 0):
                    return True
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < n and 0 <= y2 < m and vis[x2][y2] != T and grid[x2][y2] <= (t - 1):
                        vis[x2][y2] = T
                        dq.append((t - 1, x2, y2))
            return False

        left = max(grid[-1][-1], m + n - 2) - 1
        right = max(map(max, grid)) + m + n
        while (left + 1) < right:
            t = (left + right) // 2
            if test(t):
                right = t
            else:
                left = t + 1
        ans = right
        ans = ans + (ans - m - n) % 2
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]], 7),
    ([[0, 2, 4], [3, 2, 1], [1, 0, 4]], -1,),
]

cases += aatest_helper.read_cases_from_file('tmp.in', 2)

aatest_helper.run_test_cases(Solution().minimumTime, cases)

if __name__ == '__main__':
    pass
