#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def pow(a, b, MOD):
            r = 1
            while b:
                if b & 0x1:
                    r = (r * a) % MOD
                a = (a * a) % MOD
                b = b >> 1
            return r

        import functools
        @functools.cache
        def search(k, st):
            if st == 0:
                return pow(26, k, MOD)
            if k == 0:
                return 0
            a, b, c = (st >> 2), (st >> 1) & 0x1, st & 0x1
            r = 0
            rep = 23
            if a > 0:
                r += search(k - 1, ((a - 1) << 2) | (b << 1) | c)
            else:
                rep += 1
            if b > 0:
                r += search(k - 1, (a << 2) | ((b - 1) << 1) | c)
            else:
                rep += 1
            if c > 0:
                r += search(k - 1, (a << 2) | (b << 1) | (c - 1))
            else:
                rep += 1
            r += rep * search(k - 1, st)
            r = r % MOD
            return r

        st = (2 << 2) | (1 << 1) | 1
        ans = search(n, st)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (4, 12),
    (10, 83943898),
]

aatest_helper.run_test_cases(Solution().stringCount, cases)

if __name__ == '__main__':
    pass
