#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for s in sentences:
            ans = max(ans, len(s.split()))
        return ans


if __name__ == '__main__':
    pass
