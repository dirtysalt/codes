#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        import functools

        @functools.cache
        def A(n, m):
            r = 1
            for x in range(n - m + 1, n + 1):
                r *= x
            return r

        digit = 1
        ans = 0
        while 10 ** digit <= n:
            ans += 9 * A(9, digit - 1)
            digit += 1

        seq = []
        x = n
        while x:
            seq.append(x % 10)
            x = x // 10
        seq = seq[::-1]
        mask = [0] * 10

        def search(i, seq, mask):
            if i == len(seq): return 1
            r = 0
            start = 1 if i == 0 else 0
            for x in range(start, seq[i]):
                if mask[x] == 1: continue
                r += A(9 - i, len(seq) - i - 1)

            if mask[seq[i]] == 0:
                mask[seq[i]] = 1
                r += search(i + 1, seq, mask)
            return r

        ans += search(0, seq, mask)

        return ans


true, false, null = True, False, None
cases = [
    (20, 19),
    (5, 5),
    (135, 110),
    (10, 10),
    (2000000000, 5974650)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countSpecialNumbers, cases)

if __name__ == '__main__':
    pass
