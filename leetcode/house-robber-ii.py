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
        if n <= 2: return max(nums)

        ans = 0

        # choose 0th.
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(n):
            for k in (2, 3):
                v = i + k
                if v < (n - 1):
                    dp[v] = max(dp[v], dp[i] + nums[v])
        ans = max(ans, max(dp))

        # not choose 0th, choose 1th.
        dp = [0] * n
        dp[1] = nums[1]
        for i in range(n):
            for k in (2, 3):
                v = i + k
                if v < n:
                    dp[v] = max(dp[v], dp[i] + nums[v])
        ans = max(ans, max(dp))

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.rob([2, 3, 2]))
    print(s.rob([1, 2, 3, 1]))
