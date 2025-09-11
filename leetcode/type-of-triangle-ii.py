#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if (a + b) > c and (a + c) > b and (b + c) > a:
            if a == b == c:
                return "equilateral";
            elif a == b or b == c or a == c:
                return "isosceles"
            else:
                return "scalene"
        return "none"


if __name__ == '__main__':
    pass
