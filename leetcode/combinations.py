#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []

        def f(idx, r):
            if len(r) == k:
                res.append(r[:])
                return
            rest = k - len(r)
            for i in range(idx, n - rest + 1):
                r.append(i + 1)
                f(i + 1, r)
                r.pop()

        r = []
        f(0, r)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
