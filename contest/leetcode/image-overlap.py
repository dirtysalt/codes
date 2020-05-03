#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """

        n = len(A)

        Ax = [0] * n
        Bx = [0] * n
        for i in range(n):
            val1 = 0
            val2 = 0
            for j in range(n):
                val1 = (val1 << 1) + A[i][j]
                val2 = (val2 << 1) + B[i][j]
            Ax[i] = val1
            Bx[i] = val2

        # print(Ax, Bx)

        def check(r, c, Ax, Bx):
            res = 0
            for i in range(r, n):
                mask = (1 << (n - c)) - 1
                val = (Ax[i] & mask) & (Bx[i - r] >> c)
                while val:
                    if val & 0x1:
                        res += 1
                    val = val // 2
            return res

        ans = 0
        for i in range(n):
            for j in range(n):
                res = check(i, j, Ax, Bx)
                ans = max(ans, res)
                res = check(i, j, Bx, Ax)
                ans = max(ans, res)

        return ans


if __name__ == '__main__':
    sol = Solution()
    A = [[1, 1, 0],
         [0, 1, 0],
         [0, 1, 0]]
    B = [[0, 0, 0],
         [0, 1, 1],
         [0, 0, 1]]
    print(sol.largestOverlap(A, B))
