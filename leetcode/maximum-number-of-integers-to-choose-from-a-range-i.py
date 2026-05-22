#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        acc = 0
        ans = 0
        for i in range(1, n + 1):
            if i in ban: continue
            acc += i
            if acc > maxSum: break
            ans += 1
        return ans


if __name__ == '__main__':
    pass
