#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        def gcd(a, b):
            while True:
                c = a % b
                if c == 0:
                    return b
                a, b = b, c

        counter = Counter()
        ans = len(deck)
        for x in deck:
            counter[x] += 1
        for v in counter.values():
            ans = gcd(ans, v)
        return ans >= 2
