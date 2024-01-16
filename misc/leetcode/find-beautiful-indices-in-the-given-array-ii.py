#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class KMP2:
    @staticmethod
    def build_max_match(t):
        n = len(t)
        match = [0] * n
        c = 0
        for i in range(1, n):
            v = t[i]
            while c and t[c] != v:
                c = match[c - 1]
            if t[c] == v:
                c += 1
            match[i] = c
        return match

    def __init__(self, t):
        self.t = t
        self.max_match = self.build_max_match(t)

    def search(self, s):
        match = self.max_match
        t = self.t
        c = 0
        pos = []
        for i, v in enumerate(s):
            while c and t[c] != v:
                c = match[c - 1]
            if t[c] == v:
                c += 1
            if c == len(t):
                pos.append(i - len(t) + 1)
                c = match[c - 1]
        return pos


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def build_position(s, t):
            kmp2 = KMP2(t)
            return kmp2.search(s)

        A = build_position(s, a)
        B = build_position(s, b)

        ans = []
        j = 0
        for i in range(len(A)):
            while j < len(B) and B[j] < A[i]:
                j += 1

            # j == len(B) or B[j] >= A[i]
            ok = False
            for d in (-1, 0):
                j2 = j + d
                if 0 <= j2 < len(B) and abs(B[j2] - A[i]) <= k:
                    ok = True
                    break
            if ok:
                ans.append(A[i])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(s="isawsquirrelnearmysquirrelhouseohmy", a="my", b="squirrel", k=15, res=[16, 33]),
    aatest_helper.OrderedDict(s="abcd", a="a", b="a", k=4, res=[0]),
]

# cases += aatest_helper.read_cases_from_file('tmp.in', 5)
aatest_helper.run_test_cases(Solution().beautifulIndices, cases)

if __name__ == '__main__':
    pass
