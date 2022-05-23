#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        values = {}
        while nums2:
            x = nums2.pop()
            while st and st[-1] < x:
                st.pop()
            y = st[-1] if st else -1
            values[x] = y
            st.append(x)

        ans = []
        for x in nums1:
            ans.append(values[x])

        return ans


if __name__ == '__main__':
    pass
