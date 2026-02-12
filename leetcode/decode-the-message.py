#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        for c in key:
            if c != ' ' and c not in d:
                d[c] = chr(len(d) + ord('a'))

        ans = []
        for c in message:
            c2 = d.get(c, c)
            ans.append(c2)
        return ''.join(ans)


if __name__ == '__main__':
    pass
