#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        pos = [-1] * n

        j = 0
        pos[0] = 0
        for i in range(1, n):
            if nums[i] % 2 == nums[i - 1] % 2:
                pos[i] = i
                j = i
            else:
                pos[i] = j

        ans = []
        for f, t in queries:
            ans.append(pos[f] == pos[t])
        return ans


if __name__ == '__main__':
    pass
