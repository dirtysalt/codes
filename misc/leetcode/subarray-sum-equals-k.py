#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import Counter


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        counter = Counter()
        counter[0] = 1
        ans = 0
        acc = 0
        for x in nums:
            acc += x
            exp = acc - k
            ans += counter[exp]
            counter[acc] += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))
