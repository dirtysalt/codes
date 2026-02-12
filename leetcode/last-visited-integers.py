#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        st = []
        p = 0
        ans = []
        for x in words:
            if x == 'prev':
                p += 1
                v = st[-p] if p <= len(st) else -1
                ans.append(v)
            else:
                p = 0
                st.append(int(x))
        return ans


if __name__ == '__main__':
    pass
