#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.


def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles = set(((n-x[0], x[1]-1) for x in obstacles))
    r_q, c_q = n - r_q, c_q - 1

    ans = 0
    for dx, dy in [(x, y) for x in range(-1, 2) for y in range(-1, 2)]:
        if dx == 0 and dy == 0:
            continue
        r, c = r_q + dx, c_q + dy
        while 0 <= r < n and 0 <= c < n and (r, c) not in obstacles:
            print(r, c)
            ans += 1
            r += dx
            c += dy
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
