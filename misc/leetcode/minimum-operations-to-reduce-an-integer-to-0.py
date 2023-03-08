#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def minOperations(self, n: int) -> int:
        import functools
        @functools.cache
        def search(x):
            if x & (x - 1) == 0: return 1
            # to get the lowest bit.
            lb = x & -x
            return 1 + min(search(x + lb), search(x - lb))

        return search(n)


class Solution:
    def minOperations(self, n: int) -> int:
        ans = 1
        while n & (n - 1):
            # to get the lowest bit.
            lb = n & -n
            if n & (lb << 1):
                n += lb
            else:
                n -= lb
            ans += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (39, 3),
    (54, 3)
]

aatest_helper.run_test_cases(Solution().minOperations, cases)

if __name__ == '__main__':
    pass
