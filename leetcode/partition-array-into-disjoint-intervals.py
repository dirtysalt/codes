#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def partitionDisjoint(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#
#         n = len(A)
#         right = [0] * n
#         right[-1] = A[-1]
#         for i in range(n - 2, -1, -1):
#             right[i] = min(right[i + 1], A[i])
#
#         value = A[0]
#         for i in range(n - 1):
#             value = max(value, A[i])
#             if value <= right[i + 1]:
#                 return i + 1
#         raise RuntimeError()


"""
这题目如果使用辅助数组很容易想到，但是下面O(1)space不太容易。
i是扫描下表，j是观察后续元素是否都比max(A[..i])要大。这题目是一个贪心算法。
"""


class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        n = len(A)
        value = A[0]
        i, j = 0, 0
        while j < n:
            if value <= A[j]:
                j += 1
            else:
                i += 1
                value = max(value, A[i])
                j = max(i + 1, j)
        return i + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.partitionDisjoint([5, 0, 3, 8, 6]))
    print(sol.partitionDisjoint([1, 1, 1, 0, 6, 12]))
