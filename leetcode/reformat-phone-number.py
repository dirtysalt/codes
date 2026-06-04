#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def reformatNumber(self, number: str) -> str:
        tmp = []
        s = number.replace('-', '').replace(' ', '')
        i = 0
        while len(s) - i > 4:
            tmp.append(s[i:i + 3])
            i += 3

        if len(s) - i == 4:
            tmp.append(s[i:i + 2])
            tmp.append(s[i + 2:])
        else:
            tmp.append(s[i:])

        ans = '-'.join(tmp)
        return ans
