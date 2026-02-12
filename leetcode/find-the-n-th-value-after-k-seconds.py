#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        ans = [1] * n
        MOD = 10 ** 9 + 7
        # a[0], a[0]+a[1], a[0]+a[1]+a[2]
        # a[0], 2*a[0]+a[1], 2*(a[0]+a[1])+a[2]
        # a[0], 3*a[1]+a[1], 4*a[0]+3a[1]+a[2]
        for _ in range(k):
            for i in range(1, n):
                ans[i] += ans[i - 1]
                ans[i] %= MOD
        return ans[-1]


if __name__ == '__main__':
    pass
