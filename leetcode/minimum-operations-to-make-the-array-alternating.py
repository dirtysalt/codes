#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        from collections import Counter
        a = Counter()
        b = Counter()
        ta, tb = 0, 0
        for i in range(len(nums)):
            x = nums[i]
            if i % 2 == 0:
                a[x] += 1
                ta += 1
            else:
                b[x] += 1
                tb += 1
        print(a, b)

        # preserve a top value.
        def compute(a, b, ta, tb):
            ans = 1 << 30
            for ka, va in a.most_common()[:1]:
                keep = 0
                for kb, vb in b.most_common():
                    if ka != kb:
                        # keep kb
                        keep = vb
                        break
                res = ta - va + tb - keep
                ans = min(ans, res)
            return ans

        c0 = compute(a, b, ta, tb)
        c1 = compute(b, a, tb, ta)
        return min(c0, c1)

true, false, null = True, False, None
cases = [
    ([3, 1, 3, 2, 4, 3], 3),
    ([1, 2, 2, 2, 2], 2),
    (
        [69, 91, 47, 74, 75, 94, 22, 100, 43, 50, 82, 47, 40, 51, 90, 27, 98, 85, 47, 14, 55, 82, 52, 9, 65, 90, 86, 45,
         52,
         52, 95, 40, 85, 3, 46, 77, 16, 59, 32, 22, 41, 87, 89, 78, 59, 78, 34, 26, 71, 9, 82, 68, 80, 74, 100, 6, 10,
         53,
         84, 80, 7, 87, 3, 82, 26, 26, 14, 37, 26, 58, 96, 73, 41, 2, 79, 43, 56, 74, 30, 71, 6, 100, 72, 93, 83, 40,
         28,
         79, 24], 84),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumOperations, cases)

if __name__ == '__main__':
    pass
