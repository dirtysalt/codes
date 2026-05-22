#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        for c in s:
            if c == 'i':
                ans = ans[::-1]
            else:
                ans.append(c)
        return ''.join(ans)


if __name__ == '__main__':
    pass
