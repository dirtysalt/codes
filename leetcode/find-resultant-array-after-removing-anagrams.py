#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        st = []
        for w in words:
            w2 = sorted(w)
            if st and st[-1][1] == w2:
                continue
            st.append((w, w2))

        ans = [x[0] for x in st]
        return ans

if __name__ == '__main__':
    pass
