#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import bisect


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n == 0: return False
        m = len(matrix[0])
        if m == 0: return False
        s, e = 0, n - 1
        while s <= e:
            mid = (s + e) // 2
            if matrix[mid][m - 1] < target:
                s = mid + 1
            else:
                e = mid - 1
        if s >= n: return False

        i = bisect.bisect_left(matrix[s], target)
        if i < m and matrix[s][i] == target:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1], [3], [5]], 4))
