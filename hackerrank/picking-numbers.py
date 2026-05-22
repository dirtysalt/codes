#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    cnt = [0] * 100
    for x in a:
        cnt[x] += 1
    ans = 0
    for i in range(100):
        x = cnt[i] + cnt[i - 1] if i > 0 else 0
        y = cnt[i] + cnt[i + 1] if (i + 1) < 100 else 0
        ans = max(ans, x, y)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
