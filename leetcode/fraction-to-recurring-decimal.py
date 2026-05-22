#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        minus = False
        if numerator < 0:
            numerator = - numerator
            minus = not minus
        if denominator < 0:
            denominator = -denominator
            minus = not minus

        res = ""
        if minus:
            res += "-"
        if numerator >= denominator:
            res += "{}".format(numerator // denominator)
            numerator %= denominator
            if numerator == 0:
                return res
            res += "."
        else:
            res += "0."

        bits = []
        nums = {}
        numerator *= 10
        while (numerator != 0 and numerator not in nums):
            d = numerator // denominator
            nums[numerator] = len(bits)
            bits.append(d)
            numerator %= denominator
            numerator *= 10

        if numerator == 0:
            res += ''.join([str(x) for x in bits])
        else:
            recurring = nums[numerator]
            res += ''.join([str(x) for x in bits[:recurring]])
            res += '('
            res += ''.join([str(x) for x in bits[recurring:]])
            res += ')'
        return res


if __name__ == '__main__':
    s = Solution()
    print((s.fractionToDecimal(20, 3)))
    print((s.fractionToDecimal(-20, 3)))
    print((s.fractionToDecimal(2, 3)))
    print((s.fractionToDecimal(1, 2)))
    print((s.fractionToDecimal(2, 1)))
    print((s.fractionToDecimal(1379, 8773)))
    print((s.fractionToDecimal(-1379, 8773)))
