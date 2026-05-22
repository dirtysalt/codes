#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.cx, self.cy = x_center, y_center

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(self.cx - self.radius, self.cx + self.radius)
            y = random.uniform(self.cy - self.radius, self.cy + self.radius)
            if ((x - self.cx) ** 2 + (y - self.cy) ** 2) <= self.radius ** 2:
                break
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
