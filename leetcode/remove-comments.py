#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        t = ''
        comment = 0
        ans = []
        for s in source:
            i = 0
            while i < len(s):
                c = s[i]
                i += 1

                # switch comment
                if comment == 0 and c == '/' and i < len(s) and s[i] == '*':
                    comment = 1
                    i += 1
                    continue

                if comment == 1 and c == '*' and i < len(s) and s[i] == '/':
                    comment = 0
                    i += 1
                    continue

                if comment == 1:
                    continue

                if c == '/' and i < len(s) and s[i] == '/':
                    break

                t += c

            if t and not comment:
                ans.append(t)
                t = ''

        assert comment == 0
        if t:
            ans.append(t)
        return ans
