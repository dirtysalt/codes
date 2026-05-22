#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.


def climbingLeaderboard(scores, alice):
    scores = sorted(set(scores))

    def bs(s, x):
        n = len(scores)
        # s, e = 0, n-1
        e = n - 1
        pos = None
        while s <= e:
            m = (s + e) // 2
            if scores[m] == x:
                pos = m
                break
            if scores[m] > x:
                e = m - 1
            else:
                s = m + 1
        if pos is None:
            pos = e
        return n - pos, max(pos, 0)

    ans = []
    start = 0
    for x in alice:
        # print('>>>',start)
        rank, start = bs(start, x)
        ans.append(rank)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
