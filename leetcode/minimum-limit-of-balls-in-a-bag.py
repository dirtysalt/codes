#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def test(V):
            ans = 0
            for x in nums:
                split = (x + V - 1) // V - 1
                ans += split
                if ans > maxOperations:
                    return False
            return True

        s, e = 1, max(nums)
        while s <= e:
            m = (s + e) // 2
            ok = test(m)
            # print(s, e, m, ok)
            if ok:
                e = m - 1
            else:
                s = m + 1
        ans = s
        return ans


cases = [
    ([9], 2, 3),
    ([2, 4, 8, 2], 4, 2),
    ([7, 17], 2, 7)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().minimumSize, cases)
