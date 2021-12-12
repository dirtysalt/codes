#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        tmp = nums.copy()
        tmp.sort()
        from collections import Counter
        cnt = Counter(tmp[-k:])

        ans = []
        for x in nums:
            if cnt[x]:
                ans.append(x)
                cnt[x] -= 1
        return ans


if __name__ == '__main__':
    pass
