#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)
        ans = 0
        for w in set(words1 + words2):
            if cnt1[w] == 1 and cnt2[w] == 1:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
