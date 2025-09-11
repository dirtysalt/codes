#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def outer(sz):
            return 12 * (sz - 1) * (sz - 1)

        def length(sz):
            return 8 * (sz - 1)

        sz = 1
        acc = 0
        while True:
            acc += outer(sz)
            if acc >= neededApples:
                break
            sz += 1

        return length(sz)


true, false, null = True, False, None
cases = [
    (1, 8),
    (13, 16),
    (1000000000, 5040),
    (2784381467700, 70896)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumPerimeter, cases)

if __name__ == '__main__':
    pass
