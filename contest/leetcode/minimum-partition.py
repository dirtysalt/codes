#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums
    """

    def findMin(self, nums):
        # write your code here

        n = len(nums)
        if n == 0: return 0

        # acc = sum(nums)
        # m = acc // 2 + 1
        # dp = [[0] * m for i in range(2)]
        # now = 0
        # dp[0][0] = 1
        # for i in range(n):
        #     val = nums[i]
        #     for j in range(m):
        #         dp[1 - now][j] = 0
        #     for j in range(m):
        #         if not dp[now][j]: continue
        #         if (j + val) < m:
        #             dp[1 - now][j + val] = 1
        #         if (j - val) >= 0:
        #             dp[1 - now][j - val] = 1
        #     now = 1 - now
        # res = acc
        # for j in range(m):
        #     if dp[now][j]:
        #         res = min(res, abs(j - (acc - j)))
        # return res

        st = {0}
        acc = sum(nums)
        upper = acc // 2
        for i in range(n):
            val = nums[i]
            adds = []
            for bal in st:
                if (bal + val) <= upper:
                    adds.append(bal + val)
            st.update(adds)
            # print(st)

        res = acc
        for v in st:
            if abs(v - (acc - v)) < res:
                res = abs(v - (acc - v))
        return res
