#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        ans = 0
        for x in cnt:
            if cnt[x] == 2:
                ans ^= x
        return ans


if __name__ == '__main__':
    pass
