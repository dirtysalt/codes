#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        left[0] = 1
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1

        right[-1] = 1
        for i in reversed(range(n - 1)):
            if nums[i] <= nums[i + 1]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1

        ans = []
        for i in range(k, n - k):
            if left[i - 1] >= k and right[i + 1] >= k:
                ans.append(i)
        return ans


if __name__ == '__main__':
    pass
