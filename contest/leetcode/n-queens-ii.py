#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]
        if n == 0: return res[0]

        def f(idx, r):
            if idx == n:
                res[0] += 1
                return
            for i in range(0, n):
                r[idx] = i
                ok = True
                for j in range(0, idx):
                    if r[j] == i or \
                                    abs(r[j] - r[idx]) == abs(idx - j):
                        ok = False
                        break

                if ok:
                    f(idx + 1, r)

        r = [0] * n
        f(0, r)
        return res[0]


if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(1))
