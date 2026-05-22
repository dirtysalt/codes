#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        depth = {}
        for x in nums:
            depth[x] = 0

        ans = 0
        for x in nums:
            if depth[x] != 0:
                continue

            i = x
            while i in depth:
                i -= 1
            i += 1

            sz = 1
            while i in depth:
                depth[i] = sz
                sz += 1
                i += 1
            ans = max(ans, sz - 1)
        return ans


cases = [
    ([100, 4, 200, 1, 3, 2], 4)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestConsecutive, cases)
