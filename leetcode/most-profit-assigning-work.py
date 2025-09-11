#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        xs = list(zip(difficulty, profit))
        xs.sort()

        for i in range(1, len(xs)):
            xs[i] = (xs[i][0], max(xs[i][1], xs[i-1][1]))

        # print(xs)
        worker.sort()
        i = 0
        ans = 0
        for w in worker:
            while i < len(xs) and xs[i][0] <= w:
                i += 1
            if i > 0:
                i = i - 1
                # print(xs[i][1])
                ans += xs[i][1]
        return ans


cases = [
    ([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7], 100),
    ([68, 35, 52, 47, 86], [67, 17, 1, 81, 3], [92, 10, 85, 84, 82], 324),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().maxProfitAssignment, cases)
