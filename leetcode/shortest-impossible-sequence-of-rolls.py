#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        from collections import defaultdict
        from collections import deque
        dd = defaultdict(deque)
        n = len(rolls)
        for i in range(n):
            x = rolls[i]
            dd[x].append(i)

        l = -1
        ans = 1
        while True:
            r = l
            for i in range(1, k + 1):
                dq = dd[i]
                while dq and dq[0] <= l: dq.popleft()
                if not dq: return ans
                r = max(r, dq[0])
            l = r
            ans += 1


true, false, null = True, False, None
cases = [
    ([4, 2, 1, 2, 3, 3, 2, 4, 1], 4, 3),
    ([1, 1, 2, 2], 2, 2),
    ([1, 1, 3, 2, 2, 2, 3, 3], 4, 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().shortestSequence, cases)

if __name__ == '__main__':
    pass
