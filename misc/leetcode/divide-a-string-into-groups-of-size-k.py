#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            ss = s[i:i + k]
            i += k
            if len(ss) < k:
                ss += fill * (k - len(ss))
            ans.append(ss)
        return ans


if __name__ == '__main__':
    pass
