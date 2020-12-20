#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 这题目难度不大，但是写起来比较麻烦。
# 另外一种办法是通过二分搜索最近的值

class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        A, B = B, A
        ax = list(enumerate(A))
        ax.sort(key=lambda x: x[1])
        bx = list(enumerate(B))
        bx.sort(key=lambda x: x[1])

        n = len(A)

        sel = []
        i, j = 0, 0
        while i < n and j < n:
            if ax[i][1] >= bx[j][1]:
                j += 1
            else:
                sel.append((i, j))
                i += 1
                j += 1

        ans = [0] * n
        ans_set = [0] * n
        bx_set = [0] * n
        for x, y in sel:
            ans[ax[x][0]] = bx[y][1]
            ans_set[ax[x][0]] = 1
            bx_set[y] = 1

        i, j = 0, 0
        for i in range(n):
            if ans_set[i]:
                continue
            while bx_set[j]:
                j += 1
            ans[i] = bx[j][1]
            bx_set[j] = 1
            ans_set[i] = 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    A = [2, 7, 11, 15]
    B = [1, 10, 4, 11]
    print(sol.advantageCount(A, B))
    A = [12, 24, 8, 32]
    B = [13, 25, 32, 11]
    print(sol.advantageCount(A, B))
