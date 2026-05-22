#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = [0] * 101
        for x in nums:
            cnt[x] += 1

        freq = max(cnt)
        ans = 0
        for x in cnt:
            if x == freq:
                ans += freq
        return ans


if __name__ == '__main__':
    pass
