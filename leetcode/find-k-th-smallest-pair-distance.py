#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect


class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n = len(nums)
        nums.sort()

        def find_kth(d):
            ans = 0
            for i in range(n):
                j = bisect.bisect_right(nums, nums[i] + d, i + 1)
                ans += j - i - 1
            return ans

        s, e = 0, nums[-1] - nums[0]
        while s < e:
            m = (s + e) // 2
            k2 = find_kth(m)
            if k2 < k:
                s = m + 1
            else:
                e = m
        return e


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestDistancePair([1, 3, 1], 1))
    print(sol.smallestDistancePair([1, 3, 1], 2))
    print(sol.smallestDistancePair([1, 3, 1], 3))
    print(sol.smallestDistancePair([1, 3, 1], 4))
