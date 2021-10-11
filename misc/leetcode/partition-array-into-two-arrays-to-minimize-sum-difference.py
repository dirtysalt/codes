#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        LST = (sum(nums) + 1) // 2
        n = len(nums) // 2

        def search(A, B):
            import itertools
            rs0 = itertools.combinations(range(n), A)
            rs1 = itertools.combinations(range(n), B)
            xs = []
            ys = []
            for r in rs0:
                x = sum((nums[i] for i in r))
                xs.append(x)
            for r in rs1:
                x = sum((nums[i + n] for i in r))
                ys.append(x)

            xs.sort()
            ys.sort()

            j = len(ys) - 1
            ans = 1 << 30
            for x in xs:
                if ys[j] + x >= LST:
                    while j >= 0 and ys[j] + x >= LST:
                        j -= 1
                    j += 1
                    ans = min(ans, ys[j] + x)

            return ans

        ans = 1 << 30
        for A in range(n + 1):
            res = search(A, n - A)
            ans = min(ans, res)

        other = sum(nums) - ans
        return ans - other


true, false, null = True, False, None
cases = [
    ([3, 9, 7, 3], 2),
    ([-36, 36], 72),
    ([2, -1, 0, 4, -2, -9], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumDifference, cases)

if __name__ == '__main__':
    pass
