#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect


class RLEIterator:
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.nums = []
        self.values = []
        for i in range(0, len(A), 2):
            self.nums.append(A[i])
            self.values.append(A[i + 1])
        self.off = 0
        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i - 1]
        self.lo = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.off > self.nums[-1]:
            return -1
        self.off += n
        if self.off > self.nums[-1]:
            return -1
        idx = bisect.bisect_left(self.nums, self.off, self.lo)
        ans = self.values[idx]
        self.lo = idx
        return ans
