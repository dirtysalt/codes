#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    x = 5
    ans = 0
    for _ in range(n):
        liked = x // 2
        ans += liked
        x = liked * 3
    return ans


if __name__ == '__main__':
    import os, sys, atexit

    sys.stdin = open('tmp.in', 'r')
    os.environ['OUTPUT_PATH'] = 'tmp.out'


    def cat_out():
        print('===== output =====')
        with open('tmp.out', 'r') as fh:
            print(fh.read())


    atexit.register(cat_out)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
