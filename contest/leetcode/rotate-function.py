#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List

from leetcode.aatest_helper import run_test_cases


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        B = A + A
        res, n = 0, len(A)

        for i in range(n):
            res += i * B[i]

        for i in range(n):
            value = 0
            for j in range(n):
                value += j * B[(i + j)]
            # print(value)
            res = max(res, value)
        return res


"""
这题目开始没有想到特别好的办法，尤其是盯着公式似乎看不出什么诀窍出来。
但是如果仔细看case就会发现规律

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

观察F(1)-F(0)的差异：
- (1*4)-(0*4) + (2*3)-(2*2) + (3*2)-(2*2)
- (0*6)-(3*6)
就是是说，除了最后一个元素x之外，剩余每个元素都加上，而这个元素x是-(n-1)*x

同理观察F(2)-F(1)的差异也是如此

非常有意思：）
"""


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n, acc = len(A), sum(A)
        value = 0
        for i in range(n):
            value += i * A[i]
        res = value

        for i in range(n - 1, 0, -1):
            exclude = A[i]
            delta = -exclude * (n - 1) + (acc - exclude)
            value += delta
            res = max(res, value)
        return res


cases = [
    ([4, 3, 2, 6], 26)
]
sol = Solution()
fn = sol.maxRotateFunction
run_test_cases(fn, cases)
