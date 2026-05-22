#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import random
from typing import List

random.seed(42)


# 这个快速排序调试老费功夫了。一定要把nums[p]和结尾交换，然后在结束时交换回来，不然就会出现数据覆盖的情况

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s, e = 0, len(nums) - 1
        while s < e:
            p = random.randint(s, e)
            pv = nums[p]
            nums[p], nums[e] = nums[e], nums[p]

            # pivot with pv
            i, j = s, e - 1
            while i < j:
                if nums[i] < pv:
                    i += 1
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            assert i == j

            if nums[i] < pv:
                i += 1
            p = i
            nums[p], nums[e] = nums[e], nums[p]

            # adjust s, e, k
            if p == (e - k + 1):
                return pv
            elif p > (e - k + 1):
                k = k - (e - p + 1)
                e = p - 1
            else:
                s = p + 1
        return nums[s]


cases = [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findKthLargest, cases)
