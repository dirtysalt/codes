#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = [0]
        n = len(nums)
        M = 0
        for i in range(n):
            M = max(M, nums[i])
            ans.append(ans[-1] + M + nums[i])
        return ans[1:]


if __name__ == '__main__':
    pass
