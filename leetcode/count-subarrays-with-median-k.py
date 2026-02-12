#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        from sortedcontainers import SortedList
        from collections import Counter
        p = nums.index(k)

        def precompute():
            sl = SortedList()
            cnt = Counter()
            for i in range(p, n):
                sl.add(nums[i])
                x = sl.bisect_left(k)
                # right number - left number
                diff = (len(sl) - 1 - x) - x
                cnt[diff] += 1
            return cnt

        def compute(cnt):
            sl = SortedList()
            ans = 0
            for i in reversed(range(p + 1)):
                sl.add(nums[i])
                x = sl.bisect_left(k)
                # left number - right number
                diff = x - (len(sl) - 1 - x)
                ans += cnt[diff]
                ans += cnt[diff + 1]
            return ans

        cnt = precompute()
        ans = compute(cnt)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 2, 1, 4, 5], 4, 3),
    ([2, 3, 1], 3, 1),
]

aatest_helper.run_test_cases(Solution().countSubarrays, cases)

if __name__ == '__main__':
    pass
