#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        t = list(zip(heights, names))
        t.sort(reverse=True)
        ans = [x[1] for x in t]
        return ans


if __name__ == '__main__':
    pass
