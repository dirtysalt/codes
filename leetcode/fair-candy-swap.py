#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        sumA = sum(A)
        sumB = sum(B)
        diff = (sumA - sumB) // 2
        setB = set()
        for x in B:
            setB.add(x)
        ans = []
        for x in A:
            exp = x - diff
            if exp in setB:
                ans = [x, exp]
                break
        return ans
