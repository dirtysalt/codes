#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = int(area ** 0.5)
        while l * l < area:
            l += 1

        while True:
            if area % l == 0:
                w = area // l
                return [l, w]
            l += 1


if __name__ == '__main__':
    pass
