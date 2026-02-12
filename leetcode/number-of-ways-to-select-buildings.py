#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def numberOfWays(self, s: str) -> int:
        ss = [0 if s[i] == '0' else 1 for i in range(len(s))]

        def search(ss):
            n = len(ss)
            # 01
            left = [0] * (n + 1)
            zero = 0
            for i in range(n):
                if ss[i] == 0:
                    zero += 1
                else:
                    left[i + 1] += zero
                left[i + 1] += left[i]

            # print(left)

            ans = 0
            for i in reversed(range(n)):
                if ss[i] == 0:
                    ans += left[i]
            return ans

        ans = search(ss)
        ans += search([1 - x for x in ss])
        return ans


true, false, null = True, False, None
cases = [
    ("001101", 6),
    ("11100", 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfWays, cases)

if __name__ == '__main__':
    pass
