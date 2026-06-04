#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        l, u = [-1] * 26, [-1] * 26
        for i in range(len(word)):
            c = ord(word[i]) - ord('a')
            if 0 <= c < 26:
                l[c] = i
            else:
                c = ord(word[i]) - ord('A')
                if u[c] == -1:
                    u[c] = i

        for i in range(26):
            if l[i] != -1 and u[i] != -1 and u[i] > l[i]:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
