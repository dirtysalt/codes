#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numPermsDISequence(self, S: str) -> int:
        dp = {}
        MOD = 10 ** 9 + 7

        def run(s, ith, n):
            if s == len(S):
                assert n == 1
                # assert ith == 0
                return 1

            key = '{}.{}'.format(s, ith)
            if key in dp:
                return dp[key]

            ans = 0
            # 当前有那个n选择，ith属于[0,n-1].
            if S[s] == 'I':
                for j in range(ith + 1, n):
                    # 选择了j之后，那么剩余选择是n-1个
                    # 但是注意对于下一轮来说，它的编号其实是j-1.
                    ans += run(s + 1, j - 1, n - 1)
            else:
                for j in range(0, ith):
                    # 选择了j之后，剩余选择是n-1个
                    # 对于下一轮来说，它的编号其实是j
                    ans += run(s + 1, j, n - 1)

            dp[key] = ans
            return ans

        n = len(S) + 1
        ans = 0
        for ith in range(n):
            ans += run(0, ith, n)
        return ans % MOD


cases = [
    ("DID", 5),
    ("I", 1),
    ("ID", 2),
    ("IDDDIIDIIIIIIIIDIDID", 853197538)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numPermsDISequence, cases)
