#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        n = children
        m = money
        if m < n: return -1

        c = [1] * n
        ans = 0
        last = -1
        m -= n
        for i in range(n):
            if m >= 7:
                c[i] += 7
                m -= 7
                ans += 1
            else:
                c[i] += m
                last = i
                m = 0
                break

        if m > 0:
            ans -= 1
        elif c[last] == 4 and last == n - 1:
            ans -= 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (17, 2, 1),
    (20, 3, 1),
    (16, 2, 2),
]

aatest_helper.run_test_cases(Solution().distMoney, cases)

if __name__ == '__main__':
    pass
