#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        if not numRows: return ans
        ans.append([1])

        for _ in range(numRows - 1):
            r = ans[-1]
            r2 = [0] * (len(r) + 1)
            r2[0] = r[0]
            r2[-1] = r[-1]
            for i in range(1, len(r2) - 1):
                r2[i] = r[i - 1] + r[i]
            ans.append(r2)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(10))
