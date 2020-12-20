#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


"""
可以互换的前提是行列里面只能有两种值a, b.
1. a & b = 0
2. a | b = (1 << n) - 1
3. a, b的数量各占一半或者是k+1,k
然后在计算swap次数的时候，假设0110要变成0101的
只需要计算有差异的位置个数
"""


class Solution:
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        n = len(board)

        # for i in range(n):
        #     print(board[i])

        def try_swap(xs):
            cnt = 0
            temp = []
            for i in range(n):
                if xs[i] == xs[0]:
                    cnt += 1
                    temp.append(0)
                elif ((xs[0] & xs[i]) == 0) and ((xs[0] | xs[i]) == (1 << n) - 1):
                    temp.append(1)
                else:
                    return -1
            if abs(n - cnt - cnt) > 1:
                return -1

            cnt0, cnt1 = 0, 0
            exp = 0
            for i in range(n):
                if temp[i] != exp:
                    cnt0 += 1
                if temp[i] != (1 - exp):
                    cnt1 += 1
                exp = 1 - exp

            res = 1 << 10
            if cnt0 % 2 == 0:
                res = min(res, cnt0 // 2)
            if cnt1 % 2 == 0:
                res = min(res, cnt1 // 2)
            return res

        ans = 0
        # handle row
        xs = []
        for i in range(n):
            value = 0
            for j in range(n):
                value = (value << 1) | board[i][j]
            xs.append(value)
        res = try_swap(xs)
        if res == -1:
            return -1
        ans += res

        # handle col
        xs = []
        for j in range(n):
            value = 0
            for i in range(n):
                value = (value << 1) | board[i][j]
            xs.append(value)
        res = try_swap(xs)
        if res == -1:
            return -1
        ans += res
        return ans


if __name__ == '__main__':
    sol = Solution()
    board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
    print(sol.movesToChessboard(board))
    board = [[0, 1], [1, 0]]
    print(sol.movesToChessboard(board))
    board = [[1, 0], [1, 0]]
    print(sol.movesToChessboard(board))
    board = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]
    print(sol.movesToChessboard(board))
    board = [[1, 0, 1, 1, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1]]
    print(sol.movesToChessboard(board))
