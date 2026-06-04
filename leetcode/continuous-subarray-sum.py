#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i - 1] == 0 and nums[i] == 0:
                    return True
            return False

        values = set()
        from collections import deque
        dq = deque()

        acc = 0
        dq.append(acc)
        for x in nums:
            if len(dq) == 2:
                r = dq.popleft()
                values.add(r)

            acc += x
            acc %= k
            if acc in values:
                return True
            dq.append(acc)

        return False


cases = [
    ([23, 2, 4, 6, 7], 6, True),
    ([23, 2, 6, 4, 7], 6, True),
    ([23, 2, 6], 6, False),
    ([0, 0], 0, True),
    ([0, 1, 0], 0, False),
    ([1, 1, ], 0, False),
    ([0], 0, False)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().checkSubarraySum, cases)
