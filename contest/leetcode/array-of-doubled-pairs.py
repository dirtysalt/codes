#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        from collections import Counter
        counter = Counter()
        for x in A:
            counter[x] += 1

        values = list(counter.keys())
        values.sort(key=lambda x: abs(x))
        for v in values:
            v2 = v * 2
            if counter[v2] >= counter[v]:
                counter[v2] -= counter[v]
            else:
                return False

        return True

# [1,2,4,8] WA.
# class Solution:
#     def canReorderDoubled(self, A: List[int]) -> bool:
#         def cmpfn(x, y):
#             if abs(x) != abs(y):
#                 return abs(x) - abs(y)
#             return x - y
#         import functools
#         A.sort(key=functools.cmp_to_key(cmpfn))
#         # print(A)
#         n2 = len(A) // 2
#         for i in range(n2):
#             if A[i] * 2 != A[i + n2]:
#                 return False
#         return True


import aatest_helper
cases = [
    ([4, -2, 2, -4], True),
    ([1, 2, 4, 16, 8, 4], False),
    ([2, 1, 2, 6], False),
    ([3, 1, 3, 6], False),
    ([1, 2, 4, 8], True)
]

aatest_helper.run_test_cases(Solution().canReorderDoubled, cases)
