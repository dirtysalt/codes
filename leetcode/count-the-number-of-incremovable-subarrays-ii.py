#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [0] * n
        inc[0] = 1
        for i in range(1, n):
            inc[i] = inc[i - 1] & (nums[i] > nums[i - 1])

        # empty set.
        ans = 1
        from sortedcontainers import SortedList
        sl = SortedList()
        for i in range(n):
            if inc[i]:
                sl.add(nums[i])
                # prefix set.
                ans += 1

        # if all sorted, then prefix and postfix will be counted twice.
        if inc[-1]:
            ans -= (n + 1)

        flag = 1
        for i in reversed(range(n)):
            flag = flag & (nums[i] < nums[i + 1] if (i + 1) < n else 1)
            if not flag:
                break
            if inc[i]:
                sl.remove(nums[i])
            size = sl.bisect_right(nums[i] - 1) + 1
            # print(sl, nums[i:], size)
            ans += size

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4], 10),
    ([6, 5, 7, 8], 7),
    ([8, 7, 6, 6], 3),
    ([10, 10], 3)
]

aatest_helper.run_test_cases(Solution().incremovableSubarrayCount, cases)

if __name__ == '__main__':
    pass
