#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        inf = 1 << 30

        import functools
        @functools.lru_cache(maxsize=None)
        def search(i, k):
            if i == len(nums):
                return 0
            if k == -1:
                return inf

            choose = nums[i]
            acc = 0
            ans = inf
            for j in range(i, len(nums)):
                if nums[j] > choose:
                    delta = nums[j] - choose
                    acc += delta * (j - i)
                    choose += delta
                acc += choose - nums[j]
                res = acc + search(j + 1, k - 1)
                ans = min(ans, res)
            return ans

        ans = search(0, k)
        return ans


true, false, null = True, False, None
cases = [
    ([10, 20], 0, 10),
    ([10, 20, 30], 1, 10),
    ([10, 20, 15, 30, 20], 2, 15),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minSpaceWastedKResizing, cases)

if __name__ == '__main__':
    pass
