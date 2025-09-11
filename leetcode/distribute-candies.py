#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candies.sort()
        n = len(candies)
        last = None
        res = 0
        for i in range(n):
            if candies[i] != last:
                res += 1
                last = candies[i]
        return min(res, n // 2)


def test():
    cases = [
        ([1, 1, 2, 2, 3, 3], 3),
        ([1, 1, 2, 3], 2)
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (ms, exp) = c
        res = sol.distributeCandies(ms)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
