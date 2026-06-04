#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        n = len(asteroids)

        for i in range(n):
            x = asteroids[i]
            if x > mass:
                return False
            mass += x

        return True


if __name__ == '__main__':
    pass
