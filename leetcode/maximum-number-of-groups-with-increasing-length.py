# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        xs = usageLimits.copy()
        n = len(xs)
        xs.append(0)

        ans = 1
        for i in range(n):
            if xs[i] >= ans:
                xs[i] -= ans
                ans += 1
            xs[i + 1] += xs[i]
        return ans - 1


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort(reverse=True)

        def test(K):
            gap = 0
            for x in usageLimits:
                gap = min(gap + x - K, 0)
                if K > 0:
                    K -= 1
            return gap >= 0

        s, e = 1, len(usageLimits)
        while s <= e:
            k = (s + e) // 2
            if test(k):
                s = k + 1
            else:
                e = k - 1
        return e


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 5], 3),
    ([2, 1, 2], 2),
    ([1, 1], 1),
    ([1, 1, 2, 10, 9, 2], 5),
]

aatest_helper.run_test_cases(Solution().maxIncreasingGroups, cases)

if __name__ == '__main__':
    pass
