#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last = {}

        inf = 1 << 30
        ans = inf
        for i in range(len(cards)):
            c = cards[i]
            if c not in last:
                last[c] = i
            else:
                dist = i - last[c] + 1
                ans = min(dist, ans)
                last[c] = i

        if ans == inf:
            ans = -1
        return ans


if __name__ == '__main__':
    pass
