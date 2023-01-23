#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        from collections import Counter
        cnt = Counter()
        for i in range(1, len(nums)):
            x = nums[i - 1] + nums[i]
            cnt[x] += 1
            if cnt[x] == 2:
                return True
        return False
    

if __name__ == '__main__':
    pass
