#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        A = []
        for i in range(len(s) - len(a) + 1):
            if s[i:i + len(a)] == a:
                A.append(i)

        B = []
        for i in range(len(s) - len(b) + 1):
            if s[i:i + len(b)] == b:
                B.append(i)

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

aatest_helper.run_test_cases(Solution().beautifulIndices, cases)

if __name__ == '__main__':
    pass
