#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import deque
        nums.sort()

        # dq includes unique values in [x, x + len(nums) - 1]
        dq = deque()
        j = 0
        ans = 0
        for x in nums:
            to = x + len(nums) - 1

            while dq and dq[0] < x:
                dq.popleft()

            while j < len(nums) and nums[j] <= to:
                y = nums[j]
                if not dq or dq[-1] != y:
                    dq.append(y)
                j += 1

            ans = max(ans, len(dq))

        return len(nums) - ans


true, false, null = True, False, None
cases = [
    ([4, 2, 5, 3], 0),
    ([1, 2, 3, 5, 6], 1),
    ([1, 10, 100, 1000], 3),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minOperations, cases)

if __name__ == '__main__':
    pass
