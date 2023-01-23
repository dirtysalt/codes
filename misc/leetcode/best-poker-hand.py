#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if all((x == suits[0]) for x in suits): return "Flush"
        from collections import Counter
        c = Counter(ranks)
        a = c.most_common()[0][1]
        if a >= 3:
            return "Three of a Kind"
        elif a >= 2:
            return "Pair"
        return "High Card"


if __name__ == '__main__':
    pass
