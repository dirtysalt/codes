#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        x = num // 3
        return [x - 1, x, x + 1]


if __name__ == '__main__':
    pass
