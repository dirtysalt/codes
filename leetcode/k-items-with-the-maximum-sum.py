#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = [1] * numOnes
        nums += [0] * numZeros
        nums += [-1] * numNegOnes
        ans = sum(nums[:k])
        return ans


if __name__ == '__main__':
    pass
