#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        xs = [(v, idx) for (idx, v) in enumerate(nums)]
        xs.sort()
        for i in range(1, len(xs)):
            if xs[i][0] == xs[i - 1][0] and xs[i][1] - xs[i - 1][1] <= k:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print((s.containsNearbyDuplicate([1, 2, 3, 1], 3)))
