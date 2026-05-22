#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param words: a string array
    @return: the maximum product
    """

    def maxProduct(self, words):
        # Write your code here

        def word2bits(word):
            value = 0
            for w in word:
                idx = ord(w) - ord('a')
                value |= (1 << idx)
            return value

        res = 0
        xs = [word2bits(w) for w in words]
        for i in range(len(xs)):
            x = xs[i]
            for j in range(i + 1, len(xs)):
                y = xs[j]
                if x & y == 0:
                    prod = len(words[i]) * len(words[j])
                    res = max(res, prod)
        return res
