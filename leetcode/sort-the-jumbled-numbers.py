#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def convert(x):
            if x == 0:
                return mapping[0]
            res = []
            while x:
                res.append(mapping[x % 10])
                x = x // 10
            ans = 0
            for x in reversed(res):
                ans = ans * 10 + x
            return ans

        tmp = [(convert(nums[i]), i, nums[i]) for i in range(len(nums))]
        # print(tmp)
        tmp.sort()
        ans = [x[2] for x in tmp]
        return ans


true, false, null = True, False, None
cases = [
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().sortJumbled, cases)

if __name__ == '__main__':
    pass
