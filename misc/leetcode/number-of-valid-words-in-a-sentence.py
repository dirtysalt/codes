#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countValidWords(self, sentence: str) -> int:
        def ischar(t):
            c = ord(t) - ord('a')
            return c >= 0 and c < 26

        def isdigit(t):
            c = ord(t) - ord('0')
            return c >= 0 and c < 10

        def istoken(t):
            d = 0
            for i in range(len(t)):
                if ischar(t[i]): continue
                if isdigit(t[i]): return False

                if t[i] == '-':
                    d += 1
                    if d > 1: return False
                    if i > 0 and (i + 1) < len(t) and ischar(t[i - 1]) and ischar(t[i + 1]):
                        pass
                    else:
                        return False

                if t[i] in '!.,':
                    if (i + 1) != len(t):
                        return False

            return True

        ans = 0
        for t in sentence.split():
            if istoken(t):
                ans += 1

        return ans


if __name__ == '__main__':
    pass
