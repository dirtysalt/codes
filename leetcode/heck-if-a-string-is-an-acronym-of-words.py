#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return ''.join(x[0] for x in words) == s


if __name__ == '__main__':
    pass
