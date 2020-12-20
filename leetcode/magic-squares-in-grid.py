#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])
        if n == 0 or m == 0: return 0

        def check(r, c):
            nums = [0] * 10
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    v = grid[i][j]
                    if v < 0 or v > 9 or nums[v] == 1:
                        return False
                    nums[v] = 1

            val = 15
            for i in range(r, r + 3):
                res = 0
                for j in range(c, c + 3):
                    res += grid[i][j]
                if res != val:
                    return False

            for j in range(c, c + 3):
                res = 0
                for i in range(r, r + 3):
                    res += grid[i][j]
                if res != val:
                    return False

            res = 0
            for k in range(3):
                res += grid[r + k][c + k]
            if res != val:
                return False

            res = 0
            for k in range(3):
                res += grid[r + k][c + 2 - k]
            if res != val:
                return False
            return True

        ans = 0
        for i in range(n - 2):
            for j in range(m - 2):
                # print(i, j)
                if check(i, j):
                    ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    grid = [[4, 3, 8, 4],
            [9, 5, 1, 9],
            [2, 7, 6, 2]]
    print(sol.numMagicSquaresInside(grid))
    grid = [[10, 3, 5],
            [1, 6, 11],
            [7, 9, 2]]
    print(sol.numMagicSquaresInside(grid))
