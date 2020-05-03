#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from queue import Queue

from leetcode import aatest_helper


class Solution:
    """
    @param matrix: a 0-1 matrix
    @return: return a matrix
    """

    def updateMatrix(self, matrix):
        # write your code here

        n = len(matrix)
        m = len(matrix[0])
        dist = [[-1] * m for _ in range(n)]
        queue = Queue()
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    dist[r][c] = 0
                    queue.put((r, c, 0))
        while not queue.empty():
            (x, y, d) = queue.get()
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x2 = x + dx
                y2 = y + dy
                if 0 <= x2 < n and 0 <= y2 < m and matrix[x2][y2] == 1:
                    if dist[x2][y2] == -1:
                        dist[x2][y2] = (d + 1)
                        queue.put((x2, y2, d + 1))
        return dist


cases = [
    ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]])
]

sol = Solution()

aatest_helper.run_test_cases(sol.updateMatrix, cases)
