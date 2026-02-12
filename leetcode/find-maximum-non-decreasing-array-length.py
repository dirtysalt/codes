#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + nums[i]
        f = [0] * (n + 1)
        last = [0] * (n + 1)
        from collections import deque
        q = deque([0])
        for i in range(1, n + 1):
            while len(q) > 1 and s[q[1]] + last[q[1]] <= s[i]:
                q.popleft()

            f[i] = f[q[0]] + 1
            last[i] = s[i] - s[q[0]]

            while q and s[q[-1]] + last[q[-1]] >= s[i] + last[i]:
                q.pop()
            q.append(i)
        return f[-1]


true, false, null = True, False, None
import aatest_helper

cases = [
    ([5, 2, 2], 1),
    ([1, 2, 3, 4], 4),
    ([4, 3, 2, 6], 3),
    ([272, 482, 115, 925, 983], 4),
    ([418, 421, 309, 442, 80, 305, 166, 884, 791, 353], 5),
]

aatest_helper.run_test_cases(Solution().findMaximumLength, cases)

if __name__ == '__main__':
    pass
