#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        n = len(A)
        lo = 0
        for i in range(n):
            if A[i] % 2 == 0:
                A[i], A[lo] = A[lo], A[i]
                lo += 1
        return A


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortArrayByParity([1, 2, 3, 4]))
    print(sol.sortArrayByParity([4, 2, 3, 4]))
