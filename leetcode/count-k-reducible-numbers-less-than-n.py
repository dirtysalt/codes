#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        n = len(s)
        cache = [0] * (n + 1)
        for x in range(2, n + 1):
            i = x
            b = 0
            while i:
                if i & 0x1:
                    b += 1
                i = i >> 1
            cache[x] = cache[b] + 1

        MOD = 10 ** 9 + 7
        import functools
        @functools.lru_cache(None)
        def dfs(i, c, less):
            if i == len(s):
                return 1 if (c > 0 and less and (cache[c] + 1) <= k) else 0

            ans = 0
            if less:
                ans += dfs(i + 1, c, True)
                ans += dfs(i + 1, c + 1, True)
            elif s[i] == '0':
                ans += dfs(i + 1, c, False)
            else:
                ans += dfs(i + 1, c, True)
                ans += dfs(i + 1, c + 1, False)

            return ans % MOD

        ans = dfs(0, 0, False)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ('111', 1, 3),
    ('1000', 2, 6),
    ('1', 3, 0),
]

aatest_helper.run_test_cases(Solution().countKReducibleNumbers, cases)

if __name__ == '__main__':
    pass
