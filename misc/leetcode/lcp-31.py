#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

# 这个解法是枚举所有可能的状态，但是这个状态空间集合非常的大
class SolutionA:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        t = maze[0]
        n, m = len(t), len(t[0])

        from collections import deque
        dq = deque()
        dp = set()

        st = (0, 0, 0, 1,-1, -1)
        dp.add(st)
        dq.append(st)

        while dq:
            (t, x, y, temp, px, py) = dq.pop()
            if (x, y) == (n-1, m-1): return True
            if (t + 1) >= len(maze): continue
            mz = maze[t+1]

            for dx, dy in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                x2, y2 = x + dx, y + dy
                if not (0 <= x2 < n and 0 <= y2 < m): continue

                if mz[x2][y2] == '.' or (x2, y2) == (px, py):
                    st = (t+1, x2, y2, temp, px, py)
                    if st not in dp:
                        dp.add(st)
                        dq.append(st)
                else:
                    if temp:
                        st = (t + 1, x2, y2, temp-1,px,py)
                        if st not in dp:
                            dp.add(st)
                            dq.append(st)
                    if px == -1:
                        st = (t + 1, x2, y2, temp, x2, y2)
                        if st not in dp:
                            dp.add(st)
                            dq.append(st)


        # print(len(dp), len(maze))
        return False

# 这个解法几乎也是枚举所有的状态，只不过将可以永久删除的点单独放循环里面枚举
class SolutionB:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        n, m = len(maze[0]), len(maze[0][0])

        def test(px, py):
            from collections import deque

            dp = {}
            dq = deque()

            st = (0, 0, 0)
            dp[st] = 0
            dq.append(st)

            def update(st, v):
                if st not in dp:
                    dp[st] = v
                    return True
                dp[st] = min(dp[st], v)
                return False

            while dq:
                st = (t, x, y) = dq.popleft()
                if (x, y) == (n-1, m-1): return True
                if (t + 1) >= len(maze): continue
                mz = maze[t+1]
                old = dp[st]

                for dx, dy in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                    x2, y2 = x + dx, y + dy
                    if not (0 <= x2 < n and 0 <= y2 < m): continue
                    st2 = (t + 1, x2, y2)
                    if mz[x2][y2] == '.' or (x2, y2) == (px, py):
                        if update(st2, old):
                            dq.append(st2)
                    elif old == 0:
                        if update(st2, 1):
                            dq.append(st2)
            return False

        for px in range(n):
            for py in range(m):
                if test(px, py):
                    return True
        return False

# 尝试做些改进，其中test是判断从哪个位置开始出现block, 那么将这个位置记录下来，下个阶段从这个地方开始遍历，并且认为这个位置是可以被免除的
# 感觉还有某些计算是可以减少的，但是暂时想不出来
class SolutionC:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        n, m = len(maze[0]), len(maze[0][0])

        def test(start):
            from collections import deque
            dp = set()
            dq = deque()

            st = (0, 0, 0)
            dp.add(st)
            dq.append(st)

            while dq:
                st = (t, x, y) = dq.popleft()
                if (x, y) == (n-1, m-1): return True
                if (t + 1) >= len(maze): continue
                mz = maze[t+1]

                for dx, dy in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                    x2, y2 = x + dx, y + dy
                    if not (0 <= x2 < n and 0 <= y2 < m): continue
                    st2 = (t + 1, x2, y2)
                    if mz[x2][y2] == '.':
                        if st2 not in dp:
                            dp.add(st2)
                            dq.append(st2)
                    else:
                        start[(x2, y2)].append(st2)
            return False

        def test2(st, px, py):
            from collections import deque
            dp = set()
            dq = deque()
            dq.append(st)

            while dq:
                (t, x, y, temp) = dq.popleft()
                if (x, y) == (n-1, m-1): return True
                if (t + 1) >= len(maze): continue
                mz = maze[t+1]
                for dx, dy in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                    x2, y2 = x + dx, y + dy
                    if not (0 <= x2 < n and 0 <= y2 < m): continue
                    st2 = (t + 1, x2, y2, temp)
                    if mz[x2][y2] == '.' or (x2, y2) == (px, py):
                        if st2 not in dp:
                            dp.add(st2)
                            dq.append(st2)
                    elif temp:
                        st2 = (t + 1, x2, y2, temp - 1)
                        if st2 not in dp:
                            dp.add(st2)
                            dq.append(st2)

            return False

        from collections import defaultdict
        start = defaultdict(list)
        if test(start):
            return True

        for (px, py), stlist in start.items():
            for (t, x, y) in stlist:
                st = (t, x, y, 1)
                if test2(st, px, py):
                    return True
        return False

# 看了这题的动态规划解法，其中有个观察就是，如果某次使用了永久卷轴的话，那么可以在这里多次等待，效果其实类似可以跳到之后的+d时刻，而不是仅仅+1时刻。
import numpy as np
class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        T, N, M = len(maze), len(maze[0]), len(maze[0][0])
        dp = np.zeros((T, N, M, 4), dtype=np.int8)
        maxhis = np.zeros((T, N, M, 4), dtype=np.int8)

        dp[0][0][0][0] = 1

        for t in range(T-1):
            # update forward
            for i in range(N):
                for j in range(M):
                    for st in range(4):
                        value = dp[t][i][j][st]
                        if (st & 0x2):
                            value |= maxhis[t][i][j][st]
                        if value == 0: continue

                        for dx, dy in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                            x, y = i + dx ,j + dy
                            if not (0 <= x < N and 0 <= y < M): continue
                            if maze[t+1][x][y] == '.':
                                dp[t+1][x][y][st] = 1
                                continue

                            # 没有使用临时卷轴
                            if (st & 0x1) == 0:
                                dp[t+1][x][y][st | 0x1] = 1

                            # 没有使用永久卷轴
                            if (st & 0x2) == 0:
                                # 那么可以跳转到任意位置下面
                                # dp[t+x][x][y][u | 0x3]
                                # for t2 in range(t+1, T):
                                #     dp[t2][x][y][st | 0x2] = 1
                                maxhis[t+1][x][y][st | 0x2] = 1
            # update maxhis
            for x in range(N):
                for y in range(M):
                    for st in range(4):
                        if (st & 0x2):
                            maxhis[t+1][x][y][st] |= maxhis[t][x][y][st]

        return bool(max(dp[T-1][N-1][M-1]) == 1)


cases = [
    ([[".#.","#.."],["...",".#."],[".##",".#."],["..#",".#."]], True),
    ([[".#.","..."],["...","..."]], False),
    ([["...","...","..."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]], False),
    ([["...",".##","##.","#.#",".##","...",".#.","##.","##."],[".##","###","##.",".##",".##","##.",".#.","###","##."],[".##","###","###",".##","##.","##.","#.#","###",".#."],[".##","#.#",".##","#.#","###","#.#","###","...",".#."],["..#","###","#..",".##",".##","..#",".#.","###",".#."],["..#",".#.","..#",".##","###","#.#","#..","###","##."],[".##","..#",".##",".#.","##.","###","##.","###","##."],[".##","..#","#.#",".##","###",".##","##.",".##","#.."],["...","##.","#.#","..#","##.","..#",".##","#.#","##."],[".##","###","###","#.#",".##",".##","###","###","#.."],["..#","###","..#","#..",".#.","###","#.#","###",".#."],["..#","###","##.","##.",".#.","#..","###","##.",".#."],[".##","#.#",".#.",".##",".#.","###",".#.","###","##."],[".#.","#.#",".##","#..","#.#","##.","###","###","##."],["..#","###","###","###","##.",".#.","##.","###","##."],["..#","#..",".#.","##.","###","...",".##","#.#",".#."],[".##","###",".##",".##","###","#..","###","...",".#."],[".##",".##","##.","#..","###","..#","...","###","##."],[".##","#..","###","###","##.","#..",".##","..#","##."],["...",".#.","###","###","###","###","##.","#.#",".#."],[".##",".#.","#..","#.#","###","##.",".#.","###",".#."],["..#","###","###","###","#.#","##.","##.","#.#","#.."],["...","###","###","##.","#.#",".#.","#.#","#..",".#."],[".##","..#","##.",".##","###","#..","#.#","#.#","##."],["..#","###","###","##.",".##",".##","#.#","#..",".#."],["..#","..#","#..","...",".##","##.","#.#","##.","##."],[".#.","##.","#.#","##.","#.#","##.","###",".#.","##."],[".#.","###","..#","###",".##","..#",".#.","###","##."],[".#.","###","###","##.","###",".##","##.","##.",".#."],[".#.",".##","###",".#.",".#.",".#.","###","###","..."],[".##","#.#",".##","###","###",".##",".##",".##","##."],["..#","##.",".#.",".##","###","###","###",".##","##."],[".#.",".##","##.","#..","###",".#.",".#.","#.#","##."],[".#.","###","...","###","##.",".#.","#.#",".##","##."],["..#","#..","#.#",".##","###","##.",".#.","##.","##."],["..#","##.","###","###","#..","##.","##.",".##","##."],["..#","###",".##","..#",".#.",".##",".##","###",".#."],["..#",".#.",".##",".#.",".#.",".##","#.#","##.","##."],["..#","###","#..","...","#..",".##","..#",".##","..."],[".##","###","#..","###","#.#","##.","#..","###","##."]], True),
    ([[".##..####",".#######."],["..######.","########."],[".#####.##",".#######."],[".#..###.#","########."],[".########","########."],[".######.#","####.###."],[".#####.##","#####.#.."],[".##.####.","##.#####."],[".########","#####.##."],[".#.######","#.##.###."],[".########","###.#.#.."],[".########","########."],[".####.##.","##.##...."],[".#######.","###.#.##."],[".####.###","###.####."],[".######.#","##.####.."],[".##.#####","##.###.#."],[".####.###","##.#####."],[".##.##..#",".#.#####."],[".###.####","##.#..##."],[".####.#.#","##.#####."],[".####.###","####.###."],[".########","#######.."],[".#####.##","#.######."],[".########","###..#.#."],[".####.#.#","###..##.."],[".######.#","########."],[".########","##.#####."],[".########","..######."],[".#####..#","#######.."],[".#.######",".#######."],[".###.#.#.",".##..#.#."],[".#.##.###","####.##.."]], True),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().escapeMaze, cases)

if __name__ == '__main__':
    pass
