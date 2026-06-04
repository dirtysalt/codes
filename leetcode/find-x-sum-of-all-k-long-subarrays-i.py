#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, X: int) -> List[int]:
        from collections import Counter

        cnt = Counter(nums[:k])

        def xsum():
            items = list(cnt.items())
            items.sort(key=lambda x: (x[1], x[0]))
            return sum([x[0] * x[1] for x in items[-X:]])

        ans = []
        ans.append(xsum())
        for i in range(k, len(nums)):
            cnt[nums[i]] += 1
            cnt[nums[i - k]] -= 1
            ans.append(xsum())
        return ans


if __name__ == '__main__':
    pass
