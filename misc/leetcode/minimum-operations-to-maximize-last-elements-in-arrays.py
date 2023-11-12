#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        def search(x, y):
            ans = 0
            for i in range(n - 1):
                if x[i] <= x[-1] and y[i] <= y[-1]:
                    continue
                if y[i] <= x[-1] and x[i] <= y[-1]:
                    ans += 1
                else:
                    return n
            # print(x, y, ans)
            return ans

        A = search(nums1, nums2)
        nums1[-1], nums2[-1] = nums2[-1], nums1[-1]
        B = search(nums1, nums2)
        nums1[-1], nums2[-1] = nums2[-1], nums1[-1]
        ans = min(A, B + 1)
        if ans >= n: ans = -1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums1=[1, 2, 7], nums2=[4, 5, 3], res=1),
    aatest_helper.OrderedDict(nums1=[2, 3, 4, 5, 9], nums2=[8, 8, 4, 4, 4], res=2),
    aatest_helper.OrderedDict(nums1=[1, 5, 4], nums2=[2, 5, 3], res=-1)
]

aatest_helper.run_test_cases(Solution().minOperations, cases)

if __name__ == '__main__':
    pass
