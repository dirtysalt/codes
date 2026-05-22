#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        keys = pressedKeys
        MOD = 10 ** 9 + 7

        import functools

        @functools.lru_cache(maxsize=None)
        def search(i):
            if i == len(keys): return 1

            res = 0
            a = int(keys[i])
            sz = 3
            if a in (7, 9):
                sz = 4
            for j in range(i, min(i + sz, len(keys))):
                b = int(keys[j])
                if b == a:
                    res += search(j + 1)
                else:
                    break
            return res % MOD

        ans = search(0)
        return ans % MOD


true, false, null = True, False, None
cases = [
    ("22233", 8),
    ("222222222222222222222222222222222222", 82876089),
    ("344644885", 8),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countTexts, cases)

if __name__ == '__main__':
    pass
