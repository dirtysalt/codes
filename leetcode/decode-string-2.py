#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def decodeString(self, s: str) -> str:

        def parse_string(s, i, until=None):
            ans = ''

            while i < len(s):
                if until and s[i] == until:
                    i += 1
                    break

                if s[i].isdigit():
                    res, j = parse_repeat(s, i)
                    ans += res
                    i = j
                else:
                    ans += s[i]
                    i += 1

            return ans, i

        def parse_repeat(s, i):
            r = 0
            while s[i] != '[':
                r = r * 10 + ord(s[i]) - ord('0')
                i += 1
            res, j = parse_string(s, i + 1, ']')
            return res * r, j

        ans, _ = parse_string(s, 0)
        return ans
