#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        from collections import deque
        dq = deque()
        for i in range(len(tickets)):
            dq.append((tickets[i], i))

        ans = 0
        while True:
            ans += 1
            (t, idx) = dq.popleft()
            t -= 1
            if t > 0:
                dq.append((t, idx))
            elif idx == k:
                break

        return ans

if __name__ == '__main__':
    pass
