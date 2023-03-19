#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        from collections import Counter
        cnt = Counter()
        for x in nums:
            cnt[x % value] += 1

        ans = 0
        exp = 0
        while True:
            if cnt[exp] == 0: break
            cnt[exp] -= 1
            exp = (exp + 1) % value
            ans += 1
        return ans


if __name__ == '__main__':
    pass
