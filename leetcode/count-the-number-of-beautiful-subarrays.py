#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        from collections import Counter
        cnt = Counter()
        cnt[0] += 1
        acc, ans = 0, 0
        for x in nums:
            acc = acc ^ x
            ans += cnt[acc]
            cnt[acc] += 1
        return ans


if __name__ == '__main__':
    pass
