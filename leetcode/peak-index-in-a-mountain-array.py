#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        n = len(A)
        for i in range(n):
            if ((i - 1) >= 0 and A[i] > A[i - 1]) and \
                    ((i + 1) < n and A[i] > A[i + 1]):
                return i
        raise AssertionError("IP")


def test():
    cases = [
        ([0, 1, 0], 1),
        ([0, 2, 1, 0], 1)
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (A, exp) = c
        res = sol.peakIndexInMountainArray(A)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
