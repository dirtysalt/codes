#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        def sim(s1, s2):
            ss1 = s1.split()
            ss2 = s2.split()

            for i in range(len(ss2)+1):
                # ss2[:i]
                # ss2[i:]
                a = ss2[:i]
                b = ss2[i:]

                if (not a or ss1[:len(a)] == a) and (not b or ss1[-len(b):] == b):
                    return True
            return False

        s1, s2 = sentence1, sentence2
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        return sim(s1, s2)


if __name__ == '__main__':
    pass
