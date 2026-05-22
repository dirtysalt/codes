#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        st = [(0, 0)]
        n = len(s)
        if s[-1] != '0': return False

        ans = False

        for i in range(n):
            if s[i] != '0':
                continue
            ok = False

            for j in range(len(st)):
                x, y = st[j]
                if x <= i <= y:
                    # truncate to j
                    st = st[j:]
                    ok = True
                    break

            ans = ok
            if not ok: continue
            x, y = i + minJump, i + maxJump
            while st:
                a, b = st[-1]
                if a <= x <= b:
                    x, y = a, y
                st.pop()

            st.append((x, y))

        return ans


true, false, null = True, False, None
cases = [
    ("011010", 2, 3, true),
    ("01101110", 2, 3, false),
    ("00111010", 3, 5, false),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().canReach, cases)

if __name__ == '__main__':
    pass
