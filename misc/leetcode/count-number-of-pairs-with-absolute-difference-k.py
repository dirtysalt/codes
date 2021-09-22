#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        from collections import Counter
        cnt = Counter(nums)

        ans = 0
        for x in nums:
            exp = x + k
            ans += cnt[exp]

        return ans


if __name__ == '__main__':
    pass
