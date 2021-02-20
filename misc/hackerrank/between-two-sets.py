#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def factors(x):
    ans = 0
    i = 1
    while i * i <= x:
        if x % i == 0:
            ans += 2
        i += 1
    if (i - 1) ** 2 == x:
        ans = ans - 1
    return ans


def getTotalX(a, b):
    # Write your code here
    r = 1
    for x in a:
        r = lcm(r, x)

    t = b[0]
    for x in b:
        t = gcd(t, x)

    # print(r, t)
    if t % r != 0:
        return 0
    ans = factors(t // r)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
