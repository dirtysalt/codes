#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []

        ans = []
        exp = 2
        while finalSum >= (exp + exp + 2):
            ans.append(exp)
            finalSum -= exp
            exp += 2
        ans.append(finalSum)
        return ans


if __name__ == '__main__':
    pass
