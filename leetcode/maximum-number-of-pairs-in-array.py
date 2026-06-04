#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        from collections import Counter
        cnt = Counter()

        for x in nums:
            cnt[x] += 1

        a, b = 0, 0
        for k, v in cnt.items():
            a += v // 2
            b += v % 2
        return a, b


if __name__ == '__main__':
    pass
