#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        from collections import defaultdict
        pos = defaultdict(list)
        for i in range(n):
            x = nums[i]
            if len(pos[x]) < 2:
                pos[x].append(i)

        dp = [[1] * 2 for _ in range(n)]
        for i in range(n):
            x = nums[i]

            for k in range(2):
                # dp[i][0] + k ->
                #   dp[j][0] nums[j] = x + k + 1
                #   dp[j][1] nums[j] = x + k
                c = dp[i][k]
                for j in pos[x + k + 1]:
                    dp[j][0] = max(dp[j][0], c + 1)
                for j in pos[x + k]:
                    if j == i: continue
                    dp[j][1] = max(dp[j][1], c + 1)

        ans = 0
        for i in range(n):
            ans = max(ans, max(dp[i]))
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 1, 5, 1, 1], 3),
    ([1, 4, 7, 10], 1),
    ([12, 11, 8, 7, 2, 10, 18, 12], 6),
]

aatest_helper.run_test_cases(Solution().maxSelectedElements, cases)

if __name__ == '__main__':
    pass
