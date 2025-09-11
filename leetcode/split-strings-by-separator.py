#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        s = separator.join(words)
        ss = s.split(separator)
        return [x for x in ss if x]


if __name__ == '__main__':
    pass
