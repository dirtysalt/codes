#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        def is_win(c):
            c3 = c * 3
            for i in range(3):
                if board[i] == c3:
                    return True

            for j in range(3):
                x = board[0][j] + board[1][j] + board[2][j]
                if x == c3:
                    return True

            x = board[0][0] + board[1][1] + board[2][2]
            if x == c3:
                return True
            x = board[0][2] + board[1][1] + board[2][0]
            if x == c3:
                return True

            return False

        x, o = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    x += 1
                elif board[i][j] == 'O':
                    o += 1

        x_win, o_win = is_win('X'), is_win('O')

        # if (x - o) >= 2 or (x < o):
        #     return False

        if x == o:
            # o is last step, x can not win
            if x_win:
                return False
            return True

        if x == (o + 1):
            # x is last step, o can not win
            if o_win:
                return False
            return True

        return False
