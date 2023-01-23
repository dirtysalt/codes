#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 通过特定的方法来构造这个数组

class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        ans = []
        x = 1
        d = 0
        step = k
        ans.append(x)
        while step >= 1:
            if d == 0:
                x = x + step
            else:
                x = x - step
            ans.append(x)
            step -= 1
            d = 1 - d

        for x in range(2 + k, n + 1):
            ans.append(x)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.constructArray(10, 4))
    print(sol.constructArray(10, 5))
