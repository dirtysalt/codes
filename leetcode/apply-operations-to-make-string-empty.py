#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = [0] * 26
        pos = [-1] * 26

        for i in range(len(s)):
            c2 = ord(s[i]) - ord('a')
            cnt[c2] += 1
            pos[c2] = i

        maxc = max(cnt)
        left = []
        for i in range(26):
            if cnt[i] == maxc:
                left.append(i)
        left.sort(key=lambda x: pos[x])
        ans = ''.join([chr(x + ord('a')) for x in left])
        return ans


if __name__ == '__main__':
    pass
