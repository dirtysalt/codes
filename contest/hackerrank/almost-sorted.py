#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3


# Complete the almostSorted function below.
def almostSorted(arr):
    xs = [(arr[i], i) for i in range(len(arr))]
    xs.sort()

    st = []
    for i in range(len(xs)):
        if xs[i][1] != i:
            st.append(xs[i][1])

    if len(st) == 0:
        print('yes')

    elif len(st) == 2:
        print('yes')
        print('swap %d %d' % (st[-1] + 1, st[0] + 1))

    else:
        ok = True
        for i in range(1, len(st)):
            if (st[i - 1] - st[i]) != 1:
                ok = False
                break
        if ok:
            print('yes')
            print('reverse %d %d' % (st[-1] + 1, st[0] + 1))
        else:
            print('no')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
