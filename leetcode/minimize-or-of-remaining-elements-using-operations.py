#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        mask = 0

        bit_count = 0
        M = max(nums)
        while (1 << bit_count) <= M:
            bit_count += 1

        for test_b in reversed(range(0, bit_count)):
            mask |= (1 << test_b)
            cnt = 0
            and_res = -1
            for x in nums:
                and_res = and_res & (x & mask)
                if and_res:
                    cnt += 1
                else:
                    and_res = -1
            if cnt > k:
                ans |= (1 << test_b)
                mask &= ~(1 << test_b)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[3, 5, 3, 2, 7], k=2, res=3),
    aatest_helper.OrderedDict(nums=[7, 3, 15, 14, 2, 8], k=4, res=2),
    aatest_helper.OrderedDict(nums=[10, 7, 10, 3, 9, 14, 9, 4], k=1, res=15),
]

aatest_helper.run_test_cases(Solution().minOrAfterOperations, cases)

if __name__ == '__main__':
    pass
