#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isOK(arr):
            if len(arr) < 2: return False
            d = arr[1] - arr[0]
            for i in range(1, len(arr)):
                if (arr[i] - arr[i - 1]) != d:
                    return False
            return True

        ans = []
        for i, j in zip(l, r):
            arr = sorted(nums[i: j + 1])
            ok = isOK(arr)
            # print(arr, ok)
            ans.append(ok)
        return ans
