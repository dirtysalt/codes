#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        # 标记为0的操作是谁发起的，最后会做验证
        marker = [-1] * n
        # 标记为0的时间是多少，如果访问相同0之间时间=1则认为是无效
        traces = [0] * n
        trace_id = 0

        for i in range(n):
            # 访问之后就会比较为0.
            if nums[i] == 0:
                continue

            idx = i
            forward = nums[idx] > 0
            initiator = idx

            while nums[idx] != 0:
                t = (idx + nums[idx] + n) % n
                marker[idx] = initiator
                nums[idx] = 0
                traces[idx] = trace_id
                trace_id += 1
                idx = t
                if forward != (nums[idx] > 0):
                    break

            if nums[idx] == 0 and marker[idx] == initiator:
                if (trace_id - traces[idx]) > 1:
                    return True

        return False


import aatest_helper

cases = (
    ([2, -1, 1, 2, 2], True),
    ([-1, 2], False),
    ([-1, -2, -3, -4, -5], False),
    ([-2, 1, -1, -2, -2], False),
    ([1, 1, 2], True)
)

aatest_helper.run_test_cases(Solution().circularArrayLoop, cases)
