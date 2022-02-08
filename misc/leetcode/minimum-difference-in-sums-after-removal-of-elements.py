#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        import heapq

        def process_left(nums):
            n = len(nums) // 3
            hp = [-x for x in nums[:n]]
            heapq.heapify(hp)

            tt = sum(nums[:n])
            left = [tt]
            for i in range(n, 2 * n):
                x = nums[i]
                heapq.heappush(hp, -x)
                y = -heapq.heappop(hp)
                tt = tt - y + x
                left.append(min(left[-1], tt))

            return left

        def process_right(nums):
            nums = nums[::-1]
            n = len(nums) // 3
            hp = [x for x in nums[:n]]
            heapq.heapify(hp)

            tt = sum(nums[:n])
            right = [tt]
            for i in range(n, 2 * n):
                x = nums[i]
                heapq.heappush(hp, x)
                y = heapq.heappop(hp)
                tt = tt - y + x
                right.append(max(right[-1], tt))

            return right[::-1]

        left = process_left(nums)
        right = process_right(nums)
        print(left, right)
        ans = 1 << 63
        for i in range(len(left)):
            res = left[i] - right[i]
            ans = min(ans, res)
        return ans


true, false, null = True, False, None
cases = [
    ([3, 1, 2], -1),
    ([7, 9, 5, 8, 1, 3], 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumDifference, cases)

if __name__ == '__main__':
    pass
