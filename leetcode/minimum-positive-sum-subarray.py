#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = acc[i] + nums[i]

        inf = 1 << 30
        ans = inf
        for i in range(n):
            # print(i, i + l - 1, min(i + r, n))
            for j in range(i + l - 1, min(i + r, n)):
                res = acc[j + 1] - acc[i]
                if res > 0:
                    ans = min(ans, res)
        if ans == inf:
            ans = -1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([-12, 8], 1, 1, 8),
]

aatest_helper.run_test_cases(Solution().minimumSumSubarray, cases)

if __name__ == '__main__':
    pass
