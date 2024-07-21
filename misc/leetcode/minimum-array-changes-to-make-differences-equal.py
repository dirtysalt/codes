#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        from collections import Counter
        cnt = Counter()
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if j <= i: break
            d = abs(nums[i] - nums[j])
            cnt[d] += 1

        delta = {}
        for d, c in cnt.items():
            if c not in delta:
                delta[c] = d
            else:
                delta[c] = min(delta[c], d)

        def test(X):
            r = 0
            for i in range(len(nums)):
                j = len(nums) - 1 - i
                if j <= i: break
                a, b = nums[i], nums[j]
                if a > b: a, b = b, a
                if b - a == X: continue
                # a < b
                if a + X <= k or b - X >= 0:
                    r += 1
                else:
                    r += 2
            return r

        ans = 1 << 30
        for c, d in delta.items():
            r = test(d)
            ans = min(ans, r)
        return ans


if __name__ == '__main__':
    pass
