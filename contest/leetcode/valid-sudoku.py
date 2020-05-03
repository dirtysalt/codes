#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def isValidSudoku(self, board):
        # for x in board:
        #     print x
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # by row and column
        for i in range(0, 9):
            d = set()
            d2 = set()
            for j in range(0, 9):
                c = board[i][j]
                if c != '.':
                    if c in d: return False
                    d.add(c)

                c = board[j][i]
                if c != '.':
                    if c in d2: return False
                    d2.add(c)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                d = set()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        c = board[x][y]
                        if c == '.': continue
                        if c in d: return False
                        d.add(c)

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku(
        ["..4...63.", ".........", "5......9.", "...56....", "4.3.....1", "...7.....", "...5.....", ".........",
         "........."]))
