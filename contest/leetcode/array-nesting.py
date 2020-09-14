#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0: return 0

        ans = 0
        visited = [0] * n
        for i in range(n):
            res = 0
            x = i
            while not visited[x]:
                visited[x] = 1
                res += 1
                x = nums[x]
            ans = max(ans, res)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.arrayNesting([5, 4, 0, 3, 1, 6, 2]))
