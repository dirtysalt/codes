#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        value = None

        for i in range(len(number)):
            if number[i] == digit:
                s = number[:i] + number[i + 1:]
                if value is None or s > value:
                    value = s

        return value


if __name__ == '__main__':
    pass
