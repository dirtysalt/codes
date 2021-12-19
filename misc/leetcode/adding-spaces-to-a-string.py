#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and spaces[j] == i:
                ans.append(' ')
                j += 1
            ans.append(s[i])
        return ''.join(ans)


if __name__ == '__main__':
    pass
