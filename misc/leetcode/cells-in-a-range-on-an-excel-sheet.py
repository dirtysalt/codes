#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        r0, c0 = ord(s[0]) - ord('a'), int(s[1])
        r1, c1 = ord(s[3]) - ord('a'), int(s[4])

        ans = []
        for i in range(r0, r1 + 1):
            for j in range(c0, c1 + 1):
                x = '%s%d' % (chr(ord('a') + i), j)
                ans.append(x)
        return ans


if __name__ == '__main__':
    pass
