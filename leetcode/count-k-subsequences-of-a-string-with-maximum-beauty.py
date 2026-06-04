#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        cnt = [0] * 26
        for c in s:
            ci = ord(c) - ord('a')
            cnt[ci] += 1

        cnt.sort(reverse=True)
        n = 0
        while n < 26 and cnt[n]:
            n += 1
        if k > n: return 0

        rep = cnt[k - 1]
        t = k
        while t < n and cnt[t] == rep:
            t += 1
        f = k - 1
        while f >= 0 and cnt[f] == rep:
            f -= 1
        f += 1

        MOD = 10 ** 9 + 7

        # [0..f-1], [f..t]
        ans = 1
        for i in range(f):
            ans *= cnt[i]
            ans = ans % MOD

        # print(f, t, cnt[:n])

        if (k - f) > 0:
            # select (k-f) from [t-f]
            # C(t-f, k-f) * (cnt[k] ^ (k-f))

            @functools.cache
            def C(n, m):
                if m == 0: return 1
                if n == m: return 1
                return (C(n - 1, m - 1) + C(n - 1, m)) % MOD

            ans = ans * C(t - f, k - f)
            for _ in range(k - f):
                ans = (ans * rep) % MOD
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("bcca", 2, 4,),
    ("abbcd", 4, 2),
    ("fkp", 2, 3),
    ("jyuhiyzjuk", 2, 12),
    ("abcdefghijklmnopqrstuvwxyz", 26, 1),
]

aatest_helper.run_test_cases(Solution().countKSubsequencesWithMaxBeauty, cases)

if __name__ == '__main__':
    pass
