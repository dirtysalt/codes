#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        rot = [0, 1, 5, -1, -1, 2, 9, -1, 8, 6]

        def rot_ok(x):
            val = 0
            base = 1
            z = x
            while x:
                y = x % 10
                x = x // 10
                if rot[y] == -1:
                    return False
                val = val + rot[y] * base
                base *= 10
            return val != z

        ans = 0
        for x in range(1, N + 1):
            if rot_ok(x):
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.rotatedDigits(10))
