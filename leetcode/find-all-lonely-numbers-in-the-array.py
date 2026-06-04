#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        ans = []
        for x in nums:
            if cnt[x] > 1 or cnt[x - 1] or cnt[x + 1]:
                continue
            ans.append(x)
        return ans


if __name__ == '__main__':
    pass
