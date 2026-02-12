#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import Counter
        cnt = Counter()

        j = 0
        ans = 0
        for i in range(len(nums)):
            x = nums[i]
            cnt[x] += 1
            if cnt[x] > k:
                while True:
                    cnt[nums[j]] -= 1
                    j += 1
                    if nums[j - 1] == x:
                        break
            sz = i - j + 1
            ans = max(ans, sz)
        return ans


if __name__ == '__main__':
    pass
