#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        return ans


if __name__ == '__main__':
    pass
