#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class State:
    def __init__(self, n, m):
        self.minr = n
        self.maxr = -1
        self.minc = m
        self.maxc = -1

    def see(self, r, c):
        if r < self.minr:
            self.minr = r
        if r > self.maxr:
            self.maxr = r
        if c < self.minc:
            self.minc = c
        if c > self.maxc:
            self.maxc = c

    def area(self):
        return (self.maxr - self.minr + 1) * (self.maxc - self.minc + 1)


class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """

    # def minArea(self, image, x, y):
    #     # write your code here
    #
    #     n = len(image)
    #     if n == 0: return 0
    #     m = len(image[0])
    #     if m == 0: return 0
    #
    #     state = State(n, m)
    #     nm = n * m
    #     visited = [0] * nm
    #
    #     def dfs(x, y):
    #         idx = x * m + y
    #         if visited[idx]:
    #             return
    #         visited[idx] = 1
    #         # print((x, y))
    #         state.see(x, y)
    #         if state.area() == nm:
    #             return
    #         for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    #             nx = x + dx
    #             ny = y + dy
    #             if 0 <= nx < n and 0 <= ny < m and image[nx][ny] == '1':
    #                 dfs(nx, ny)
    #
    #     dfs(x, y)
    #     return state.area()

    def minArea(self, image, x, y):
        n = len(image)
        if n == 0: return 0
        m = len(image[0])
        if m == 0: return 0

        minc, maxc = m, -1
        for r in range(n):
            for c in range(m):
                if image[r][c] == '1':
                    minc = min(c, minc)
                    break
            for c in range(m - 1, -1, -1):
                if image[r][c] == '1':
                    maxc = max(c, maxc)
                    break

        minr, maxr = n, -1
        for c in range(m):
            for r in range(n):
                if image[r][c] == '1':
                    minr = min(r, minr)
                    break
            for r in range(n - 1, -1, -1):
                if image[r][c] == '1':
                    maxr = max(r, maxr)
                    break

        res = (maxc - minc + 1) * (maxr - minr + 1)
        return res
