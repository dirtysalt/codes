#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        from collections import Counter
        n = len(nums)
        cnt = Counter()
        for xs in nums:
            for x in xs:
                cnt[x] += 1

        ans = []
        for x in cnt:
            if cnt[x] == n:
                ans.append(x)
        ans.sort()
        return ans

if __name__ == '__main__':
    pass
