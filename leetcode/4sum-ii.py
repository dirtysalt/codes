#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
#         from collections import Counter
#
#         def make_cross(a, b):
#             c = Counter()
#             for x in a:
#                 for y in b:
#                     c[x + y] += 1
#             return c
#
#         ab = make_cross(A, B)
#         cd = make_cross(C, D)
#         ans = 0
#         for k, v in cd.items():
#             ans += v * ab[-k]
#         return ans

# class Solution:
#     def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
#         from collections import Counter
#
#         def make_cross(a, b):
#             c = Counter()
#             for x in a:
#                 for y in b:
#                     c[x + y] += 1
#             return c
#
#         ab = make_cross(A, B)
#         ans = 0
#         for x in C:
#             for y in D:
#                 ans += ab[-x - y]
#         return ans

# 从提交上来看，放在一行的写法可以节省接近100ms. 此外我们不用构造两个counter.
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import Counter
        ab = Counter((x + y for x in A for y in B))
        ans = sum(ab[-x - y] for x in C for y in D)
        return ans


cases = [
    ([1, 2], [-2, -1], [-1, 2], [0, 2], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().fourSumCount, cases)
