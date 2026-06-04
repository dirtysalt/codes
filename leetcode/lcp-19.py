#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumOperations(self, leaves: str) -> int:
        # (0..j), (j+1..i), (i+1..n-1)
        #    Y      X - Y     Z - X
        # (j+1) - Y # y -> r
        # X - Y # r -> y
        # (n-i-1) - Z + X # y -> r


        # total =(j+1)-Y+X-Y+(n-i-1)-Z+X
        #       = n-i+j+2*X-2*Y-Z = n-i+2*X-Z+(j-2*Y)
        #       = n - Z + (j-2*Y) - (i-2*X)
        # find min j-Y
        # j >= 0

        n = len(leaves)
        Z = 0
        for i in range(n):
            if leaves[i] == 'r':
                Z += 1

        X, Y = 0, 0
        if leaves[i] == 'r':
            X += 1
            Y += 1

        MinV = -2 * Y
        ans = n
        for i in range(1, n-1):
            if leaves[i] == 'r':
                X += 1
            V = i - 2 * X
            res = n - Z + MinV - V
            ans = min(res, ans)
            MinV = min(MinV, V)
        return ans

cases = [
    ("rrryyyrryyyrr", 2),
    ("ryr", 0),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().minimumOperations, cases)
