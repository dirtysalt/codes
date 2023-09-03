#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        from collections import Counter
        cnt = Counter()
        tt = 0
        for i in range(k):
            x = nums[i]
            cnt[x] += 1
            tt += x

        ans = 0
        if len(cnt) >= m:
            ans = tt

        for i in range(k, len(nums)):
            x = nums[i]
            cnt[x] += 1
            tt += x
            x = nums[i - k]
            cnt[x] -= 1
            if cnt[x] == 0:
                del cnt[x]
            tt -= x

            if len(cnt) >= m:
                ans = max(ans, tt)
        return ans


if __name__ == '__main__':
    pass
