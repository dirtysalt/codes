#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:

        def diff(s):
            res = []
            for i in range(1, len(s)):
                d = ord(s[i]) - ord(s[i - 1])
                res.append(d)
            return tuple(res)

        ss = [diff(w) for w in words]
        if ss[0] == ss[1]:
            for i in range(2, len(ss)):
                if ss[i] != ss[0]:
                    return words[i]
        elif ss[0] == ss[2]:
            return words[1]
        else:
            return words[0]


if __name__ == '__main__':
    pass
