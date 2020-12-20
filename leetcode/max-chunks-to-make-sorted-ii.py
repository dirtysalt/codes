#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        n = len(arr)
        right = [0] * n
        right[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], arr[i])

        ans = 1
        val = arr[0]
        for i in range(n - 1):
            val = max(val, arr[i])
            if val <= right[i + 1]:
                ans += 1
                val = arr[i + 1]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxChunksToSorted([2, 1, 3, 4, 4]))
    print(sol.maxChunksToSorted([5, 4, 3, 2, 1]))
