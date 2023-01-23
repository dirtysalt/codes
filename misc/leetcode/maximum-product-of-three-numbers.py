#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pos = [x for x in nums if x >= 0]
        neg = [x for x in nums if x < 0]
        pos.sort()
        neg.sort()

        res = []
        res.append(pos[-3:])
        res.append(pos[-1:] + neg[:2])
        res.append(pos[-2:] + neg[:1])
        res.append(neg[:3])

        ans = None
        for x in res:
            if len(x) == 3:
                val = x[0] * x[1] * x[2]
                if ans is None or val > ans:
                    ans = val
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumProduct([1, 2, 3]))
    print(sol.maximumProduct([1, 2, 3, 4]))
    print(sol.maximumProduct([1, 2, -3, -4]))
    print(sol.maximumProduct([1, -2, -3, -4]))
