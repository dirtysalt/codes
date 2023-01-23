#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm
# https://en.wikipedia.org/wiki/Roman_numerals

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        xs = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
        for (x, p) in xs:
            while s.startswith(p):
                n += x
                s = s[len(p):]
        return n


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('LXXIV'))
