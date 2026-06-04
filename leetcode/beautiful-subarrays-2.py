#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param nums: an integer list
    @param numOdds: an integer
    @return: return the number of beautiful subarrays
    """

    def BeautifulSubarrays(self, nums, numOdds):
        # write your code here
        odd = 0
        i, j = 0, -1

        while i < len(nums):
            odd += nums[i] % 2
            if odd == numOdds:
                break
            i += 1

        ans = 0
        while i < len(nums):
            k = j + 1
            while nums[k] % 2 == 0:
                k += 1

            kk = i + 1
            while kk < len(nums) and nums[kk] % 2 == 0:
                kk += 1

            print(i, kk, j, k)
            ans += (kk - i) * (k - j)
            i = kk
            j = k

        return ans
