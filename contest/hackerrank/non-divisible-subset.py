#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    # Write your code here
    dup = set()
    cnt = [0] * k
    for v in s:
        if v in dup:
            continue
        dup.add(v)
        cnt[v % k] += 1

    # print(cnt)
    ans = 0
    # 余数为0只能选择一个
    if cnt[0] != 0:
        ans += 1
    # i, k-i只能选择最大的
    # 如果i == k-i的话，那么这个值也只能选择1个
    for i in range(1, k // 2+1):
        j = k - i
        if i != j:
            ans += max(cnt[i], cnt[j])
        else:
            ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
