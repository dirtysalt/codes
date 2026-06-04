#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


# 我们可以从逆向推导最初序列是什么，假设目标序列是 1,2,3,4,5,6,7
# 6,7 就是 6,7
# 5,6,7 为了保证取5之后是6,7， 那么需要变成7，6，所以就是 5 7 6
# 4,5,6,7 为了保证取4之后是 5 7 6, 那么需要将6放在最前面，所以就是 4 6 5 7
# 3 7 4 6 5
# 2 5 3 7 4 6
# 1 6 2 5 3 7 4
# 假设我们现在要取x, 之后序列是S的话，那么要求序列就是 x + S[-1] + S[:-1].

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        from collections import deque
        dq = deque()

        deck = sorted(deck)
        n = len(deck)

        dq.append(deck[-1])
        for i in reversed(range(n - 1)):
            v = deck[i]
            x = dq.pop()
            dq.appendleft(x)
            dq.appendleft(v)

        ans = list(dq)
        return ans


cases = [
    ([1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 2, 7, 3, 6, 4, 8]),
    ([17, 13, 11, 2, 3, 5, 7], [2, 13, 3, 11, 5, 17, 7])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().deckRevealedIncreasing, cases)
