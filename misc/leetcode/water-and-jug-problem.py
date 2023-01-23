#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        visited = set()
        todo = []

        def new_state(st):
            (a, b) = st
            if (a, b) in visited:
                return
            visited.add((a, b))
            todo.append((a, b))

        new_state((0, 0))

        while todo:
            (a, b) = todo.pop()
            # print(a, b)
            if a == z or b == z or (a + b) == z:
                return True

            new_state((x, b))
            new_state((a, y))
            new_state((0, b))
            new_state((a, 0))

            if (a + b) > x:
                new_state((x, b + a - x))
            else:
                new_state((a + b, 0))

            if (a + b) > y:
                new_state((a + b - y, y))
            else:
                new_state((0, a + b))

        return False


cases = [
    (3, 5, 4, True),
    (2, 6, 5, False),
    (1, 2, 3, True)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().canMeasureWater, cases)
