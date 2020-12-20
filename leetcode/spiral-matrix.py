#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        n = len(matrix)
        if not n: return res
        m = len(matrix[0])
        if not m: return res
        (i, j) = (0, 0)
        nm = n * m

        # print '---'
        while True:
            # print (i, j) , (i, m-1-j) , (n-1-i, m-1-j) , (n-1-i, j)
            for c in range(j, m - j):
                res.append((i, c))
            # if len(res) == n * m: break

            for r in range(i + 1, n - i):
                res.append((r, m - 1 - j))
            # if len(res) == n * m: break

            for c in range(m - 2 - j, j - 1, -1):
                res.append((n - 1 - i, c))
            # if len(res) == n * m: break

            for r in range(n - 2 - i, i, -1):
                res.append((r, j))
            # if len(res) == n * m: break

            i += 1
            j += 1
            if len(res) >= nm: break

        res = res[:nm]
        res = [matrix[xy[0]][xy[1]] for xy in res]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))

    print(s.spiralOrder([
        [1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8],
        [7, 8, 9, 10, 11]
    ]))
