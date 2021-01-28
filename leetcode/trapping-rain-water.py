#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 这道题目还可以做成space O(1)的算法，只需要从某个点往两点查找即可
# 不过需要考虑worst case, 就是如果所有height都是相同的，如果这样的话需要做个预处理

# thread 里面的解法更好
# https://leetcode.com/problems/trapping-rain-water/discuss/17527/My-Accepted-Java-Solution
# 我们可以先找到max_index, 然后以这个max_index为分界点，这样就不需要维护left, right数组

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0: return 0
        left = [0] * n
        right = [0] * n

        right[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])

        ans = 0
        for i in range(n):
            ans += min(left[i], right[i]) - height[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.trap([4, 2, 3]))
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]))
