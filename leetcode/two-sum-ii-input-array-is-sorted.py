#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            val = numbers[i] + numbers[j]
            if val == target:
                return i + 1, j + 1
            elif val < target:
                i += 1
            else:
                j -= 1
        raise RuntimeError()
