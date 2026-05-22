#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        maxK = len(sequence) // len(word)

        for k in reversed(range(1, maxK + 1)):
            s = word * k
            if sequence.find(s) != -1:
                return k

        return 0
