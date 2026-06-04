#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:

        import functools
        @functools.cache
        def search(i, c):
            if i == len(word):
                return 0

            ans = (1 << 30)
            for j in range(26):
                fix = 1
                if j == (ord(word[i]) - ord('a')):
                    fix = 0
                if abs(c - j) > 1:
                    cost = search(i + 1, j) + fix
                    ans = min(ans, cost)

            return ans

        ans = search(0, -2)
        return ans


if __name__ == '__main__':
    pass
