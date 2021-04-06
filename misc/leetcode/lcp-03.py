#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        dx, dy = 0, 0
        paths = set()
        for c in command:
            paths.add((dx, dy))
            if c == 'U':
                dy += 1
            else:
                dx += 1
        paths.add((dx, dy))

        def norm(x, y):
            r = min(x // dx, y // dy)
            return x - r * dx, y - r * dy, r

        X, Y = x, y
        x, y, step = norm(X, Y)
        if (x, y) not in paths:
            return False
        # print(X, Y, x, y, step)

        for a, b in obstacles:
            a, b, s = norm(a, b)
            if s > step: continue
            if (a, b) not in paths: continue
            if s < step or (s == step and a <= x and b <= y):
                return False
        return True


cases = [
    ("URR", [], 3, 2, True),
    ("URR", [[2, 2]], 3, 2, False),
    ("URR", [[4, 2]], 3, 2, True),
    ("RRRUUU", [[3, 0]], 3, 3, False),
]

import aatest_helper

# cases.append(aatest_helper.read_case_from_file("/Users/zhyanzy/Downloads/in.txt", True))

aatest_helper.run_test_cases(Solution().robot, cases)
