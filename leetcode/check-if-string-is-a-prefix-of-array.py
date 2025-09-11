#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        now = ''
        for w in words:
            now += w
            if now == s:
                return True
        return False


if __name__ == '__main__':
    pass
