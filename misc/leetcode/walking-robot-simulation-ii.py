#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DNAME = ['East', 'North', 'West', 'South']


class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = (0, 0)
        self.dir = 0

    def _move(self):
        r, c = self.pos
        dx, dy = DXY[self.dir]
        r2, c2 = r + dx, c + dy
        if 0 <= r2 < self.height and 0 <= c2 < self.width:
            self.pos = (r2, c2)
            return

        self.dir += 1
        self.dir %= 4
        self._move()

    def move(self, num: int) -> None:
        MOD = 2 * (self.height + self.width - 2)
        t = num // MOD
        if num % MOD == 0:
            if t > 0:
                num -= (t - 1) * MOD
        else:
            num = num % MOD

        while num:
            num -= 1
            self._move()

    def getPos(self) -> List[int]:
        r, c = self.pos
        return [c, r]

    def getDir(self) -> str:
        return DNAME[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

if __name__ == '__main__':
    pass
