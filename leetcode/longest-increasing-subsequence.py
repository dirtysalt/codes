#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # res[i] 是长度是(i+1)序列的最大值是多少.
        # bisect_left就是在不断地减少这个最小值
        res = []
        for x in nums:
            index = bisect_left(res, x)
            if index == len(res):
                res.append(x)
            else:
                res[index] = x
        # print(res)
        return len(res)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
