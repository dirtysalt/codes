#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        from collections import Counter
        cnt = Counter([h % 24 for h in hours])
        ans = 0
        for h in hours:
            h = h % 24
            ans += cnt[(24 - h) % 24]
            if h == 0 or h == 12:
                ans -= 1

        return ans // 2


if __name__ == '__main__':
    pass
