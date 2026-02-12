#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        from sortedcontainers import SortedList
        sl = SortedList(nums[:dist + 1])

        # nums[0] is must,
        # we are going to select min-k from `dist`th elements.
        k -= 1
        now = 0
        ans = (1 << 63)
        for i in range(k):
            now += sl[i]

        # special cases, can not be well handled
        if (dist + 1) == k:
            for i in range(1, len(nums) - k + 1):
                now -= nums[i - 1]
                now += nums[i + dist]
                ans = min(ans, now)
            return ans + nums[0]

        for i in range(1, len(nums) - k + 1):
            # remove nums[i-1]
            # add nums[i + dist]

            x = nums[i - 1]
            if x <= sl[k - 1]:
                now -= x
                now += sl[k]
            sl.remove(x)

            if (i + dist) < len(nums):
                x = nums[i + dist]
                if x <= sl[k - 1]:
                    now -= sl[k - 1]
                    now += x
                sl.add(x)
            ans = min(ans, now)
        return ans + nums[0]


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[1, 3, 2, 6, 4, 2], k=3, dist=3, res=5),
    aatest_helper.OrderedDict(nums=[10, 1, 2, 2, 2, 1], k=4, dist=3, res=15),
    aatest_helper.OrderedDict(nums=[10, 8, 18, 9], k=3, dist=1, res=36),
]

aatest_helper.run_test_cases(Solution().minimumCost, cases)

if __name__ == '__main__':
    pass
