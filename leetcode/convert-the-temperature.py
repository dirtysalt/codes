#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        a = celsius + 273.15
        b = celsius * 1.80 + 32.0
        return [a, b]


if __name__ == '__main__':
    pass
