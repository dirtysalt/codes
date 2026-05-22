#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def findLatestTime(self, s: str) -> str:
        def ok(ss):
            a = int(''.join(ss[:2]))
            b = int(''.join(ss[3:]))
            if a >= 12: return -1, ''
            if b >= 60: return -1, ''
            return a * 60 + b, ''.join(ss)

        def dfs(i):
            if i == 5:
                return ok(ss)
            t, r = -1, ''
            if ss[i] == '?':
                for j in range(0, 10):
                    ss[i] = chr(ord('0') + j)
                    a, b = dfs(i + 1)
                    if a > t:
                        t, r = a, b
                ss[i] = '?'
                return t, r
            else:
                return dfs(i + 1)

        ss = list(s)
        _, ans = dfs(0)
        return ans


if __name__ == '__main__':
    pass
