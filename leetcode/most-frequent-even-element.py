#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter()
        occ = 0
        ans = -1
        for x in nums:
            if x % 2 == 0:
                cnt[x] += 1
                if cnt[x] > occ:
                    occ = cnt[x]
                    ans = x
        if ans == -1: return ans
        for k, v in cnt.items():
            if v == occ and k < ans:
                ans = k
        return ans


if __name__ == '__main__':
    pass
