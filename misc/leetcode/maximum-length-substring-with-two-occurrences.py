#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        cnt = [0] * 26
        j = 0
        ans = 0
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            cnt[c] += 1
            while cnt[c] == 3:
                c2 = ord(s[j]) - ord('a')
                cnt[c2] -= 1
                j += 1
            sz = i - j + 1
            ans = max(ans, sz)
        return ans


if __name__ == '__main__':
    pass
