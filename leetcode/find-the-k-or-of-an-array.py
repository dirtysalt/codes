#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = [0] * 32
        for x in nums:
            for i in range(32):
                if x & (1 << i):
                    cnt[i] += 1

        ans = 0
        for i in range(32):
            if cnt[i] >= k:
                ans = ans | (1 << i)
        return ans


if __name__ == '__main__':
    pass
