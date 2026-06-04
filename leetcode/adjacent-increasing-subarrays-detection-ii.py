#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        seq = []
        j = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                seq.append((j, i - 1))
                j = i
        seq.append((j, len(nums) - 1))

        def ok(k):
            for a, b in seq:
                if (b - a + 1) >= 2 * k:
                    return True

            for i in range(1, len(seq)):
                a, b = seq[i - 1]
                c, d = seq[i]
                if (b - a + 1) >= k and (d - c + 1) >= k and (b + 1) == c:
                    return True
            return False

        s, e = 0, len(nums)
        while s <= e:
            k = (s + e) // 2
            if ok(k):
                s = k + 1
            else:
                e = k - 1
        return e


if __name__ == '__main__':
    pass
