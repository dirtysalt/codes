#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countDigits(self, num: int) -> int:
        x = num
        ans = 0
        while x:
            y = x % 10
            if num % y == 0:
                ans += 1
            x = x // 10
        return ans


if __name__ == '__main__':
    pass
