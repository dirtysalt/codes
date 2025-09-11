#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        from collections import Counter
        cnt = [Counter() for _ in range(n)]
        for x, y in pick:
            cnt[x][y] += 1

        ans = 0
        for i in range(n):
            c = cnt[i]
            for _, f in c.items():
                if f > i:
                    ans += 1
                    break
        return ans


if __name__ == '__main__':
    pass
