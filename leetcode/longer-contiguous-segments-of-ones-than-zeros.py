#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        cnt = [0] * 2
        ans = [0] * 2
        l = int(s[0])
        for c in s:
            x = int(c)
            if x != l:
                cnt[l] = 0
            cnt[x] += 1
            ans[x] = max(ans[x], cnt[x])
            l = x

        if ans[1] > ans[0]:
            return True
        return False


if __name__ == '__main__':
    pass
