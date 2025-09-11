#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """

        digit = 0

        K -= 1
        N -= 1
        for i in range(N - 1, -1, -1):
            bit = (K >> i) & 0x1
            if digit == 0:
                if bit == 0:
                    digit = 0
                else:
                    digit = 1
            else:
                if bit == 0:
                    digit = 1
                else:
                    digit = 0
        return digit
