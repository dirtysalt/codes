#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        def ok(value):
            j = 0
            acc = 0
            dup = set()
            for i in range(len(nums)):
                x = nums[i]
                if x in dup:
                    while nums[j] != x:
                        dup.remove(nums[j])
                        acc -= nums[j]
                        j += 1
                    j += 1
                    acc -= x

                dup.add(x)
                acc += x
                if acc >= value:
                    return True
            return False

        s, e = 0, sum(nums)
        ans = 0
        while s <= e:
            m = (s + e) // 2
            if ok(m):
                ans = m
                s = m + 1
            else:
                e = m - 1
        return ans
