#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # 二分判断最大值，可以通过O(8! * 8)判定 ~= 2,580,480
        # 所以时间上看上去还比较紧
        def test(x):
            import itertools
            for cks in itertools.permutations(cookies):
                kk = k
                tt = x
                ok = True
                for ck in cks:
                    if tt < ck:
                        tt = x
                        kk -= 1
                    if kk == 0:
                        ok = False
                        break
                    tt -= ck
                if ok:
                    return True
            return False

        s, e = max(cookies), sum(cookies)
        while s <= e:
            m = (s + e) // 2
            ok = test(m)
            if ok:
                e = m - 1
            else:
                s = m + 1
        return s

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)

        S = [0] * (1 << n)
        for st in range(1<<n):
            t = 0
            for i in range(n):
                if st & (1 << i):
                    t += cookies[i]
            S[st] = t

        inf = 1 << 30
        dp = [inf] * (1 << n)
        dp[0] = 0
        # O(8 * 256* 256)
        for i in range(k):
            # 状态顺序是从大到小，否则会多次更新
            for st in reversed(range(1 << n)):
                mask = (1 << n) - 1 - st
                st2 = (1 << n) - 1
                while st2 > 0:
                    st2 = st2 & mask
                    dp[st | st2] = min(dp[st | st2], max(dp[st], S[st2]))
                    st2 -= 1
        return dp[-1]

true, false, null = True, False, None
cases = [
    ([8, 15, 10, 20, 8], 2, 31),
    ([6, 1, 3, 2, 2, 4, 1, 2], 3, 7),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().distributeCookies, cases)

if __name__ == '__main__':
    pass
