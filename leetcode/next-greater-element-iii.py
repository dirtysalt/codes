#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
#
# class Solution:
#     def nextGreaterElement(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#
#         if n == 0:
#             return -1
#
#         # search first 1.
#         p1 = 0
#         while p1 < 32:
#             if (n & (1 << p1)):
#                 break
#             p1 += 1
#
#         # search first 0 after that.
#         p2 = p1
#         while p2 < 32:
#             if (n & (1 << p2)):
#                 p2 += 1
#             else:
#                 break
#         if p2 == 32:
#             return -1
#
#         # set p2 to 1, and p2 - 1 to 0.
#
#         res = n | (1 << p2)
#         res = res & (~(1 << (p2 - 1)))
#         return res

class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """

        past = []
        max_past = 0
        ok = False
        while n:
            val = n % 10
            n = n // 10
            if val >= max_past:
                past.append(val)
                max_past = val
            else:
                ok = True
                break
        if not ok:
            return -1

        swap_value = 10
        swap_idx = -1
        for i in range(0, len(past)):
            if past[i] > val:
                if past[i] < swap_value:
                    swap_value = past[i]
                    swap_idx = i

        INT_MAX = (1 << 31) - 1
        val, past[swap_idx] = past[swap_idx], val
        past.sort()
        res = n * 10 + val
        for v in past:
            res = res * 10 + v
            if res > INT_MAX:
                return -1
        return res
