#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.


def acmTeam(topic):
    n = len(topic)
    topic = [[ord(c) - ord('0') for c in x] for x in topic]

    def score(a, b):
        return sum((x | y for (x, y) in zip(a, b)))

    ans = 0
    _max = 0
    for i in range(n-1):
        for j in range(i+1, n):
            val = score(topic[i], topic[j])
            # print(i, j, val)
            if val == _max:
                ans += 1
            elif val > _max:
                _max = val
                ans = 1
            else:
                pass
    return (_max, ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
