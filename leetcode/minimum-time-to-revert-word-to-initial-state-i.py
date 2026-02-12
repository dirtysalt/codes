#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        i, ans = 0, 0
        n = len(word)
        while i < n:
            i += k
            ans += 1
            if i < n and word[:n - i] == word[i:]:
                break
        return ans


if __name__ == '__main__':
    pass
