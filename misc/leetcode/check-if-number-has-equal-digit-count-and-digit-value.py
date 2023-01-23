#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def digitCount(self, num: str) -> bool:
        c = [0] * 10
        for x in num:
            x2 = ord(x) - ord('0')
            c[x2] += 1

        for i in range(len(num)):
            if c[i] != ord(num[i]) - ord('0'):
                return False

        return True


if __name__ == '__main__':
    pass
