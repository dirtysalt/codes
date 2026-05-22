#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        # write your code here

        n = len(A)
        s, e = 0, n - 1
        while s <= e:
            m = (s + e) // 2
            if A[m] >= target:
                e = m - 1
            else:
                s = m + 1
        # A[e] < target and A[s] >= target
        res = []
        INF = 1 << 31
        while len(res) < k:
            e_abs = INF if e < 0 else abs(A[e] - target)
            s_abs = INF if s >= n else abs(A[s] - target)
            if s_abs >= e_abs:
                res.append(A[e])
                e -= 1
            else:
                res.append(A[s])
                s += 1
        return res
