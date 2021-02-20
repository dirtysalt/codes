#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import Counter


class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k < 0: return 0

        counter = Counter()
        for x in nums:
            counter[x] += 1

        ans = 0
        if k == 0:
            for x in counter:
                if counter[x] > 1:
                    ans += 1
            return ans

        for x in counter:
            a = min(1, counter[x - k])
            b = min(1, counter[x + k])
            ans += (a + b)
        ans = ans // 2
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPairs([1, 1, 3, 4, 5], 0))
    print(sol.findPairs([1, 2, 3, 4, 5], 1))
