#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


def gen_options(N):
    def reverse(x):
        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x = x // 10
        return ans

    for x in range(10):
        yield x

    for sz in range(2, N):
        mid = sz // 2
        lower, upper = 10 ** (mid - 1), 10 ** mid
        if sz % 2 == 1:
            for head in range(lower, upper):
                tail = reverse(head)
                for x in range(10):
                    yield (head * 10 + x) * upper + tail
        else:
            for head in range(lower, upper):
                tail = reverse(head)
                yield head * upper + tail


OPTIONS = list(gen_options(10))


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        options = OPTIONS

        def cap_options():
            s, e = 0, len(options) - 1
            while s <= e:
                m = (s + e) // 2
                if options[m] > nums[0]:
                    e = m - 1
                else:
                    s = m + 1
            lower = e

            s, e = 0, len(options) - 1
            while s <= e:
                m = (s + e) // 2
                if options[m] < nums[-1]:
                    s = m + 1
                else:
                    e = m - 1
            upper = s
            return options[lower: upper + 1]

        capped_options = cap_options()
        acc = ans = sum(nums)

        left, last = 0, 0
        i = 0
        for x in capped_options:
            a, b = 0, 0
            acc += left * (x - last)
            while i < len(nums) and nums[i] <= x:
                left += 1
                a += abs(nums[i] - last)
                b += abs(nums[i] - x)
                i += 1
            acc -= a
            acc += b
            right = len(nums) - left
            acc -= right * (x - last)
            last = x

            ans = min(ans, acc)
            # print(x, acc)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4, 5], 6),
    ([10, 12, 13, 14, 15], 11),
    ([22, 33, 22, 33, 22], 22),
    ([9675, 7877, 7114, 4142, 8102, 1599, 5161, 8478, 8627, 7590, 8215, 3472, 3284, 4427, 3307, 3879, 1447, 9763, 3941,
      8569, 9518, 7489, 7996, 5501, 7543, 4123], 58045)
]

aatest_helper.run_test_cases(Solution().minimumCost, cases)
