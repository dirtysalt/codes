#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if isinstance(board[0], str):
            board = [list(x) for x in board]

        row_st = []
        col_st = []
        sq_st = []
        for i in range(0, 9):
            row_st.append(set())
            col_st.append(set())
            sq_st.append(set())

        empty_pos = []

        for i in range(0, 9):
            for j in range(0, 9):
                c = board[i][j]
                if c == '.': empty_pos.append((i, j))

                if c != '.':
                    sq_idx = i / 3 * 3 + j / 3
                    sq_st[sq_idx].add(c)

                if c != '.':
                    row_st[i].add(c)

                c = board[j][i]
                if c != '.':
                    col_st[i].add(c)

        def try_it(pos_idx):
            if pos_idx == len(empty_pos):
                return True
            (x, y) = empty_pos[pos_idx]
            for i in range(1, 10):
                c = str(i)
                # print 'try (%d, %d) with %s' % (x, y, c)
                # print row_st[x], col_st[y], sq_st[x/3*3 + y /3]
                # if it works.
                if c not in row_st[x] and \
                                c not in col_st[y] and \
                                c not in sq_st[x / 3 * 3 + y / 3]:
                    # put on it.
                    row_st[x].add(c)
                    col_st[y].add(c)
                    sq_st[x / 3 * 3 + y / 3].add(c)
                    board[x][y] = c
                    if try_it(pos_idx + 1):
                        return True
                    # resume it.
                    row_st[x].remove(c)
                    col_st[y].remove(c)
                    sq_st[x / 3 * 3 + y / 3].remove(c)

        try_it(0)
        # for x in board:
        #    print x


if __name__ == '__main__':
    s = Solution()
    s.solveSudoku(
        ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6",
         "...2759.."])
