#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []

        for i in range(len(nums)):
            ok = False
            for j in range(len(nums)):
                if abs(i - j) <= k and nums[j] == key:
                    ok = True
                    break
            if ok:
                ans.append(i)
        return ans

if __name__ == '__main__':
    pass
