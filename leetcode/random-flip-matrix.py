#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import random

from typing import List


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.size = n_rows * n_cols
        self.choose = set()
        self.rnd = random.Random(42)

    def flip(self) -> List[int]:
        while True:
            x = self.rnd.randint(0, self.size - 1)
            if x in self.choose:
                continue

            r = x // self.n_cols
            c = x % self.n_cols
            self.choose.add(x)
            return [r, c]

    def reset(self) -> None:
        self.choose.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()

# import aatest_helper
# null = None
# cases = [
#     (["Solution", "flip", "flip", "flip", "flip"], [
#      [2, 3], [], [], [], []], [null, [0, 1], [1, 2], [1, 0], [1, 1]])
# ]
# aatest_helper.run_simulation_cases(Solution, cases)
