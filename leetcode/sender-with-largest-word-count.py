#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        from collections import Counter
        c = Counter()
        for m, s in zip(messages, senders):
            c[s] += len(m.split())

        tmp = [(v, k) for k, v in c.items()]
        tmp.sort()
        return tmp[-1][1]


if __name__ == '__main__':
    pass
