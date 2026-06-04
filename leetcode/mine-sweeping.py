#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param Mine_map: an array represents the map.
    @param Start: the start position.
    @return: return an array including all reachable positions.
    """

    def Mine_sweeping(self, Mine_map, Start):
        # write your code here
        n, m = len(Mine_map), len(Mine_map[0])
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            if Mine_map[i][j] == 1:
                for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m:
                        if (x, y) not in visited:
                            dfs(x, y)

        x, y = Start
        dfs(x, y)
        ans = list(list(x) for x in visited)
        return ans
