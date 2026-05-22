#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def search(arr):
            now = {(0, 0)}
            dp = []
            for i in range(n):
                update = now.copy()
                for x, c in now:
                    if c >= k: continue
                    z = x | arr[i]
                    update.add((z, c + 1))
                now = update
                dp.append({x for (x, c) in now if c == k})
            return dp

        left = search(nums)
        right = search(nums[::-1])
        ans = 0
        for i in range(0, n - 1):
            j = n - 2 - i
            for z1 in left[i]:
                for z2 in right[j]:
                    ans = max(ans, z1 ^ z2)
        return ans


true, false, null = True, False, None
import aatest_helper
import random

cases = [
    ([2, 6, 7], 1, 5),
    ([4, 2, 5, 6, 7], 2, 2),
    ([11, 71, 47, 70], 1, 105),
    ([random.randint(0, 2 ** 7 - 1) for _ in range(400)], 100, aatest_helper.ANYTHING),
    ([2, 42], 1, 40),
    ([16, 83, 31, 113], 1, 110),
]

aatest_helper.run_test_cases(Solution().maxValue, cases)

if __name__ == '__main__':
    pass
