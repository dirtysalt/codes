#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def rev_bs(xs, k, s, e):
    while s <= e:
        mid = (s + e) // 2
        if xs[mid] == k:
            return mid
        elif xs[mid] > k:
            s = mid + 1
        else:
            e = mid - 1
    return None


def bs(xs, k, s, e):
    while s <= e:
        mid = (s + e) // 2
        if xs[mid] == k:
            return mid
        elif xs[mid] > k:
            e = mid - 1
        else:
            s = mid + 1
    return None


def solve(xs, n, k):
    def search_pivot(xs, n):
        s, e = 0, n - 1
        while s <= e:
            mid = (s + e) // 2
            if (mid == 0 or (xs[mid] > xs[mid - 1])) and \
                    (mid == (n - 1) or (xs[mid] > xs[mid + 1])):
                return mid
            if mid == 0 or (xs[mid] > xs[mid - 1]):
                s = mid + 1
            else:
                e = mid - 1

    pivot = search_pivot(xs, n)
    res = bs(xs, k, 0, pivot)
    if res is not None:
        return res
    res = rev_bs(xs, k, pivot, len(xs) - 1)
    if res is not None:
        return res
    return 'OOPS! NOT FOUND'


t = int(input())
for _ in range(t):
    n, k = [int(x) for x in (input().rstrip().split())]
    xs = [int(x) for x in input().rstrip().split()]
    print(solve(xs, n, k))
