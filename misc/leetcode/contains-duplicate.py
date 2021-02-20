#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
