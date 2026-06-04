#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        from collections import defaultdict
        n = len(words)
        used = [0] * n
        repo = defaultdict(list)
        for i in range(n):
            w = words[i]
            repo[w].append(i)

        size = 0
        for i in range(n):
            if used[i]: continue
            match = False
            w = words[i]
            w2 = w[::-1]
            ss = repo[w2]
            while ss:
                j = ss.pop()
                if i != j and not used[j]:
                    size += 4
                    used[i] = 1
                    used[j] = 1
                    break

        for i in range(n):
            if not used[i] and words[i] == words[i][::-1]:
                size += 2
                break
        return size


if __name__ == '__main__':
    pass
