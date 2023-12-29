#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def find_length(fences, sz):
            a = [1] + fences + [sz]
            a.sort()
            values = set()
            for i in range(len(a)):
                for j in range(i + 1, len(a)):
                    values.add(a[j] - a[i])
            return values

        hs = find_length(hFences, m)
        vs = find_length(vFences, n)
        ans = -1
        for h in hs:
            if h in vs:
                ans = max(ans, h * h)
        MOD = 10 ** 9 + 7
        if ans >= MOD:
            ans = ans % MOD
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(m=4, n=3, hFences=[2, 3], vFences=[2], res=4),
    aatest_helper.OrderedDict(m=6, n=7, hFences=[2], vFences=[4], res=-1)
]

aatest_helper.run_test_cases(Solution().maximizeSquareArea, cases)

if __name__ == '__main__':
    pass
