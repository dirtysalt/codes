#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = []
            i = 0
            while i < len(s):
                r = 0
                for j in range(i, min(i + k, len(s))):
                    r += int(s[j])
                tmp.append(str(r))
                i += k
            s = ''.join(tmp)
        return s


if __name__ == '__main__':
    pass
