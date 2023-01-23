#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_int = (1 << 31) - 1
        if divisor == 0: return max_int
        if dividend == 0: return 0
        invert = (dividend ^ divisor) < 0

        x = abs(dividend)
        y = abs(divisor)
        res = 0
        for i in range(32, -1, -1):
            z = (y << i)
            if x >= z:
                x -= z
                res += (1 << i)
        if invert:
            res = -res
            # not compatible with python division.
            # res = -(res + (1 if x > 0 else 0))
        return min(res, max_int)


if __name__ == '__main__':
    s = Solution()
    print(s.divide(-14, 3), -14 / 3)
    print(s.divide(-14, -3), -14 / -3)
    print(s.divide(14, 3), 14 / 3)
    print(s.divide(14, -3), 14 / -3)
