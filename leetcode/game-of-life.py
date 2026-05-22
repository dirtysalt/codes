#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])

        def nn_lives(i, j):
            cnt = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue
                    i2 = i + di
                    j2 = j + dj
                    if 0 <= i2 < n and 0 <= j2 < m and (board[i2][j2] & 0x1):
                        cnt += 1
            return cnt

        for i in range(n):
            for j in range(m):
                lives = nn_lives(i, j)
                if board[i][j] & 0x1:
                    if lives in (2, 3):
                        board[i][j] |= 0x2
                else:
                    if lives == 3:
                        board[i][j] |= 0x2

        for i in range(n):
            for j in range(m):
                board[i][j] = (board[i][j] & 0x2) >> 1


if __name__ == '__main__':
    sol = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    sol.gameOfLife(board)
    print(board)
