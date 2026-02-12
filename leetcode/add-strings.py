#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        n = len(num1)
        m = len(num2)
        res = []
        for i in range(max(n,m) + 1):
            va = ord(num1[i]) - ord('0') if i < n else 0
            vb = ord(num2[i]) - ord('0') if i < m else 0
            carry += va + vb
            vc = carry % 10
            carry //= 10
            res.append(chr(vc + ord('0')))
        if res[-1] == '0':
            res = res[:-1]
        res = res[::-1]
        res = ''.join(res)
        return res
