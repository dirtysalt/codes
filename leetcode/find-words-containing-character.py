#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            w = words[i]
            if w.find(x) != -1:
                ans.append(i)
        return ans


if __name__ == '__main__':
    pass
