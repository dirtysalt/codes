#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict


class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """

    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here

        d = defaultdict(set)
        for x, y in pairs:
            d[x].add(y)
            d[y].add(x)

        if len(words1) != len(words2):
            return False

        for i in range(len(words1)):
            w1 = words1[i]
            w2 = words2[i]
            if w1 == w2:
                continue
            if (w2 in d and w1 in d[w2]) or (w1 in d and w2 in d[w1]):
                continue
            return False
        return True
