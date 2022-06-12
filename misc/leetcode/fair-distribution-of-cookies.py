#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
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


true, false, null = True, False, None
cases = [
    ([8, 15, 10, 20, 8], 2, 31),
    ([6, 1, 3, 2, 2, 4, 1, 2], 3, 7),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().distributeCookies, cases)

if __name__ == '__main__':
    pass
