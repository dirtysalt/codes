#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            res.extend([x + [n] for x in res])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
