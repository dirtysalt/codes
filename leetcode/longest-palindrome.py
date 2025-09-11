#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here

        d = defaultdict(int)
        for c in s:
            d[c] += 1

        items = list(d.items())
        res = 0
        center = 0
        for k, v in items:
            res += (v // 2) * 2
            center |= v % 2
        res += center
        return res
