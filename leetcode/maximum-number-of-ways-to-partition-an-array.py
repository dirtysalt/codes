#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        R = defaultdict(list)
        L = defaultdict(list)

        right = sum(nums)
        left = 0
        ans = 0
        for i in range(len(nums) - 1):
            x = nums[i]
            left += x
            right -= x
            diff = right - left
            R[diff].append(i + 1)
            L[-diff].append(i)
            if diff == 0:
                ans += 1

        for i in range(len(nums)):
            x = nums[i]
            exp = x - k
            res = 0

            arr = R[exp]
            s, e = 0, len(arr) - 1
            # arr[x] <= i
            while s <= e:
                m = (s + e) // 2
                if arr[m] <= i:
                    s = m + 1
                else:
                    e = m - 1
            res += (e + 1)

            arr = L[exp]
            s, e = 0, len(arr) - 1
            # arr[x] >= i
            while s <= e:
                m = (s + e) // 2
                if arr[m] >= i:
                    e = m - 1
                else:
                    s = m + 1
            res += (len(arr) - s)

            # print(i, R[exp], L[exp], res)
            ans = max(ans, res)

        return ans


true, false, null = True, False, None
cases = [
    ([2, -1, 2], 3, 1),
    ([0, 0, 0], 1, 2),
    ([22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14], -33, 4),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30827, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 33),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().waysToPartition, cases)

if __name__ == '__main__':
    pass
