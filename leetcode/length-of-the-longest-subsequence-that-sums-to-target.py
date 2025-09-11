#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


# class Solution:
#     def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
#
#         @functools.cache
#         def search(i, t):
#             if t == 0: return 0
#             if t < 0: return -1
#             if i == len(nums): return -1
#             a = search(i + 1, t)
#             b = search(i + 1, t - nums[i])
#             if b != -1:
#                 b += 1
#             return max(a, b)
#
#         ans = search(0, target)
#         return ans

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-1] * (target + 1) for _ in range(2)]
        dp[0][0] = 0

        now = 0
        for i in range(n):
            for t in range(0, target + 1):
                if dp[now][t] == -1: continue
                dp[1 - now][t] = max(dp[1 - now][t], dp[now][t])
                t2 = t + nums[i]
                if t2 <= target:
                    dp[1 - now][t2] = max(dp[1 - now][t2], dp[now][t] + 1)
            now = 1 - now

        return dp[now][target]


if __name__ == '__main__':
    pass
