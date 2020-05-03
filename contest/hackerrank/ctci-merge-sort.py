#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# 这个算法没有问题，但是在HR上面使用Python3没有办法通过
# 幸好语法上和Pypy是完全兼容的，使用PyPy3就可以通过

# Complete the countInversions function below.
def countInversions(arr):
    res = _countInversions(arr, 0, len(arr))
    return res


def _countInversions(arr, s, e):
    n = (e - s)
    if n in (0, 1): return 0
    m = n // 2
    res = 0
    res += _countInversions(arr, s, s + m)
    res += _countInversions(arr, s + m, e)

    arr2 = []
    pa, pb = s, s + m
    while pa < (s + m):
        while pb < e and arr[pa] > arr[pb]:
            arr2.append(arr[pb])
            pb += 1
        if pb == e:
            break

        # pa < [m, pb-1] and arr[pa] > arr[m, pb-1]
        res += (pb - m - s)
        arr2.append(arr[pa])
        pa += 1

    if pb == e:
        arr2.extend(arr[pa: s + m])
        res += (pb - m - s) * (s + m - pa)
    else:
        arr2.extend(arr[pb: e])
    # print('arr = {}, arr2 = {}, res = {}'.format(arr[s:e], arr2, res))
    arr[s:e] = arr2
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

# print(countInversions([2,1,3,1,2]))
