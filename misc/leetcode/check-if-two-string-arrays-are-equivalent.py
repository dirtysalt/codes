#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def walk(w):
            for i in range(len(w)):
                for c in w[i]:
                    yield c
            yield None

        for c1, c2 in zip(walk(word1), walk(word2)):
            if c1 != c2: return False

        return True
