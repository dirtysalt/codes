#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)

        ans = 0
        for i in range(n):
            if word[i] in 'aeiou':
                a = (i + 1)
                b = n - i
                ans += a * b
        return ans


if __name__ == '__main__':
    pass
