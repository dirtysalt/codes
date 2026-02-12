#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        def isOK(k):
            j = 0
            c = 1
            for i in range(len(position)):
                if (position[i] - position[j]) < k:
                    continue
                j = i
                c += 1
            return c >= m

        s, e = 0, position[-1] - position[0]
        while s <= e:
            k = (s + e) // 2
            ok = isOK(k)
            # print(k, ok)
            if ok:
                s = k + 1
            else:
                e = k - 1
        ans = e
        return ans


cases = [
    ([1, 2, 3, 4, 7], 3, 3),
    ([5, 4, 3, 2, 1, 1000000000], 2, 999999999),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxDistance, cases)
