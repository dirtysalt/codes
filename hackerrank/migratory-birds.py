#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    cnt = [0] * 6
    for x in arr:
        cnt[x] += 1

    ans = 1
    for i in range(1, 6):
        if cnt[i] > cnt[ans]:
            ans = i
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
