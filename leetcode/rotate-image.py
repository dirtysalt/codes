#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = matrix
        n = len(matrix)
        for i in range(0, n // 2):
            for j in range(i, n - 1 - i):
                # print (i, j), (j, n-1-i), (n-1-i, n-1-j), (n-1-j, i)
                v = m[n - 1 - j][i]

                m[n - 1 - j][i] = m[n - 1 - i][n - 1 - j]
                m[n - 1 - i][n - 1 - j] = m[j][n - 1 - i]
                m[j][n - 1 - i] = m[i][j]
                m[i][j] = v


if __name__ == '__main__':
    s = Solution()
    m = [[1, 2], [3, 4]]
    s.rotate(m)
    print(m)
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(m)
    print(m)
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    s.rotate(m)
    print(m)
