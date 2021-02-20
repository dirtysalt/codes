#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        n = len(A)

        for d in (-1, 1):
            ok = True
            for i in range(1, n):
                x = A[i] - A[i - 1]
                if (x * d) < 0:
                    ok = False
                    break
            if ok:
                return True
        return False
