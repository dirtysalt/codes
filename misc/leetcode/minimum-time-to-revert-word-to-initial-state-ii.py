#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class KMP:
    @staticmethod
    def build_max_match(t):
        n = len(t)
        match = [0] * n
        c = 0

        def eq(a, b):
            sz = min(len(a), len(b))
            return a[:sz] == b[:sz]

        for i in range(1, n):
            v = t[i]
            while c and not eq(t[c], v):
                c = match[c - 1]
            if eq(t[c], v):
                c += 1
            match[i] = c
        return match


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        w = []
        i = 0
        while i < len(word):
            w.append(word[i:i + k])
            i += k
        match = KMP.build_max_match(w)
        ans = len(match) - match[-1]
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(word="abacaba", k=3, res=2),
    aatest_helper.OrderedDict(word="abacaba", k=4, res=1),
    aatest_helper.OrderedDict(word="abcbabcd", k=2, res=4),
    ("aabaaaa", 1, 5),
    ("ababa", 2, 1),
    ("aaaaba", 1, 5),
]

aatest_helper.run_test_cases(Solution().minimumTimeToInitialState, cases)

if __name__ == '__main__':
    pass
