#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import math
import os
import random
import re
import sys


def find_all():
    import itertools
    import numpy as np

    for x in itertools.permutations(list(range(1, 10))):
        tmp = np.array(x)
        tmp = tmp.reshape(3, 3)

        def test(x):
            xs = np.sum(x, axis=0).reshape(-1)
            ys = np.sum(x, axis=1).reshape(-1)
            zs = [x[0][0] + x[1][1] + x[2][2], x[0][2] + x[1][1] + x[2][0]]
            # print(xs, ys, zs)
            if all((x == xs[0] for x in itertools.chain(xs, ys, zs))):
                return True
            return False

        if test(tmp):
            print(repr(tmp))


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    def gen2():
        def array(x):
            return x

        cases = [
            array([[2, 7, 6], [9, 5, 1], [4, 3, 8]]),
            array([[2, 9, 4], [7, 5, 3], [6, 1, 8]]),
            array([[4, 3, 8], [9, 5, 1], [2, 7, 6]]),
            array([[4, 9, 2], [3, 5, 7], [8, 1, 6]]),
            array([[6, 1, 8], [7, 5, 3], [2, 9, 4]]),
            array([[6, 7, 2], [1, 5, 9], [8, 3, 4]]),
            array([[8, 1, 6], [3, 5, 7], [4, 9, 2]]),
            array([[8, 3, 4], [1, 5, 9], [6, 7, 2]]),
        ]
        for x in cases:
            yield x

    def cost(a):
        res = 0
        for i in range(3):
            for j in range(3):
                res += abs(a[i][j] - s[i][j])
        return res

    ans = 100
    for x in gen2():
        # print(x)
        ans = min(ans, cost(x))

    return ans


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + "\n")

    fptr.close()
