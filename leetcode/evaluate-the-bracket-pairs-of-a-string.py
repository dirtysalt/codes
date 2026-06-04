#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)

        output = []
        last = -1
        for i in range(len(s)):
            if s[i] == '(':
                last = i
            elif s[i] == ')':
                key = s[last + 1:i]
                if key in d:
                    output.append(d[key])
                else:
                    output.append('?')
                last = -1
            else:
                if last == -1:
                    output.append(s[i])

        ans = ''.join(output)
        return ans
