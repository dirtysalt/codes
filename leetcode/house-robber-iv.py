#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def test(exp, k):
            i = 0
            while i < n:
                if nums[i] <= exp:
                    k -= 1
                    if k == 0:
                        return True
                    i += 2
                else:
                    i += 1
            return False

        s, e = 0, max(nums)
        while s <= e:
            m = (s + e) // 2
            if test(m, k):
                e = m - 1
            else:
                s = m + 1
        ans = s
        return ans


if __name__ == '__main__':
    pass
