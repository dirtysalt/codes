#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        mask = [-1] * n
        t = 0
        ans = 0
        for i in range(n):
            x = nums[i]
            if mask[x] != -1: continue
            t += 1
            while mask[x] == -1:
                mask[x] = t
                x = nums[x]
        # print(mask)

        from collections import Counter
        cnt = Counter()
        ans = 0
        for i in range(n):
            t = mask[i]
            cnt[t] += 1
            ans = max(ans, cnt[t])
        return ans

cases = [
    ([5,4,0,3,1,6,2], 4)
]

import aatest_helper
aatest_helper.run_test_cases(Solution().arrayNesting, cases)
