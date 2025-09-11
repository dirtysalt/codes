#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = acc[i] + nums[i]

        from collections import Counter
        cc = Counter(nums[:k])
        ss = set(nums[:k])
        tt = sum(nums[:k])
        ans = 0
        if len(ss) == k:
            ans = tt

        for i in range(k, n):
            tt += nums[i] - nums[i - k]
            x = nums[i - k]
            cc[x] -= 1
            if cc[x] == 0:
                ss.remove(x)
            x = nums[i]
            cc[x] += 1
            ss.add(x)
            if len(ss) == k:
                ans = max(ans, tt)
        return ans


if __name__ == '__main__':
    pass
