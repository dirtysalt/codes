#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        from sortedcontainers import SortedList

        sl = SortedList()
        n = len(nums)
        cnt = [0] * n
        ans = [-1] * n

        for i in range(n):
            x = nums[i]
            sl.add((x, i))

            dels = []
            for y, j in sl:
                if y >= x: break
                cnt[j] += 1
                if cnt[j] == 2:
                    ans[j] = x
                    dels.append((y, j))

            for p in dels:
                sl.remove(p)

        return ans


true, false, null = True, False, None
cases = [
    ([2, 4, 0, 9, 6], [9, 6, 6, -1, -1]),
    ([3, 3], [-1, -1]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().secondGreaterElement, cases)

if __name__ == '__main__':
    pass
