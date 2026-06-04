#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def minAnagramLength(self, s: str) -> int:
        total = [0] * 26
        for c in s:
            c2 = ord(c) - ord('a')
            total[c2] += 1

        cnt = [0] * 26
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            cnt[c] += 1

            sz = (i + 1)
            rep = (len(s) + sz - 1) // sz
            ok = True
            for j in range(26):
                if (cnt[j] * rep) != total[j]:
                    ok = False
                    break
            if ok: return sz
        return len(s)


if __name__ == '__main__':
    pass
