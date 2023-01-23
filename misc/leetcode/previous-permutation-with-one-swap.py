#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# note(yan): 我看了discussion里面的讨论，有用C++ map upper_bound来解决的
# 说实话这就节省了很多代码。对于这类非计数问题来说，归并排序虽然和map upper_bound原理差不多
# 但是代码量就增加了不少。题目还有O(n)的解法，看来这问题我想复杂了.

# 找到ith点，其中A[i] > min(A[i+1...]). 说明A[i+1..]有一个可以交换的元素j.然后从这里向后遍历即可
# 其中j是应该是最大的值但是A[i] > A[j]并且相同情况下尽可能靠左，
#
# class Solution:
#     def prevPermOpt1(self, A: List[int]) -> List[int]:
#         n = len(A)
#         self.ans = None
#         self.ok = False
#
#         def merge(a, b):
#             i, j = len(a) - 1, len(b) - 1
#             tmp = []
#             while i >= 0 and j >= 0:
#                 if a[i][0] <= b[j][0]:
#                     tmp.append(b[j])
#                     j -= 1
#                 else:
#                     tmp.append(a[i])
#                     x0, y0 = a[i][1], b[j][1]
#                     if self.ans is None:
#                         self.ans = (x0, y0)
#                     else:
#                         (x, y) = self.ans
#                         if x == x0:
#                             if A[y] == A[y0]:
#                                 self.ans = (x, min(y, y0))
#                             elif A[y] > A[y0]:
#                                 self.ans = (x, y)
#                             else:
#                                 self.ans = (x, y0)
#                         elif x > x0:
#                             self.ans = (x, y)
#                         else:
#                             self.ans = (x0, y0)
#                     i -= 1
#             tmp.extend(reversed(a[:i + 1]))
#             tmp.extend(reversed(b[:j + 1]))
#             tmp = tmp[::-1]
#             return tmp
#
#         def msort(a, s, e):
#             if len(a) == 1:
#                 return a
#             m = len(a) // 2
#             y = msort(a[m:], s + m, e)
#
#             # 这里可以快速返回，如果在最右侧发现了可以交换的pair之后
#             if (e + 1) == len(A) and self.ans:
#                 self.ok = True
#                 return
#
#             x = msort(a[:m], s, s + m - 1)
#
#             if self.ok:
#                 return
#             res = merge(x, y)
#             return res
#
#         arr = [(A[i], i) for i in range(n)]
#         msort(arr, 0, len(arr) - 1)
#         # print(self.ans)
#
#         if self.ans:
#             A = A[:]
#             (i, j) = self.ans
#             A[i], A[j] = A[j], A[i]
#         # print(A)
#         return A

class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)

        # 然后其实下面这个写法可以缩写为
        idx = None
        # p = 10000 + 1
        # for i in reversed(range(n - 1)):
        #     p = min(p, A[i + 1])
        #     if A[i] > p:
        #         idx = i
        #         break

        for i in reversed(range(n - 1)):
            if A[i] > A[i + 1]:
                idx = i
                break

        if idx is None:
            return A

        _max = idx + 1
        for j in range(idx + 1, n):
            if A[_max] < A[j] < A[i]:
                _max = j

        a = A[:]
        a[_max], a[idx] = a[idx], a[_max]
        return a


import aatest_helper

cases = [
    ([1, 9, 4, 6, 7], [1, 7, 4, 6, 9]),
    ([3, 1, 1, 3], [1, 3, 1, 3]),
    ([3, 2, 1], [3, 1, 2]),
    ([1, 1, 5], [1, 1, 5]),
    ([63, 23, 26, 37], [37, 23, 26, 63]),
]

aatest_helper.run_test_cases(Solution().prevPermOpt1, cases)
