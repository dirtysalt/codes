#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        ans = list(s)
        tmp, pos = [], []
        for i in range(n):
            if s[i] in 'aeiouAEIOU':
                tmp.append(s[i])
                pos.append(i)
        tmp.sort()
        for p, c in zip(pos, tmp):
            ans[p] = c
        return ''.join(ans)


if __name__ == '__main__':
    pass
