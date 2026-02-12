#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def partitionString(self, s: str) -> int:

        ans = 1
        ss = set()
        for c in s:
            if c in ss:
                ans += 1
                ss.clear()
            ss.add(c)
        return ans


if __name__ == '__main__':
    pass
