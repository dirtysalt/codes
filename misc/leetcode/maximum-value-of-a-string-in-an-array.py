#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        def value(s):
            acc = 0
            for c in s:
                x = ord(c) - ord('0')
                if 0 <= x < 10:
                    acc = acc * 10 + x
                else:
                    return len(s)
            return acc

        return max((value(x) for x in strs))

if __name__ == '__main__':
    pass
