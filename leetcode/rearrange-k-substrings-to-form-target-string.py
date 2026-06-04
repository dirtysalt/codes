#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        def cut(s):
            n = len(s)
            sz = n // k
            arr = []
            for i in range(k):
                arr.append(s[i * sz:i * sz + sz])
            return arr

        a = sorted(cut(s))
        b = sorted(cut(t))
        # print(a, b)
        return a == b


true, false, null = True, False, None
import aatest_helper

cases = [
    ("yu", "uy", 2, true),
]

aatest_helper.run_test_cases(Solution().isPossibleToRearrange, cases)

if __name__ == '__main__':
    pass
