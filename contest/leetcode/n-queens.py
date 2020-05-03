#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        if n == 0: return res

        def f(idx, r):
            if idx == n:
                res.append(tuple(r))
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

        res2 = []
        for r in res:
            m = []
            for i in range(0, n):
                m.append(['.'] * n)
                m[-1][r[i]] = 'Q'
            res2.append([''.join(x) for x in m])

        return res2


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
