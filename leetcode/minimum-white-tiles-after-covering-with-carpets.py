#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        import functools
        @functools.lru_cache(maxsize=None)
        def search(i, k):
            if i >= len(floor):
                return 0

            # don't use it
            a = search(i + 1, k)
            if floor[i] == '1':
                a += 1
            if k > 0:
                b = search(i + carpetLen, k - 1)
                a = min(a, b)
            return a

        ans = search(0, numCarpets)
        return ans


true, false, null = True, False, None
cases = [
    ("10110101", 2, 2, 2),
    ("11111", 2, 3, 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumWhiteTiles, cases)

if __name__ == '__main__':
    pass
