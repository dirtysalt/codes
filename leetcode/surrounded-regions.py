#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return

        bs = set()
        n = len(board)
        m = len(board[0])
        for i in (0, n - 1):
            for j in range(m):
                if board[i][j] == 'O':
                    bs.add((i, j))
        for j in (0, m - 1):
            for i in range(n):
                if board[i][j] == 'O':
                    bs.add((i, j))

        seen = set()

        def visit(r, c):
            st = []
            st.append((r, c, 0))
            seen.add((r, c))

            while st:
                (i, j, d) = st.pop()
                ni, nj = i, j
                d += 1
                if d == 1:
                    ni += 1
                elif d == 2:
                    nj += 1
                elif d == 3:
                    ni -= 1
                elif d == 4:
                    nj -= 1
                else:
                    continue
                st.append((i, j, d))

                if ni < 0 or ni >= n or \
                                nj < 0 or nj >= m or \
                                board[ni][nj] == 'X' or \
                                (ni, nj) in seen:
                    continue

                st.append((ni, nj, 0))
                seen.add((ni, nj))
                bs.add((ni, nj))

        # print bs
        for (r, c) in tuple(bs):
            visit(r, c)
        # print bs

        for i in range(n):
            ss = list(board[i])
            for j in range(m):
                if (i, j) in bs:
                    continue
                if ss[j] == 'O':
                    ss[j] = 'X'
            board[i] = ''.join(ss)
            # print board


if __name__ == '__main__':
    s = Solution()
    s.solve(["XXXX", "XOOX", "XXOX", "XOXX"])
