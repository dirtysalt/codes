#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        ans = 0

        def dist(a, b):
            # print(a, b)
            if a == -1 and b == -1:
                return 0
            elif a == -1:
                return b + 1
            elif b == -1:
                return n - a if a < n and seats[a] == 0 else 0
            else:
                return max(0, (b - a) // 2 + 1)

        prev = -1
        for i in range(n):
            if seats[i] == 1:
                # prev .. i-1
                res = dist(prev, i - 1)
                ans = max(res, ans)
                prev = i + 1
        res = dist(prev, -1)
        ans = max(res, ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
    print(sol.maxDistToClosest([1, 0, 0, 0]))
    print(sol.maxDistToClosest([0, 1]))
