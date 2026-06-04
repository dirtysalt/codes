#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        def test(nums):
            ans = 0
            X = 1
            for x in nums:
                t = (x + X - 1) // X
                ans += t
                X += K
            return ans

        ans = 1 << 30
        import itertools
        for nums in itertools.permutations(strength):
            res = test(nums)
            ans = min(ans, res)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(strength=[1, 4, 3], K=1, res=4),
    aatest_helper.OrderedDict(strength=[2, 5, 4], K=2, res=5),
    ([23, 45, 45], 6, 34)
]

aatest_helper.run_test_cases(Solution().findMinimumTime, cases)

if __name__ == '__main__':
    pass
