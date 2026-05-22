#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        events = []
        for s, e in flowers:
            events.append((s, 0, 0))
            events.append((e, 2, 0))
        for i in range(len(persons)):
            t = persons[i]
            events.append((t, 1, i))
        events.sort()

        ans = [0] * len(persons)
        cnt = 0
        for _, t, i in events:
            if t == 0:
                cnt += 1
            elif t == 1:
                ans[i] = cnt
            else:
                cnt -= 1
        return ans

true, false, null = True, False, None
cases = [
    ([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11], [1, 2, 2, 2]),
    ([[1, 10], [3, 3]], [3, 3, 2], [2, 2, 1]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().fullBloomFlowers, cases)

if __name__ == '__main__':
    pass
