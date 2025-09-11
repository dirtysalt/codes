#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        from collections import Counter
        cnt = Counter()
        for x in arr:
            cnt[x % k] += 1
        # print(cnt)
        for x in range(k):
            y = (k - x) % k
            if x == y:
                if cnt[x] % 2:
                    return False
            else:
                if cnt[x] != cnt[y]:
                    return False
        return True


cases = [
    ([-1, -1, -1, -1, 2, 2, -2, -2], 3, False),
    ([1, 2, 3, 4, 5, 6], 7, True),
    ([0, 0, 0, 1, 1, 1], 2, False),
    ([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5, True),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().canArrange, cases)
