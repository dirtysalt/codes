#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        seq = []
        j = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                seq.append((j, i - 1))
                j = i
        seq.append((j, len(nums) - 1))

        for a, b in seq:
            if (b - a + 1) >= 2 * k:
                return True

        for i in range(1, len(seq)):
            a, b = seq[i - 1]
            c, d = seq[i]
            if (b - a + 1) >= k and (d - c + 1) >= k and (b + 1) == c:
                return True
        return False


if __name__ == '__main__':
    pass
