#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)

        def trans(ss):
            tmp = []
            for c in ss:
                c2 = ord(c) - ord('a') + 25
                c2 = c2 % 26
                tmp.append(chr(c2 + ord('a')))
            return ''.join(tmp)

        idx = 0
        while idx < n:
            if s[idx] == 'a':
                idx += 1
            else:
                break

        if idx == n:
            return s[:n - 1] + trans(s[n - 1:])

        idx2 = idx
        while idx2 < n:
            if s[idx2] != 'a':
                idx2 += 1
            else:
                break

        ans = s[:idx] + trans(s[idx:idx2]) + s[idx2:]
        return ans


if __name__ == '__main__':
    pass
