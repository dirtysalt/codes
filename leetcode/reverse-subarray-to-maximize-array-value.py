#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

# 对[b, a ... ] 来说，在之前找到一个点，这个点 |nums[p] - b| >= |a - b|
# 这个点会存在两个，然后分别往上下游去逐一检查看交换的效果如何
# 但是这种检查如果从左向右和从右向左。比如 (m+n) > (a+b)，并不意味着m > a
# 但是可以证明 m > a or n > b. 不然逆命题是 m<=a and n<=b, 那么(m+n) <= (a+b).

# class Solution:
#     def maxValueAfterReverse(self, nums: List[int]) -> int:
#
#         def solve(nums):
#             tmp = []
#
#             def upper(a, b):
#                 diff = abs(a - b)
#                 v = b + diff
#                 ans = 0
#                 s, e = 0, len(tmp) - 1
#                 while s <= e:
#                     m = (s + e) // 2
#                     if tmp[m][0] < v:
#                         s = m + 1
#                     else:
#                         e = m - 1
#                 # starts with s
#                 for i in range(s, len(tmp)):
#                     p = tmp[i][1]
#                     x = nums[p]
#                     if (p + 1) == len(nums):
#                         ans = max(ans, abs(x - b) + - abs(a - b))
#                     else:
#                         y = nums[p + 1]
#                         ans = max(ans, abs(x - b) + abs(y - a) - abs(a - b) - abs(x - y))
#                 return ans
#
#             def lower(a, b):
#                 diff = abs(a - b)
#                 v = b - diff
#                 ans = 0
#                 s, e = 0, len(tmp) - 1
#                 while s <= e:
#                     m = (s + e) // 2
#                     if tmp[m][0] > v:
#                         e = m - 1
#                     else:
#                         s = m + 1
#
#                 # starts with e
#                 for i in range(0, e + 1):
#                     p = tmp[i][1]
#                     x = nums[p]
#                     if (p + 1) == len(nums):
#                         ans = max(ans, abs(x - b) + - abs(a - b))
#                     else:
#                         y = nums[p + 1]
#                         ans = max(ans, abs(x - b) + abs(y - a) - abs(a - b) - abs(x - y))
#                 return ans
#
#             tmp.append((nums[-1], len(nums) - 1))
#             ans = 0
#             for i in reversed(range(1, len(nums) - 1)):
#                 a = nums[i]
#                 b = nums[i - 1]
#                 ans = max(ans, upper(a, b))
#                 ans = max(ans, lower(a, b))
#                 # tmp.append((a, i))
#                 # tmp.sort()
#                 # 这里插入节点之后需要排序
#                 import bisect
#                 bisect.insort_right(tmp, (a, i))
#             return ans
#
#         ans = 0
#         ans = max(ans, solve(nums))
#         ans = max(ans, solve(nums[::-1]))
#
#         res = 0
#         for i in range(1, len(nums)):
#             res += abs(nums[i] - nums[i - 1])
#         return ans + res

"""
假设ab...cd, 如果调换的话，那么差值则是|a-c| + |b-d| - |a-b| - |c-d|. 

如何展开这个差值，可以对绝对值做枚举 max of followings
1. a-c+b-d-|a-b|-|c-d| = (a+b-|a-b|) - (c+d+|c-d|)
2. a-c+d-b-|a-b|-|c-d| = (a-b-|a-b|) - (c-d+|c-d|)
3. c-a+b-d-|a-b|-|c-d| = (-a+b-|a-b|) - (-c+d+|c-d|)
4. c-a+d-b-|a-b|-|c-d| = (-a-b-|a-b|) - (-c-d+|c-d|)

这就转换成为一个动态规划问题.

上面是旋转b,c. 没有考虑到A[0]和A[-1]和里面点的旋转，这个需要单独考虑
"""


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        base = 0
        for i in range(n - 1):
            base += abs(nums[i] - nums[i + 1])
        if n <= 3:
            return base

        def left_values(a, b):
            x = abs(a - b)
            return [a + b - x, a - b - x, -a + b - x, -a - b - x]

        def right_values(c, d):
            x = abs(c - d)
            return [c + d + x, c - d + x, -c + d + x, -c - d + x]

        ans = 0
        lv = left_values(nums[0], nums[1])
        for i in range(1, n - 1):
            c, d = nums[i], nums[i + 1]
            rv = right_values(c, d)
            res = [x - y for (x, y) in zip(lv, rv)]
            ans = max(ans, max(res))

            lv2 = left_values(c, d)
            lv = [max(x, y) for (x, y) in zip(lv, lv2)]

        for i in range(1, n - 1):
            ans = max(ans, abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]))
        for i in range(1, n - 1):
            ans = max(ans, abs(nums[i - 1] - nums[-1]) - abs(nums[i - 1] - nums[i]))

        return ans + base


cases = [
    ([2, 3, 1, 5, 4], 10),
    ([2, 4, 9, 24, 2, 1, 10], 68)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxValueAfterReverse, cases)
