#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    ans = (s - 1 + m - 1) % n + 1
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

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
