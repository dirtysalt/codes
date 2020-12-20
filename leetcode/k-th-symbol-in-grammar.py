#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0

        sz = 1 << (N - 2)
        x = 0
        k = K - 1
        while sz:
            if k < sz:
                pass
            else:
                x = 1 - x
                k -= sz
            sz = sz // 2
        return x


sol = Solution()
N = 5
res = []
for K in range(1, (1 << (N - 1)) + 1):
    res.append(sol.kthGrammar(N, K))
print(''.join([str(x) for x in res]))
