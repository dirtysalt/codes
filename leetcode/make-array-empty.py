#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        sl = SortedList()
        n = len(nums)
        pv = [(x, i) for i, x in enumerate(nums)]
        pv.sort()

        now = 0
        ans = 0

        def deleted_number(a, b):
            A = sl.bisect_left(a)
            B = sl.bisect_right(b) - 1
            return B - A + 1

        for (x, i) in pv:
            # move now to i
            if i >= now:
                # check how many elements been remove between [now, i]
                op = (i - now + 1) - deleted_number(now, i)
                ans += op
            else:
                # check how many lements in [0, i], [now, n-1]
                op = (n - now + i + 1) - deleted_number(now, n - 1) - deleted_number(0, i - 1)
                ans += op

            # print('delete ', x, 'with op = ', op)
            sl.add(i)
            now = (i + 1) % n
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 4, -1], 5),
    ([1, 2, 4, 3], 5),
    ([1, 2, 3], 3),
    ([6, 18, 13, -15], 8),
]

# cases += [(list(range(1, 100000)), 99999)]

aatest_helper.run_test_cases(Solution().countOperationsToEmptyArray, cases)

if __name__ == '__main__':
    pass
