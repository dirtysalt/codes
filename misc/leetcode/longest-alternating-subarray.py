#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        def search(xs):
            n = len(xs)
            diff = 1
            sz = 1
            for i in range(1, n):
                if xs[i] - xs[i - 1] == diff:
                    sz += 1
                    diff = -diff
                else:
                    break
            return sz

        ans = 0
        for i in range(len(nums)):
            c = search(nums[i:])
            ans = max(ans, c)
        if ans == 1:
            ans = -1
        return ans


if __name__ == '__main__':
    pass
