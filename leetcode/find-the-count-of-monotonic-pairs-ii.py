#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7

        # x >= z && x >= (A[i] - A[i-1]) + z
        # dp[i][x] = dp[i-1][z] ...

        M = max(nums)
        dp = [[0] * (M+1) for _ in range(n)]
        for i in range(M+1):
            dp[0][i] = 1
        
        for i in range(1, n):
            d = max(nums[i] - nums[i-1], 0)
            acc = 0            
            for x in range(d, nums[i] + 1):
                acc += dp[i-1][x-d]
                dp[i][x] = acc                
        
        ans = sum(dp[-1])
        return ans % MOD
            

true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 3, 2], 4),
    ([5, 5, 5, 5], 126),
]

aatest_helper.run_test_cases(Solution().countOfPairs, cases)

if __name__ == '__main__':
    pass
