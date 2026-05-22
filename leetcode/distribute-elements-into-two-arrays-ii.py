#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]

        from sortedcontainers import SortedList
        sl1, sl2 = SortedList(arr1), SortedList(arr2)

        def g(sl: SortedList, x):
            idx = sl.bisect_left(x + 1)
            return len(sl) - idx

        for i in range(2, len(nums)):
            x = nums[i]
            r0 = g(sl1, x)
            r1 = g(sl2, x)

            # print(r0, r1, arr1,arr2)
            if r0 > r1 or (r0 == r1 and len(arr1) <= len(arr2)):
                arr1.append(x)
                sl1.add(x)
            else:
                arr2.append(x)
                sl2.add(x)

        # print(arr1, arr2)
        return arr1 + arr2


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 1, 3, 3], [2, 3, 1, 3]),
    ([5, 14, 3, 1, 2], [5, 3, 1, 2, 14]),
    ([3, 3, 3, 3], [3, 3, 3, 3])
]

aatest_helper.run_test_cases(Solution().resultArray, cases)

if __name__ == '__main__':
    pass
