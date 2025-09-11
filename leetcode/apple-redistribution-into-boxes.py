#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        acc = 0
        for i in range(len(capacity)):
            acc += capacity[i]
            if acc >= total:
                return i + 1
        return -1


if __name__ == '__main__':
    pass
