#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


#
# Complete the 'countCups' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY balls
#  3. 2D_INTEGER_ARRAY swaps
#  4. 2D_INTEGER_ARRAY queries
#

def countCups(n, balls, swaps, queries):
    balls = set(balls)
    for a, b in swaps:
        ae = a in balls
        be = b in balls
        if (ae and be) or (not ae and not be): continue
        if ae:
            balls.remove(a)
            balls.add(b)
        if be:
            balls.remove(b)
            balls.add(a)
    balls = list(balls)
    balls.sort()

    # print(balls)
    import bisect
    ans = []
    for l, r in query:
        x = bisect.bisect(balls, r)
        y = bisect.bisect(balls, l - 1)
        z = x - y
        ans.append(z)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    q = int(first_multiple_input[3])

    balls = list(map(int, input().rstrip().split()))

    swaps = []

    for _ in range(s):
        swaps.append(list(map(int, input().rstrip().split())))

    query = []

    for _ in range(q):
        query.append(list(map(int, input().rstrip().split())))

    result = countCups(n, balls, swaps, query)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
