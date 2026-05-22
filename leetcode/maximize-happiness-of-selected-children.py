#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        h = happiness
        h.sort(reverse=True)
        t, ans = 0, 0
        for i in range(k):
            ans += max(h[i] - t, 0)
            t += 1
        return ans


if __name__ == '__main__':
    pass
