#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def ok(arr, op):
            for i in range(1, len(arr)):
                if op(arr[i], arr[i - 1]):
                    return False
            return True

        inc = lambda x, y: x <= y
        dec = lambda x, y: x >= y

        for sz in reversed(range(1, len(nums) + 1)):
            for i in range(0, len(nums) - sz + 1):
                arr = nums[i:i + sz]
                if ok(arr, inc) or ok(arr, dec):
                    return sz

        return 1


if __name__ == '__main__':
    pass
