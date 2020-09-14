#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0

        dp = nums.copy()
        for i in range(n):
            for k in (2, 3):
                v = i + k
                if v < n:
                    dp[v] = max(dp[v], dp[i] + nums[v])
        ans = max(dp[-2:])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2, 7, 9, 3, 1]))
    print(s.rob([2, 1, 1, 2]))
