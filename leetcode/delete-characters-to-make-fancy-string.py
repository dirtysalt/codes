#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def makeFancyString(self, s: str) -> str:
        c = s[0]
        rep = 1
        buf = []
        for i in range(1, len(s)):
            if s[i] == c:
                rep += 1
                if rep >= 3:
                    continue
                else:
                    buf.append(c)
            else:
                buf.append(c)
                c = s[i]
                rep = 1
        buf.append(c)
        return ''.join(buf)


if __name__ == '__main__':
    pass
