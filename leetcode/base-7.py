#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"

        ans = ''
        buf = []
        if num < 0:
            ans = '-'
            num = -num
        while num:
            buf.append(str(num % 7))
            num //= 7
        ans = ans + ''.join(buf[::-1])
        return ans


if __name__ == '__main__':
    pass
