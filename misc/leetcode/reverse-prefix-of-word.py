#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word
        a = word[:index + 1]
        b = word[index + 1:]
        return a[::-1] + b


if __name__ == '__main__':
    pass
