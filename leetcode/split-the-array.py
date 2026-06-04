#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        from collections import Counter
        cnt = Counter()
        for x in nums:
            cnt[x] += 1
            if cnt[x] > 2:
                return False
        return True


if __name__ == '__main__':
    pass
