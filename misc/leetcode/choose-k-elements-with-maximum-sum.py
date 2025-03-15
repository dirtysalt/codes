#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


from typing import List


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        idx = list(range(n))
        idx.sort(key=lambda x: nums1[x])
        # print(idx)

        ans = [0] * n
        from sortedcontainers import SortedList
        sl = SortedList()
        total = 0
        j = 0

        for i in range(n):
            while nums1[idx[j]] < nums1[idx[i]]:
                sl.add(nums2[idx[j]])
                total += nums2[idx[j]]
                j += 1
            while len(sl) > k:
                total -= sl[0]
                sl.pop(0)

            ans[idx[i]] = total
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([4, 2, 1, 5, 3], [10, 20, 30, 40, 50], 2, [80, 30, 0, 80, 50]),
    ([2, 2, 2, 2], [3, 1, 2, 3], 1, [0, 0, 0, 0])
]

aatest_helper.run_test_cases(Solution().findMaxSum, cases)

if __name__ == '__main__':
    pass
