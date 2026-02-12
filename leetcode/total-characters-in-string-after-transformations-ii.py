#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        cnt = [[0] for _ in range(26)]
        for c in s:
            i = ord(c) - ord('a')
            cnt[i][0] += 1

        MOD = 10 ** 9 + 7
        T = [[0] * 26 for _ in range(26)]
        for i in range(26):
            rep = nums[i]
            for j in range(rep):
                T[(i + j + 1) % 26][i] = 1

        # print(cnt, T)

        def mat_mul(a, b, MOD):
            R, K, C = len(a), len(a[0]), len(b[0])
            res = [[0] * C for _ in range(R)]
            for k in range(K):
                for i in range(R):
                    for j in range(C):
                        res[i][j] += (a[i][k] * b[k][j]) % MOD
                        res[i][j] %= MOD
            return res

        def mat_pow(a, b, MOD):
            assert (len(a) == len(a[0]))
            d = len(a)
            ans = [[0] * d for _ in range(d)]
            for i in range(d):
                ans[i][i] = 1

            while b:
                if b & 0x1:
                    ans = mat_mul(a, ans, MOD)
                a = mat_mul(a, a, MOD)
                b = b >> 1
            return ans

        T2 = mat_pow(T, t, MOD)
        R = mat_mul(T2, cnt, MOD)
        ans = 0
        for i in range(26):
            ans += R[i][0]
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(s="abcyy", t=2,
                              nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                              res=7),
    aatest_helper.OrderedDict(s="azbk", t=1,
                              nums=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                              res=8),
    ("k", 2, [2, 2, 1, 3, 1, 1, 2, 3, 3, 2, 1, 2, 2, 1, 1, 3, 1, 2, 2, 1, 3, 3, 3, 2, 2, 1], 2),
]

aatest_helper.run_test_cases(Solution().lengthAfterTransformations, cases)

if __name__ == '__main__':
    pass
