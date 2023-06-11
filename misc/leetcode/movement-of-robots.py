#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        pos = []
        for x, p in zip(nums, s):
            if p == 'R':
                x += d
            else:
                x -= d
            pos.append(x)

        pos.sort(reverse=True)
        ans = 0
        MOD = 10 ** 9 + 7

        acc = 0
        # print(pos)
        for i in range(1, len(pos)):
            d = pos[i - 1] - pos[i]
            acc += i * d
            ans += acc
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([-2, 0, 2], "RLL", 3, 8),
    ([1, 0], "RL", 2, 5),
    ([-10, -13, 10, 14, 11], "LRLLR", 2, 146)
]

aatest_helper.run_test_cases(Solution().sumDistance, cases)

if __name__ == '__main__':
    pass
