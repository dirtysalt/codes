#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = []
        n = len(obstacles)
        dp = []

        for i in range(n):
            h = obstacles[i]

            s, e = 0, len(dp) - 1
            while s <= e:
                m = (s + e) // 2
                if dp[m] > h:
                    e = m - 1
                else:
                    s = m + 1

            ans.append(e + 1)

            if (e + 1) < len(dp):
                dp[e + 1] = min(dp[e + 1], h)
            else:
                dp.append(h)

        for i in range(n):
            ans[i] += 1
        return ans


true, false, null = True, False, None
cases = [
    ([1, 2, 3, 2], [1, 2, 3, 3]),
    ([2, 2, 1], [1, 2, 1]),
    ([3, 1, 5, 6, 4, 2], [1, 1, 2, 3, 2, 2])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestObstacleCourseAtEachPosition, cases)

if __name__ == '__main__':
    pass
