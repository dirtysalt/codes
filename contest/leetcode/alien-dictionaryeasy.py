#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param words: the array of string means the list of words
    @param order: a string indicate the order of letters
    @return: return true or false
    """

    def isAlienSorted(self, words, order):
        if not words:
            return True
        tmp = {}
        for i, c in enumerate(order):
            tmp[c] = i
        words = [tuple((tmp[x] for x in w)) for w in words]
        for i in range(1, len(words)):
            if words[i - 1] > words[i]:
                return False
        return True
