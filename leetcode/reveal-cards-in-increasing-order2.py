#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        ans = [-1] * n
        deck.sort(reverse=True)

        from collections import deque
        dq = deque()
        for i in range(n):
            dq.append(i)

        while dq:
            i = dq.popleft()
            ans[i] = deck.pop()
            if dq:
                i = dq.popleft()
                dq.append(i)
        return ans


cases = [
    ([1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 2, 7, 3, 6, 4, 8]),
    ([17, 13, 11, 2, 3, 5, 7], [2, 13, 3, 11, 5, 17, 7])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().deckRevealedIncreasing, cases)
