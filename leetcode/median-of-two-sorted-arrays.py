#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 0:
            b = self.Xth(nums1, nums2, (m + n) // 2)
            a = self.Xth(nums1, nums2, (m + n) // 2 + 1)
            return (a + b) * 0.5
        else:
            return self.Xth(nums1, nums2, (m + n) // 2 + 1)

    def Xth(self, nums1, nums2, x):
        v = self.xth(nums1, nums2, x)
        if v: return v
        return self.xth(nums2, nums1, x)

    def xth(self, nums1, nums2, x):
        s, e = 0, len(nums1) - 1
        s2, e2 = 0, len(nums2) - 1
        while s <= e:
            m = (s + e) // 2
            a = nums1[m]
            left = bisect.bisect_left(nums2, a, s2, e2 + 1)
            right = bisect.bisect_right(nums2, a, s2, e2 + 1)
            if m + left + 1 <= x <= m + right + 1:
                return a
            elif (m + left + 1) < x:
                s = m + 1
                s2 = max(s2, right)
            else:
                e = m - 1
                e2 = min(e2, left)
        return None


if __name__ == '__main__':
    s = Solution()
    # print(s.xth([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5))
    # print(s.xth([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5))
    # print(s.xth([2, 4, 6, 8, 10], [1, 3, 5, 7, 9], 4))
    # print(s.xth([2, 4, 6, 8, 10], [1, 3, 5, 7, 9], 5))
    print(s.findMedianSortedArrays([1, 3], [2]))
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
    print(s.findMedianSortedArrays([1], [1]))
    print(s.findMedianSortedArrays([1, 2, 3, 4, 5, 6], []))
