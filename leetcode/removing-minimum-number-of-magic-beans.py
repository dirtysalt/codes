#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import Counter
from typing import List

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        cnt = Counter(beans)
        dist = list(cnt.items())
        dist.sort(key=lambda x: x[0])

        w = [x[0] for x in dist]
        num = [x[1] for x in dist]

        tt = sum(num) - num[0]
        cost = 0
        for i in range(1, len(dist)):
            cost += (w[i] - w[0]) * num[i]
        ans = cost

        for i in range(1, len(dist)):
            cost += w[i - 1] * num[i - 1]
            cost -= (w[i] - w[i - 1]) * tt
            tt -= num[i]
            ans = min(ans, cost)

        return ans

true, false, null = True, False, None
cases = [
    ([4, 1, 6, 5], 4),
    ([2, 10, 3, 2], 7),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumRemoval, cases)

if __name__ == '__main__':
    pass
