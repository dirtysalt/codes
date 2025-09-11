#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter
        cnt = Counter()
        for t in tasks:
            cnt[t] += 1
        ans = 0
        for v in cnt.values():
            if v == 1: return -1
            x = v // 3
            x += 1 if v % 3 != 0 else 0
            ans += x
        return ans


if __name__ == '__main__':
    pass
