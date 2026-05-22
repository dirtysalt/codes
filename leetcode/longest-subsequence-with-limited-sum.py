#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []

        for q in queries:

            t = 0
            sz = len(nums)
            for i in range(len(nums)):
                t += nums[i]
                if t > q:
                    sz = i
                    break

            ans.append(sz)
        return ans


if __name__ == '__main__':
    pass
