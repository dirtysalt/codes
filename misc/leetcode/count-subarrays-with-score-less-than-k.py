#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = acc[i] + nums[i]

        ans = 0
        for i in range(n):
            s, e = i, n - 1
            while s <= e:
                m = (s + e) // 2
                score = (m - i + 1) * (acc[m + 1] - acc[i])
                if score < k:
                    s = m + 1
                else:
                    e = m - 1
            # print(i, e - i + 1)
            ans += (e - i + 1)
        return ans


true, false, null = True, False, None
cases = [
    ([2, 1, 4, 3, 5], 10, 6),
    ([1, 1, 1], 5, 5),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countSubarrays, cases)

if __name__ == '__main__':
    pass
