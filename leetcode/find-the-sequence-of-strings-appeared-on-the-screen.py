#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        s = ""
        for c in target:
            d = ord(c) - ord('a')
            for i in range(d + 1):
                ans.append(s + chr(ord('a') + i))
            s += c
        return ans


if __name__ == '__main__':
    pass
