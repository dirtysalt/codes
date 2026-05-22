#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        dp = [0] * (1 + target)
        dp[0] = 1
        for i in range(target):
            for n in nums:
                if i + n > target:
                    continue
                dp[i + n] += dp[i]
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4([1, 2, 3], 4))
