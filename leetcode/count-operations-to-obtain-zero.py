#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 and num2:
            if num1 < num2:
                num1, num2 = num2, num1
            mod = num1 // num2
            ans += mod
            num1 -= num2 * mod
        return ans

if __name__ == '__main__':
    pass
