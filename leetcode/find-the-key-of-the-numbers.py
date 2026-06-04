#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        key = ['9'] * 4
        nums = [num1, num2, num3]
        nums = [str(x) for x in nums]
        nums = ['0' * (4 - len(x)) + x for x in nums]
        for i in range(4):
            v = min(x[i] for x in nums)
            key[i] = v

        return int(''.join(key))


if __name__ == '__main__':
    pass
