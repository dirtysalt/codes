#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.nums = nums
        self.B = [0] * (n + 1)
        for (idx, value) in enumerate(nums):
            self._update(idx, value)

    def _update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        index = i + 1
        while index < len(self.B):
            self.B[index] += val
            index += index & (-index)

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        self._update(i, diff)

    def myRange(self, i):
        index = i + 1
        res = 0
        while index:
            res += self.B[index]
            index -= index & (-index)
        return res

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        a = self.myRange(j)
        b = self.myRange(i - 1)
        return a - b


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

if __name__ == '__main__':
    obj = NumArray([1, 3, 5])
    print(obj.sumRange(0, 2))
    obj.update(1, 2)
    print(obj.sumRange(0, 2))
